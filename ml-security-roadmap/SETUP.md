# Your ML Security environment: everything you need

You don't need to install everything on day 1. Each tool is tagged with the **phase** where you need it.

## Hardware

| | Minimum | Good |
|---|---|---|
| Computer | Any laptop with 8 GB RAM | 16 GB+ RAM, recent CPU |
| GPU | Not needed (use Google Colab's free GPU) | NVIDIA GPU with 8 GB+ VRAM for local LLMs |
| Disk | 30 GB free | 100 GB+ SSD (models are large) |

**Only have a phone?** You can start Phases 0–2 with **Google Colab** (colab.research.google.com),
which runs Python + GPU in the browser for free, plus PortSwigger/TryHackMe labs in a browser.
You'll want a laptop by Phase 4.

---

## 1. Operating system (Phase 0)

- **Windows:** install **WSL2 + Ubuntu** (open PowerShell as admin → `wsl --install`, then restart).
  Do your security/ML work inside Ubuntu; most tools assume Linux.
- **Mac:** use the built-in Terminal + install **Homebrew** (brew.sh).
- **Linux:** you're already set (Ubuntu recommended).
- **Later (Phase 3):** **Kali Linux** in VirtualBox or WSL, which comes with hacking tools preinstalled.

## 2. Core tools (Phase 0)

| Tool | Why | Install |
|---|---|---|
| **VS Code** | Code editor | code.visualstudio.com, then add extensions: Python, Jupyter, WSL (Windows) |
| **Python 3.11+** | Main language for ML & security | Ubuntu: `sudo apt install python3 python3-venv python3-pip` · Mac: `brew install python` |
| **Git + GitHub account** | Save & share your work | `sudo apt install git` / `brew install git`, then github.com |
| **Node.js (LTS)** | Needed for promptfoo | nodejs.org or `brew install node` |

Set up a project environment (do this once, in this folder):

```bash
cd ml-security-roadmap
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Every time you come back to work: `source .venv/bin/activate`.

## 3. Math & ML (Phases 1–2)

Installed by `requirements.txt`: numpy, pandas, matplotlib, scikit-learn, jupyter, **PyTorch**,
torchvision, Hugging Face `transformers` + `datasets`.

- Open notebooks: `jupyter lab`
- **GPU users:** install PyTorch with the command from pytorch.org (pick your CUDA version)
  *before* running `pip install -r requirements.txt`.
- Free GPU alternative: Google Colab or Kaggle Notebooks.

## 4. Local LLMs (Phase 2 → 4)

**Ollama** runs open-source LLMs on your own computer. It's free, needs no API key, and
it's the safe, legal target to attack.

```bash
# Linux / WSL
curl -fsSL https://ollama.com/install.sh | sh
# Mac/Windows: download from ollama.com

ollama pull llama3.2          # ~2 GB, works on 8 GB RAM
ollama run llama3.2           # chat with it to check it works
```

For RAG projects: `pip install chromadb` (vector database) plus an embedding model:
`ollama pull nomic-embed-text`.

## 5. Web security tools (Phase 3)

| Tool | Why | Get it |
|---|---|---|
| **Burp Suite Community** | Intercept & modify web/API traffic (SSRF, auth bugs) | portswigger.net/burp |
| **PortSwigger Academy account** | Free labs | portswigger.net/web-security |
| **TryHackMe account** | Guided hacking rooms | tryhackme.com |
| **OWASP Juice Shop** | Vulnerable app to practise on | `docker run -p 3000:3000 bkimminich/juice-shop` |
| **Docker Desktop** | Run vulnerable apps & tools safely in containers | docker.com |
| **Postman** or `curl` | Talk to APIs | postman.com |

## 6. AI security / red-teaming tools (Phase 4, the ones from the video)

```bash
source .venv/bin/activate

# IBM Adversarial Robustness Toolbox: attacks & defences for ML models
pip install adversarial-robustness-toolbox

# garak (NVIDIA): LLM vulnerability scanner
pip install garak
python -m garak --list_probes                       # see what it can test
python -m garak --model_type ollama --model_name llama3.2 --probes promptinject
#   (newer garak versions call these --target_type / --target_name; check `python -m garak --help`)

# PyRIT (Microsoft): automate AI red teaming
pip install pyrit

# promptfoo: test & red-team prompts and LLM apps (needs Node.js)
npx promptfoo@latest redteam setup                  # opens a guided web UI
```

> PyRIT and garak have many dependencies. If they conflict, give each its own venv:
> `python3 -m venv .venv-garak`, and so on.

Practice targets (all legal):
- **Gandalf** by Lakera: gandalf.lakera.ai
- **PortSwigger "Web LLM attacks"** labs
- **Crucible** by Dreadnode: crucible.dreadnode.io
- Your own Ollama model and your own RAG chatbot

## 7. Learning & productivity tools

| Tool | Use |
|---|---|
| **Obsidian** (or Notion) | Notes: one note per attack / paper / lab |
| **Zotero** | Organise research papers (NeurIPS, arXiv) |
| **arXiv** (arxiv.org, `cs.CR` + `cs.LG`) | New papers |
| **X / Twitter, LinkedIn** | Follow researchers, share progress |
| **Anki** | Flashcards for math & security terms |

## 8. Optional paid APIs (later)

Testing against hosted models (OpenAI, Anthropic, Google) costs money and must follow their
usage policies. **Stick to local models via Ollama until Phase 4 is solid.**

---

## Quick check that everything works

```bash
source .venv/bin/activate
python -c "import torch, sklearn, transformers; print('ML stack OK, torch', torch.__version__)"
python labs/01_fgsm_attack.py       # your first adversarial attack
ollama run llama3.2 "Say hi"        # local LLM OK
```
