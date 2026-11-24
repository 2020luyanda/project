# ML / AI Security Roadmap (from zero to AI red teamer)

This roadmap is based on the reel **"22yo engineer explains how to learn ML security"** (@remonbiz).
Everything he mentions in the video is covered here, in a sensible order:

| From the video | Where it is in this roadmap |
|---|---|
| Studying real security incidents (AI-found flaws, "Black October") | Habit #1, Phase 5 |
| *Mathematics for Machine Learning* (book) | Phase 1 |
| How ML works (training set → algorithm → model → prediction) | Phase 2 |
| Server-Side Request Forgery (SSRF), authentication | Phase 3 |
| Attack surfaces of LLM apps / MCP / agents / tools / memory | Phase 4 |
| Backdoors & supply chain (SolarWinds) | Phase 4 |
| IBM tools (Adversarial Robustness Toolbox) | Phase 4 |
| Prompt injection, jailbreaking, RAG poisoning | Phase 4 |
| PyRIT, garak, promptfoo | Phase 4 (labs) |
| NeurIPS / research papers | Phase 5 |
| Security newsletters + "Tech Twitter" (X) | Habits, Phase 5 |

> **Ethics rule (read this first):** only attack systems you own, local models, CTFs, or programs that
> explicitly allow it (bug bounty scope). Testing other people's apps without permission is illegal
> in most countries, including under South Africa's Cybercrimes Act. Everything in this roadmap
> runs on your own machine or on practice platforms made for it.

---

## The big picture

ML security = **three skills** combined:

```
   Programming (Python)  +  Machine Learning  +  Security (hacker mindset)
                    \            |             /
                     ---> ML / AI Security <---
```

You don't need to be an expert in all three before starting. Learn them in parallel,
but in the order below. **Rough time: 9–12 months at ~1.5–2 hours a day.**

---

## Phase 0: Setup and foundations (Weeks 1–3)

**Goal:** a working environment and enough Python to read and write scripts.

- Set up your machine using [SETUP.md](SETUP.md).
- Python basics: variables, loops, functions, lists/dicts, files, `pip`, virtual environments.
- Git and GitHub basics: clone, commit, push.
- Linux terminal basics: `cd`, `ls`, `cat`, `grep`, pipes, permissions.

**Resources (free):**
- *Python for Everybody* (Dr. Chuck): py4e.com
- *The Missing Semester of Your CS Education* (MIT): missing.csail.mit.edu (shell, git, editors)
- OverTheWire **Bandit** (learn Linux by playing a hacking game): overthewire.org/wargames/bandit

**Project:** a Python script that reads a text file and counts word frequencies; push it to GitHub.

---

## Phase 1: Math for ML (Weeks 3–8, in parallel with Phase 2)

**Goal:** understand *why* models work, so you understand *why* attacks work.
Adversarial attacks are literally "use the gradient against the model".

Topics:
1. Linear algebra: vectors, matrices, dot product, matrix multiplication.
2. Calculus: derivatives, the chain rule, **gradients**.
3. Probability & statistics: distributions, mean/variance, Bayes' rule.
4. Optimization: gradient descent.

**Resources:**
- 📘 ***Mathematics for Machine Learning***, by Deisenroth, Faisal & Ong (the book in the video, free PDF at mml-book.github.io)
- 3Blue1Brown on YouTube: *Essence of Linear Algebra* and *Essence of Calculus* (watch these **first**)
- Khan Academy for any gaps

Don't try to finish the whole book before moving on. Read chapters 2 (linear algebra),
5 (vector calculus) and 6 (probability), and come back when you need more.

---

## Phase 2: Machine learning & deep learning (Weeks 4–14)

**Goal:** train your own models, so you can then break them.

Topics:
- Training set → learning algorithm → model → prediction (the diagram in the video)
- Supervised learning: regression, classification, overfitting, train/test split
- Neural networks, backpropagation, PyTorch
- CNNs (images), and then **transformers & LLMs** (the most important today)
- Embeddings & vector databases (needed to understand RAG)

