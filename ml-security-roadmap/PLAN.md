# My plan: job hunting, 3 hours a day, goal = job + money + curiosity

This replaces the generic timeline in README.md. The README phases are still the *content*;
this file is the *order and the schedule* for my situation.

## The honest truth this plan is built on

- "ML security engineer" is a **destination, not an entry-level job**. Few companies hire a
  beginner directly into it.
- So the plan runs **two tracks at once**:
  1. **Income track:** skills and jobs that can pay in weeks to months.
  2. **Core track:** the path to AI security, which also makes me stand out for income-track jobs.
- Math is learned **just in time**, not up front. LLM application security needs very little of it.
- 3 h/day × 6 days = **18 h/week**. With focus, I can be job-ready for entry security roles
  in **~4–6 months** and have a real AI security portfolio by **~6–9 months**.

## Daily structure (3 hours)

| Block | Time | What |
|---|---|---|
| 1. Learn | 60 min | Course or lesson for the current month (below) |
| 2. Do | 75 min | Labs, Bandit, coding, projects: hands on keyboard |
| 3. Money & visibility | 45 min | Job applications, CV/LinkedIn, gig platforms, one public post a week |

Day 7: rest, or a light review of the week's notes.

## Month-by-month

### Month 1: Foundations + start earning options
- [ ] Linux: Bandit levels 0–15
- [ ] Python: py4e chapters 1–10 + small scripts pushed to GitHub
- [ ] Git: daily commits (notes + code); a clean GitHub profile with a README about me
- [ ] Gandalf (gandalf.lakera.ai): all levels. This is my "do I enjoy this?" test
- [ ] **Money:** sign up for AI training / evaluation platforms that pay for writing and
      red-teaming AI responses (check that they're available in my country, and **never pay to join**;
      paying to join is a scam signal)
- [ ] **Money:** CV updated with "Python, Linux, Git, AI security (learning)"; LinkedIn headline set
- [ ] Start a "learning ML security from zero" weekly post (LinkedIn and/or X)

### Month 2: Security fundamentals + first certificate
- [ ] TryHackMe: Pre Security → start "SOC Level 1" or "Jr Penetration Tester"
- [ ] PortSwigger Academy: SSRF, authentication, access control (Apprentice labs)
- [ ] **Certificate (cheap/free first):** ISC2 *Certified in Cybersecurity (CC)* (check whether the
      free training + exam offer is still running) or Google Cybersecurity Certificate (Coursera, apply for financial aid)
- [ ] **Money:** apply to 5–10 entry roles a week: SOC analyst L1, IT/security support,
      junior Python/automation dev, AI data/evaluation roles

### Month 3: LLMs + first AI security skills
- [ ] Karpathy "Zero to Hero" first 2 videos OR Hugging Face LLM course ch. 1–3 (understand how LLMs work)
- [ ] Ollama on Windows + small model (llama3.2:1b/3b); connect from the VM
- [ ] PortSwigger "Web LLM attacks" labs (all)
- [ ] Read OWASP Top 10 for LLM Applications + MITRE ATLAS overview
- [ ] DeepLearning.AI "Red Teaming LLM Applications" (free short course)
- [ ] **Money:** enter a paid jailbreak/red-teaming competition (HackAPrompt, Gray Swan Arena, etc.)

### Month 4: Portfolio project #1 (the thing that gets interviews)
- [ ] Build a small RAG chatbot (Ollama + Chroma)
- [ ] Attack it: prompt injection, indirect injection via documents, RAG poisoning, data leakage
- [ ] Scan it with **garak** and **promptfoo redteam**
- [ ] Add defences, re-test, measure the difference
- [ ] **Publish a writeup** (GitHub README + blog/LinkedIn post): "I built an AI chatbot and hacked it"
- [ ] **Money:** start applying to junior AppSec / AI security / pentest roles with this project on the CV

### Month 5: Classic ML attacks + tools
- [ ] Lab 01 exercises (PGD, adversarial training) + same attacks with IBM ART
- [ ] Math just in time: 3Blue1Brown linear algebra + calculus (now it will make sense)
- [ ] PyRIT: automate a multi-turn attack on my own model
- [ ] Portfolio project #2: data poisoning / backdoor on a small model + writeup

### Month 6+: Earn from the skill
- [ ] AI bug bounties: huntr (AI/ML open-source libraries), HackerOne/Bugcrowd AI programs, **in scope only**
- [ ] Offer LLM security testing to small businesses with chatbots, **with written permission only**
- [ ] CTFs: Crucible (Dreadnode), AI Village CTF
- [ ] Keep applying; keep posting writeups

## Jobs I can realistically target (closest first)

1. AI trainer / evaluator / red-teaming contractor (gig work): possible in month 1–2
2. IT support / helpdesk with security duties
3. SOC analyst (Level 1)
4. Junior Python / AI automation developer
5. Junior pentester / AppSec
6. **AI security / ML security engineer**: the destination

## Weekly check-in (every Sunday, 15 min)
- What did I finish? What did I skip and why?
- How many applications did I send?
- What did I post publicly?
- What's the one thing to fix next week?
