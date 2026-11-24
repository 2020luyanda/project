"""
Lab 01: Your first adversarial attack (FGSM)
=============================================

What you'll learn
-----------------
1. Train a small neural network that recognises handwritten digits (MNIST).
2. Attack it with the Fast Gradient Sign Method (FGSM; Goodfellow et al., 2014).
   FGSM adds a tiny change to each pixel, in the direction that INCREASES the
   model's error:

        x_adv = x + epsilon * sign( d loss / d x )

   The image still looks the same to a human, but the model gets it wrong.
3. See how accuracy collapses as epsilon (the attack strength) grows.

This is why the math in Phase 1 matters: the attack is literally "use the
model's own gradient against it".

Run it
------
    pip install torch torchvision matplotlib
    python 01_fgsm_attack.py

It takes ~1-3 minutes on a normal laptop CPU (no GPU needed).

Exercises after it works
------------------------
  a) Change EPSILONS and find the smallest epsilon that drops accuracy below 50%.
  b) Implement PGD: repeat FGSM 10 times with a small step, clipping each time.
  c) Defence: "adversarial training". Train on a mix of clean + FGSM images,
     then re-run the attack. Does robustness improve? What happens to clean accuracy?
  d) Redo the attack with IBM's Adversarial Robustness Toolbox (ART):
     pip install adversarial-robustness-toolbox
     (see art.attacks.evasion.FastGradientMethod)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

torch.manual_seed(0)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EPSILONS = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]


# 1. A small convolutional neural network -----------------------------------
class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)  # 28x28 -> 14x14
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # 14x14 -> 7x7
        x = x.flatten(1)
        x = F.relu(self.fc1(x))
        return self.fc2(x)  # raw scores (logits) for digits 0-9


# 2. Data (pixel values stay in [0, 1] so the attack is easy to reason about)
def get_data():
    tfm = transforms.ToTensor()
    train = datasets.MNIST("data", train=True, download=True, transform=tfm)
    test = datasets.MNIST("data", train=False, download=True, transform=tfm)
    return (
        DataLoader(train, batch_size=128, shuffle=True),
        DataLoader(test, batch_size=500, shuffle=False),
    )


# 3. Train ------------------------------------------------------------------
def train(model, loader, epochs=1):
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    model.train()
    for epoch in range(epochs):
        for i, (x, y) in enumerate(loader):
            x, y = x.to(DEVICE), y.to(DEVICE)
            loss = F.cross_entropy(model(x), y)
            opt.zero_grad()
            loss.backward()
            opt.step()
            if i % 100 == 0:
                print(f"  epoch {epoch + 1} batch {i:4d}  loss {loss.item():.3f}")


# 4. The attack -------------------------------------------------------------
def fgsm(model, x, y, epsilon):
    """Return adversarial versions of images x (true labels y)."""
    x = x.clone().detach().requires_grad_(True)
    loss = F.cross_entropy(model(x), y)
    model.zero_grad()
    loss.backward()  # gradient of the loss with respect to the INPUT pixels
    x_adv = x + epsilon * x.grad.sign()  # step that makes the model more wrong
    return x_adv.clamp(0, 1).detach()  # keep it a valid image


def accuracy_under_attack(model, loader, epsilon):
    model.eval()
    correct = total = 0
    for x, y in loader:
        x, y = x.to(DEVICE), y.to(DEVICE)
        if epsilon > 0:
            x = fgsm(model, x, y, epsilon)
        with torch.no_grad():
            correct += (model(x).argmax(1) == y).sum().item()
        total += y.size(0)
    return correct / total


def save_example(model, loader, epsilon=0.2, path="fgsm_example.png"):
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("(install matplotlib to save a picture of the attack)")
        return
    model.eval()
    x, y = next(iter(loader))
    x, y = x[:6].to(DEVICE), y[:6].to(DEVICE)
    x_adv = fgsm(model, x, y, epsilon)
    with torch.no_grad():
        p_clean, p_adv = model(x).argmax(1), model(x_adv).argmax(1)
    fig, axes = plt.subplots(2, 6, figsize=(12, 4.5))
    for i in range(6):
        axes[0, i].imshow(x[i, 0].cpu(), cmap="gray")
        axes[0, i].set_title(f"clean: {p_clean[i].item()}")
        axes[1, i].imshow(x_adv[i, 0].cpu(), cmap="gray")
        axes[1, i].set_title(f"attacked: {p_adv[i].item()}")
        axes[0, i].axis("off")
        axes[1, i].axis("off")
    fig.suptitle(f"FGSM attack, epsilon = {epsilon}")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    print(f"Saved picture of the attack to {path}")


if __name__ == "__main__":
    print(f"Using device: {DEVICE}")
    train_loader, test_loader = get_data()
    model = SmallCNN().to(DEVICE)

    print("Training the model (1 epoch)...")
    train(model, train_loader, epochs=1)

    print("\nAccuracy as the attack gets stronger:")
    print(" epsilon | accuracy")
    print("---------+---------")
    for eps in EPSILONS:
        acc = accuracy_under_attack(model, test_loader, eps)
        bar = "#" * int(acc * 40)
        print(f"  {eps:5.2f}  |  {acc * 100:5.1f}%  {bar}")

    save_example(model, test_loader)
    print("\nDone! Now try the exercises at the top of this file.")