**Resources:**
- Andrew Ng, *Machine Learning Specialization* (Coursera, free to audit)
- fast.ai, *Practical Deep Learning for Coders* (free, very hands-on)
- Andrej Karpathy, *Neural Networks: Zero to Hero* (YouTube; build GPT from scratch)
- Hugging Face LLM Course: huggingface.co/learn

**Projects:**
1. Train an MNIST digit classifier in PyTorch.
2. Fine-tune a small text classifier with Hugging Face.
3. Build a tiny RAG chatbot (local LLM via Ollama + a vector DB like Chroma).
   **Keep it**, because you'll attack it in Phase 4.

---

## Phase 3: Classic security (Weeks 8–20, in parallel)

**Goal:** the hacker mindset. AI apps are still web apps, and most real AI incidents
are classic bugs (SSRF, broken auth, injection) reached *through* the AI.

Topics:
- Networking: HTTP, DNS, TCP/IP, how APIs work
- **OWASP Top 10**: injection, broken access control, **authentication** failures, **SSRF**
- Burp Suite basics (intercepting and modifying requests)
- Threat modelling: "what are the assets, who is the attacker, what are the **attack surfaces**?"

**Resources:**
- **PortSwigger Web Security Academy** (free, best on the internet): portswigger.net/web-security
  Do the SSRF, authentication, access-control and API labs.
- TryHackMe: "Pre Security" → "Jr Penetration Tester" paths
- OWASP Juice Shop (a deliberately vulnerable app you run locally)

**Project:** finish all PortSwigger *Apprentice* labs for SSRF + authentication. Write short notes for each.

---

## Phase 4: ML / AI security, the core (Weeks 16–36)

### 4a. Attacks on classic ML models
| Attack | What it means |
|---|---|
| **Evasion / adversarial examples** | Tiny input changes that fool a model (FGSM, PGD) |
| **Data poisoning & backdoors** | Corrupt training data so the model has a hidden trigger |
| **Model extraction / stealing** | Copy a model by querying its API |
| **Membership inference** | Learn whether someone's data was in the training set |
| **Supply chain** | Malicious model files (pickle), poisoned packages. Same idea as the **SolarWinds** backdoor, applied to ML |

Tool: **IBM Adversarial Robustness Toolbox (ART)**, `pip install adversarial-robustness-toolbox`
(this is "the tools from IBM" in the video).

### 4b. Attacks on LLM apps & agents (the hottest area right now)
| Attack | What it means |
|---|---|
| **Prompt injection** | Input that overrides the system's instructions (direct or hidden in documents/web pages = *indirect*) |
| **Jailbreaking** | Getting the model to break its safety rules |
| **RAG poisoning** | Planting malicious content in the documents a RAG system retrieves |
| **Tool / MCP poisoning** | Malicious tool descriptions or tool outputs that hijack an agent |
| **Memory poisoning** | Corrupting an agent's long-term memory |
| **Data exfiltration** | Tricking the model into leaking secrets (e.g. via markdown image links) |
| **Excessive agency** | Agent has more permissions than needed, so injection becomes real damage (SSRF, deleting files) |

Read: **OWASP Top 10 for LLM Applications** (genai.owasp.org) and **MITRE ATLAS** (atlas.mitre.org).

### 4c. The red-teaming tools from the video
| Tool | By | What it does |
|---|---|---|
| **garak** | NVIDIA | LLM vulnerability scanner ("nmap for LLMs") |
| **PyRIT** | Microsoft | Framework to automate red teaming of AI systems |
| **promptfoo** | open source | Test & red-team prompts/apps from a config file; great for CI |

