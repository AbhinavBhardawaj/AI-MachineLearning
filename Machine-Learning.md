# ML/AI Learning Roadmap — Week by Week

*Paced for curiosity-driven learning, not job deadlines. Treat weeks as "chunks of effort," not a strict calendar — slide them around freely. Check things off as you go.*

---

## Phase 1: Math Refresh (Weeks 1–2)
Goal: build geometric intuition, not memorize formulas.

- [x] Week 1: 3Blue1Brown — *Essence of Linear Algebra* (all episodes). After each video, pause and ask "what would this look like in numpy?"
- [ ] Week 2: 3Blue1Brown — *Essence of Calculus* (all episodes). Focus especially on derivatives, chain rule, and the intro to gradients.
- [ ] Only if something still feels foreign: dip into the Cartoon/Manga guide for that specific topic (e.g. just the derivatives chapter).

**Checkpoint:** Can you explain what a dot product and a gradient *mean*, without formulas, to a friend?

---

## Phase 2: ML Intuition (Weeks 3–5)
Goal: understand *why* each algorithm exists and what problem it solves.

- [ ] Week 3: StatQuest — Linear Regression → Logistic Regression → Cross Validation / Bias-Variance tradeoff
- [ ] Week 4: StatQuest — Decision Trees → Random Forest → Gradient Boosting / XGBoost
- [ ] Week 5: StatQuest — PCA → intro Neural Network videos
- [ ] Alongside all of this: keep Starmer's book open as a reference — reread a section anytime a video moves too fast.

**Checkpoint:** Could you sketch, from memory, how a decision tree decides where to split?

---

## Phase 3: Hands-On Coding (Weeks 3–6, run in parallel with Phase 2)
Goal: turn intuition into working code.

- [ ] Sentdex — "ML from scratch in Python" style playlists: implement KNN, linear regression, and a simple decision tree using plain Python/numpy (not just sklearn calls)
- [ ] Once comfortable, redo 2–3 of those same algorithms using scikit-learn, and compare your scratch version's output to sklearn's
- [ ] Pick one small dataset (Titanic, Iris, or something you're curious about) and run it through your own regression + a tree model end to end

**Checkpoint:** Can you write logistic regression from scratch with just numpy, no sklearn?

---

## Phase 4: Theoretical Depth — CS229 (Weeks 7–10)
Goal: formalize what StatQuest made intuitive.

- [ ] Week 7: Linear regression, gradient descent, normal equations — derive them on paper
- [ ] Week 8: Logistic regression, generalized linear models
- [ ] Week 9: SVMs, kernels
- [ ] Week 10: Unsupervised learning (k-means, EM, PCA formalized), learning theory basics
- [ ] Use lecture notes as primary material; use lectures for anything notes don't clarify

**Checkpoint:** Can you derive the gradient descent update rule for linear regression from scratch on paper?

---

## Phase 5: Deep Learning Foundations (Weeks 11–15)
Goal: understand backprop, training dynamics, and CNNs.

- [ ] Week 11: 3Blue1Brown's Neural Network series (rewatch if you saw it earlier — it'll hit differently now)
- [ ] Weeks 12–13: CS231n — backpropagation, optimization, training dynamics lectures (treat as mandatory)
- [ ] Weeks 14–15: CS231n — CNN architectures, and vision-specific content (treat as optional/interest-based — skim if vision itself isn't your focus)

**Checkpoint:** Can you explain backpropagation as "the chain rule applied through a computation graph," and trace it through a 2-layer network by hand?

---

## Phase 6: Build From Scratch — Karpathy (Weeks 16–20)
Goal: the payoff phase — build real things with your own hands.

- [ ] Week 16–17: *micrograd* — build a tiny autograd engine
- [ ] Week 18: *makemore* — character-level language models, several iterations
- [ ] Week 19–20: Build a GPT from scratch (the "Let's build GPT" video/series)

**Checkpoint:** You now understand transformers well enough to read the "Attention Is All You Need" paper without feeling lost.

---

## Ongoing Throughout (start immediately, never really "finish")
- [ ] Colah's blog and Jay Alammar's "Illustrated ___" posts — read whichever one matches whatever topic you're currently stuck on
- [ ] After Phase 6: read foundational papers — AlexNet, ResNet, *Attention Is All You Need*, GPT-2/3, BERT
- [ ] Save Krish Naik for whenever you want to see full project pipelines or deployment — not needed until you're building something end-to-end for others to use

---

### Notes on flexibility
- If a checkpoint feels shaky, don't move on — repeat the phase's resources or find a blog post that explains it differently. Speed doesn't matter here.
- Phases 2 and 3 are deliberately parallel — alternate between them week to week so intuition and code-writing reinforce each other.
- It's fine to jump ahead and watch a Karpathy video early out of curiosity — just don't skip the derivation work in Phases 1, 2, and 4. That's where real understanding gets built.