### Labs (do them in this order)
1. `labs/01_fgsm_attack.py` (in this folder): fool an image classifier with the FGSM attack.
2. Same attack using IBM ART instead of hand-written code.
3. Gandalf by Lakera (gandalf.lakera.ai): prompt-injection game, 8 levels.
4. PortSwigger **"Web LLM attacks"** labs.
5. Run **garak** against a local model in Ollama (see SETUP.md).
6. Run **promptfoo redteam** against your Phase 2 RAG chatbot.
7. Use **PyRIT** to automate a multi-turn jailbreak against your own local model.
8. Poison your own RAG: add a document with hidden instructions and watch the bot obey it. Then build a defence and measure it.

**Courses:**
- *Red Teaming LLM Applications* (DeepLearning.AI short course, free)
- Microsoft *AI Red Teaming 101*, and the PyRIT docs
- NVIDIA *Exploring Adversarial Machine Learning* (DLI)

---

## Phase 5: Go deep and get visible (Month 9+)

- **Read papers:** NeurIPS, ICML, IEEE S&P, USENIX Security, and the SaTML conference. Start with:
  - Goodfellow et al., *Explaining and Harnessing Adversarial Examples* (FGSM)
  - Greshake et al., *Not what you've signed up for* (indirect prompt injection)
  - Zou et al., *Universal and Transferable Adversarial Attacks on Aligned LLMs* (GCG)
  - Carlini et al., *Extracting Training Data from Large Language Models*
- **Study incidents:** for each AI security news story, write down: what was the attack surface,
  the bug, the impact, and the fix.
- **CTFs & bounties:** AI Village CTF (DEF CON), Crucible by Dreadnode, HackAPrompt,
  and AI bug bounty programs (huntr, HackerOne AI programs). **Stay in scope.**
- **Share what you learn:** a blog, GitHub, X/LinkedIn. This is how people get hired in this field.

---

## Daily habits (from the video)

1. **Follow incidents:** 10 minutes a day reading security news.
2. **Newsletters:** Simon Willison's blog (prompt injection), *tl;dr sec*, *Last Week in AI*,
   Bruce Schneier's *Crypto-Gram*, Embrace The Red (Johann Rehberger's blog).
3. **Tech Twitter / X:** follow AI security researchers (e.g. @simonw, @wunderwuzzi23,
   @NicholasCarlini, @elder_plinius, @garak_llm, @promptfoo), plus the creator of the reel.
4. **Build in public:** post one thing you learned each week.

## Weekly study schedule (~10–12 h/week)

| Day | Focus |
|---|---|
| Mon | Math (1 h) + Python (1 h) |
| Tue | ML course (1.5 h) |
| Wed | Security labs: PortSwigger/TryHackMe (1.5 h) |
| Thu | ML course / project (1.5 h) |
| Fri | AI security lab or tool (1.5 h) |
| Sat | Project day (2–3 h): build something, push to GitHub |
| Sun | Read 1 paper/incident + write notes (1 h) |

## Learning method

1. **Learn → build → break → write.** For every concept, build a small thing, attack it, and write a note.
2. **Don't get stuck on theory.** If you're stuck for 2+ days, move on and come back.
3. **Keep a notes folder** (`notes/` in this repo, or Obsidian/Notion).
4. **Track progress** with the checklist below.

## Progress checklist

- [ ] Phase 0: environment set up, Python basics, Bandit levels 0–10
- [ ] Phase 1: 3Blue1Brown linear algebra + calculus; MML book ch. 2, 5, 6
- [ ] Phase 2: MNIST classifier; fine-tuned model; local RAG chatbot
- [ ] Phase 3: PortSwigger SSRF + auth + access-control labs; OWASP Top 10
- [ ] Phase 4: Labs 1–8 complete; read OWASP LLM Top 10 + MITRE ATLAS
- [ ] Phase 5: 10 papers read; 1 CTF played; 3 blog posts published

## Careers this leads to

AI red teamer · ML security engineer · AI security researcher · LLM application security / AppSec
· Trust & safety engineer. Helpful certifications later (optional): CompTIA Security+,
PortSwigger BSCP, and AI-security certs such as OffSec's or SANS's AI-focused courses.
