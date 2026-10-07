# AI-Powered Adaptive UEBA for Insider Threat Detection
## Research-Paper Judge Cross-Question Bank (430 Master Defense Q&A)

**Academic Degree:** M.Tech in Computer Science and Engineering  
**Student Name:** Mr. Chetan Shrikant Lokhande (PRN: 25PCS009)  
**Guide Name:** Prof. S. R. Patil (PG Recognition No: SU/PGBUTR/RECOG/761368)  
**Institution:** D.K.T.E. Society's Textile and Engineering Institute, Ichalkaranji (Affiliated to Shivaji University, Kolhapur)  
**Dataset:** Carnegie Mellon University (CMU) CERT Insider Threat Dataset r5.2  
**Document Workspace:** `D:\Chetan Sir\cyberProject\PDF\`

---

## MASTER TABLE OF CATEGORIES

1. [Category A — Fundamental Research-Defense Questions (Q1–Q20)](#category-a--fundamental-research-defense-questions)
2. [Category B — Architecture and Overall Design (Q21–Q40)](#category-b--architecture-and-overall-design)
3. [Category C — Why CERT r5.2? (Q41–Q55)](#category-c--why-cert-r52)
4. [Category D — Data Preprocessing (Q56–Q70)](#category-d--data-preprocessing)
5. [Category E — Feature Engineering (Q71–Q90)](#category-e--feature-engineering)
6. [Category F — Feature Engineering — Difficult Judge Questions (Q91–Q100)](#category-f--feature-engineering--difficult-judge-questions)
7. [Category G — SVM — Why and Why Not? (Q101–Q112)](#category-g--svm--why-and-why-not)
8. [Category H — XGBoost — Very Likely Judge Questions (Q113–Q132)](#category-h--xgboost--very-likely-judge-questions)
9. [Category I — Isolation Forest (Q133–Q142)](#category-i--isolation-forest)
10. [Category J — SMOTE — Important Cross Questions (Q143–Q157)](#category-j--smote--important-cross-questions)
11. [Category K — Adaptive Baseline — Core Research Defense (Q158–Q185)](#category-k--adaptive-baseline--core-research-defense)
12. [Category L — Baseline Governance — Very Difficult Questions (Q186–Q200)](#category-l--baseline-governance--very-difficult-questions)
13. [Category M — Risk Fusion (Q201–Q220)](#category-m--risk-fusion)
14. [Category N — SHAP / Explainability (Q221–Q242)](#category-n--shap--explainability)
15. [Category O — LLM / Explainable Alert System (Q243–Q260)](#category-o--llm--explainable-alert-system)
16. [Category P — Django / Backend Technology Choices (Q261–Q270)](#category-p--django--backend-technology-choices)
17. [Category Q — PostgreSQL / Database (Q271–Q280)](#category-q--postgresql--database)
18. [Category R — Redis / Celery (Q281–Q297)](#category-r--redis--celery)
19. [Category S — Frontend / Dashboard (Q298–Q308)](#category-s--frontend--dashboard)
20. [Category T — Evaluation (Q309–Q325)](#category-t--evaluation)
21. [Category U — Results — Questions Judges Can Attack (Q326–Q342)](#category-u--results--questions-judges-can-attack)
22. [Category V — Research Contribution / Novelty (Q343–Q352)](#category-v--research-contribution--novelty)
23. [Category W — Alternatives — Judge's Favorite Questions (Q353–Q362)](#category-w--alternatives--judges-favorite-questions)
24. [Category X — Drawbacks / Limitations (Q363–Q378)](#category-x--drawbacks--limitations)
25. [Category Y — Security Questions (Q379–Q390)](#category-y--security-questions)
26. [Category Z — Extremely Difficult Judge Questions (Q391–Q430)](#category-z--extremely-difficult-judge-questions)
27. [Master Mapping — 15 Core Decision Clusters Summary](#master-mapping--15-core-decision-clusters-summary)

---

## Category A — Fundamental Research-Defense Questions

#### Q1: What is the exact research problem you are trying to solve?
* **Answer:** We address the vulnerability of adaptive User and Entity Behavior Analytics (UEBA) systems to **slow-escalation baseline poisoning**. When an insider gradually increases anomalous activity (e.g., +5% per month), ungoverned adaptive models absorb the malicious trajectory as normal, causing detection rates to collapse from 94% down to 22% by Month 6.
* **Why Examiner Asks This:** To verify if you have a clear, focused research problem rather than a generic engineering project.
* **Key Point:** Slow-escalation poisoning collapses unguarded adaptive baselines.

#### Q2: Why is this problem important in cybersecurity?
* **Answer:** Malicious insiders already possess valid credentials and authorized access. Perimeter tools (firewalls, IDS) cannot block them. If an adaptive UEBA baseline is poisoned by slow escalation, exfiltration occurs with zero alert generation, exposing corporate IP to catastrophic loss.
* **Why Examiner Asks This:** Testing domain motivation.
* **Key Point:** Credentialed insiders bypass perimeter security; baseline poisoning neutralizes UEBA.

#### Q3: Why did you choose UEBA instead of a traditional intrusion detection system?
* **Answer:** Traditional IDS rely on static malware signatures or IP blocklists. Insiders exfiltrate data using standard enterprise tools (USB, email, browser). UEBA monitors longitudinal behavioral patterns to flag structural deviations rather than static signatures.
* **Why Examiner Asks This:** Testing understanding of security paradigms.
* **Key Point:** Behavioral anomalies vs static signatures.

#### Q4: What is the difference between UEBA and conventional anomaly detection?
* **Answer:** Conventional anomaly detection flags any instantaneous statistical outlier (generating high false alarms). UEBA incorporates user entity baselines, organizational peer groups, role-normalized contexts, and longitudinal trajectory tracking to reduce false positives.
* **Why Examiner Asks This:** Testing technical depth in security analytics.
* **Key Point:** Contextual peer & individual historical baselines vs global point anomalies.

#### Q5: What exactly makes your UEBA system adaptive?
* **Answer:** It maintains rolling 30-day user baseline vectors ($\mathbf{B}_u$) and role/department peer centroids ($\mathbf{C}_{R,D}$) that update over time as new weekly telemetry arrives, incorporating benign operational changes without manual reset.
* **Why Examiner Asks This:** Validating the definition of "adaptive".
* **Key Point:** Rolling 30-day historical window + peer centroid updates.

#### Q6: What is the main weakness of a static behavioral baseline?
* **Answer:** Static baselines trigger persistent false alarms whenever an employee legitimately changes projects, gets promoted, or increases workload, causing severe SOC alert fatigue.
* **Why Examiner Asks This:** Contrast reasoning.
* **Key Point:** Alert fatigue from benign operational shifts.

#### Q7: What happens when legitimate user behavior changes over time?
* **Answer:** Under legitimate changes (e.g., role promotion), the user's vector shifts *along with their peer group centroid*, keeping peer divergence low. Our governance engine detects this and ALLOWS the baseline to update.
* **Why Examiner Asks This:** Verifying handling of concept drift.
* **Key Point:** Legitimate drift tracks peer group centroids.

#### Q8: What happens when malicious behavior changes slowly over time?
* **Answer:** An attacker increases exfiltration by small deltas. In an ungoverned system, the baseline shifts upward in lockstep. In our governed system, the update triggers Stage 2 peer divergence and Stage 3 7-day monotonic trend checks, freezing the baseline.
* **Why Examiner Asks This:** Attack mechanics check.
* **Key Point:** Unilateral escalation triggers peer divergence and trend checks.

#### Q9: What is slow-escalation poisoning?
* **Answer:** An adversarial strategy where an insider increments anomalous activity at sub-threshold rates ($\alpha \approx 0.05$/month) to deliberately habituate an adaptive ML model into normalizing exfiltration.
* **Why Examiner Asks This:** Threat model definition.
* **Key Point:** $\alpha$-slow escalation habituates online learning algorithms.

#### Q10: Why is slow-escalation poisoning more difficult to detect than sudden anomalous behavior?
* **Answer:** Sudden anomalies create sharp distance spikes ($D_{\text{user}} \gg 0$) that trigger immediate alert thresholds. Slow escalation keeps daily deltas below point thresholds while manipulating the historical reference mean.
* **Why Examiner Asks This:** Comparative anomaly physics.
* **Key Point:** Sub-threshold daily deltas vs large point spikes.

#### Q11: What is the difference between behavioral drift and malicious behavior?
* **Answer:** Behavioral drift is directional variance over time. It is benign if aligned with organizational peer shifts, and malicious if executed unilaterally with persistent monotonic acceleration.
* **Why Examiner Asks This:** Core conceptual distinction.
* **Key Point:** Peer-aligned drift = benign; unilateral monotonic drift = malicious.

#### Q12: How does your system distinguish legitimate drift from malicious drift?
* **Answer:** Through Stage 2 of our governance engine: comparing individual user deviation $D_{\text{user}}$ against role/department peer centroid distance $D_{\text{peer}}$. Legitimate drift exhibits low peer divergence ($\Delta_{\text{peer}} < 0.45$), whereas malicious drift exhibits high unilateral divergence.
* **Why Examiner Asks This:** Validating Experiment E4 (94% accuracy, 4% FSR).
* **Key Point:** Peer-anchor divergence check ($\Delta_{\text{peer}}$).

#### Q13: What is the central research hypothesis of your work?
* **Answer:** A 4-stage baseline governance engine using peer-group anchors can prevent slow-escalation baseline poisoning and sustain high detection rates ($\ge 90\%$) on CMU CERT r5.2 without increasing false baseline suppression on legitimate role changes.
* **Why Examiner Asks This:** Scientific methodology check.
* **Key Point:** Governed baselines sustain detection without blocking legitimate shifts.

#### Q14: What is your primary research contribution?
* **Answer:** The **Contamination-Resistant 4-Stage Baseline Update Governance Engine** (Algorithm 1 in Paper 1) and its empirical validation showing a sustained 93% detection rate under 6-month poisoning campaigns.
* **Why Examiner Asks This:** Disambiguating core novelty from engineering.
* **Key Point:** 4-Stage Baseline Update Governance Engine.

#### Q15: What part of your project is engineering and what part is research?
* **Answer:**  
  * **Research:** Threat formalization of $\alpha$-slow escalation, the 4-stage governance math ($S_1, S_2, S_3, S_{\text{drift}}$), multi-model risk fusion formulation, TreeSHAP evidence bounding, and FaithLens LLM audit.  
  * **Engineering:** Data cleaning pipeline, Celery/Redis queue architecture, Django REST APIs, and React 18 dashboard.
* **Why Examiner Asks This:** Evaluating academic scope.
* **Key Point:** Governance math & risk fusion = research; full-stack code = engineering.

#### Q16: Why is this more than simply applying XGBoost to the CERT dataset?
* **Answer:** Standalone XGBoost is a static classifier that cannot handle temporal baseline drift or slow poisoning. Our work builds a complete governed adaptive pipeline, multi-model risk fusion, exact TreeSHAP attribution, and zero-hallucination LLM reporting.
* **Why Examiner Asks This:** Defending against "trivial ML application" claims.
* **Key Point:** Static XGBoost fails under baseline poisoning; governance solves the security gap.

#### Q17: What is actually novel in your approach?
* **Answer:** It is the first work on the CMU CERT dataset to formally model, defend, and experimentally validate against slow-escalation baseline poisoning using peer-anchored update gating.
* **Why Examiner Asks This:** Novelty audit.
* **Key Point:** Peer-anchored 4-stage update gating against slow-rate poisoning.

#### Q18: How is your approach different from existing adaptive UEBA approaches?
* **Answer:** Existing models (BRITD, MambaITD, Evidential Clustering) update baselines or thresholds continuously based on incoming statistical density, leaving them vulnerable to steering. Our system decouples raw score computation from baseline updates using a 4-stage governance gate.
* **Why Examiner Asks This:** Literature positioning.
* **Key Point:** Decoupled governance gate vs un-gated continuous learning.

#### Q19: What specific research gap did you identify?
* **Answer:** No peer-reviewed UEBA literature on CMU CERT r5.2 defends against slow-escalation baseline poisoning, and LLM security tools have not been grounded on user behavioral SHAP attributions.
* **Why Examiner Asks This:** Literature gap validation.
* **Key Point:** Lack of baseline poisoning defense in UEBA literature.

#### Q20: How does your proposed system address that research gap?
* **Answer:** By implementing a 4-stage governance gate ($S_1$ drift acceleration, $S_2$ peer divergence, $S_3$ 7-day monotonic trend, $S_4$ composite gating) and combining TreeSHAP payloads with evidence-constrained Claude 3.5 Sonnet synthesis.
* **Why Examiner Asks This:** Connecting gap to solution.
* **Key Point:** 4-stage gate + SHAP-grounded LLM evidence objects.

---

## Category B — Architecture and Overall Design

#### Q21: Explain the complete architecture of your system from raw data to final alert.
* **Answer:** Raw CERT CSVs $\to$ Data Cleaning & UTC Normalization $\to$ 44 Daily User Feature Matrix $\to$ Chronological 80/20 Split $\to$ Multi-Model Scoring (SMOTE XGBoost, SVM, Isolation Forest) $\to$ 4-Stage Baseline Governance Gate $\to$ Multi-Model Risk Fusion ($0$--$100$ score) $\to$ TreeSHAP Top-5 Attributions $\to$ JSON Evidence Builder $\to$ Celery/Redis Async Task $\to$ Claude 3.5 Sonnet Explanation $\to$ React 18 SOC Dashboard.
* **Why Examiner Asks This:** Architecture comprehension test.
* **Key Point:** 4-layer end-to-end dataflow.

```
Raw CSVs -> Feature Extraction (44D) -> Multi-Model Scoring -> Governance Gate -> Risk Fusion -> TreeSHAP -> Claude LLM -> React Dashboard
```

#### Q22: Why did you separate data processing, ML detection, baseline governance, risk fusion, and explanation?
* **Answer:** Separation of concerns. Decoupling allows independent model tuning, prevents expensive LLM inference from blocking REST APIs, and ensures baseline updates are audited independently of raw classifier output.
* **Why Examiner Asks This:** Software engineering design principles.
* **Key Point:** Modularity, non-blocking execution, and independent auditability.

#### Q23: Why did you choose a modular architecture?
* **Answer:** To support research experimentation. Modules (`feature_engineer.py`, `governance.py`, `risk_fusion.py`, `shap_explainer.py`) can be swapped or modified independently without breaking the Django/React web stack.
* **Why Examiner Asks This:** Maintainability & research flexibility.
* **Key Point:** Independent module evaluation and clean refactoring.

#### Q24: Why did you not use a microservices architecture?
* **Answer:** Microservices introduce network serialization overhead, distributed tracing complexity, and deployment friction unnecessary for a research prototype. A modular monolith provides clean code boundaries with simple deployment.
* **Why Examiner Asks This:** Architectural trade-off justification.
* **Key Point:** Avoids unnecessary network latency and operational complexity.

#### Q25: Why is a pure monolithic architecture unsuitable for this project?
* **Answer:** A single tight monolith executing long-running ML matrix operations or 5-second LLM API calls on the main HTTP thread would freeze user UI requests.
* **Why Examiner Asks This:** Concurrency & scalability understanding.
* **Key Point:** Synchronous HTTP thread blocking during heavy ML/LLM workloads.

#### Q26: Why is modular monolith + separate ML pipeline appropriate?
* **Answer:** It combines logical code modularity in Django/React with asynchronous background execution via Celery workers for heavy ML and LLM tasks.
* **Why Examiner Asks This:** Defending current hybrid choice.
* **Key Point:** Clean Django ORM domain models + background task queues.

#### Q27: What are the major modules in your system?
* **Answer:**  
  1. Data Ingestion & Cleaning (`cert_ingestor.py`, `cleaner.py`).  
  2. Feature Engineering & Splitting (`feature_engineer.py`, `splitter.py`).  
  3. Hybrid ML Engine (`xgboost_model.py`, `svm_model.py`, `isolation_forest.py`).  
  4. Baseline Governance Engine (`governance.py`).  
  5. Risk Fusion Engine (`risk_fusion.py`).  
  6. SHAP & LLM Evidence Pipeline (`shap_explainer.py`, `evidence_builder.py`, `llm_client.py`).  
  7. Django REST Backend & React 18 Frontend.
* **Why Examiner Asks This:** Codebase taxonomy check.
* **Key Point:** 7 core functional modules.

#### Q28: Which module is responsible for the actual security decision?
* **Answer:** The **Risk Fusion Engine** (`risk_fusion.py`), which computes the composite 0–100 $RiskScore$ and assigns severity tiers (Critical, High, Medium, Low).
* **Why Examiner Asks This:** Identifying decision authority.
* **Key Point:** Risk Fusion Engine computes final score and severity.

#### Q29: Which module is responsible only for explanation?
* **Answer:** The **LLM Explanation Module** (`llm_client.py` & `apps/explanations/tasks.py`), which synthesizes structured JSON evidence into plain-English analyst summaries.
* **Why Examiner Asks This:** Testing LLM isolation.
* **Key Point:** Claude LLM is strictly an explanation generator.

#### Q30: Can the LLM modify the final security risk score?
* **Answer:** **NO.** The LLM has zero authority over risk scores or alerts. It operates post-hoc, receiving immutable JSON evidence payloads.
* **Why Examiner Asks This:** Safety & guardrail check.
* **Key Point:** Complete firewall between decision engine and LLM.

#### Q31: Why should the LLM not make the final security decision?
* **Answer:** Generative LLMs are non-deterministic, vulnerable to prompt manipulation, and lack mathematical guarantees. Security decisions require deterministic, auditable ML risk models.
* **Why Examiner Asks This:** AI ethics & safety reasoning.
* **Key Point:** Non-determinism and lack of formal safety guarantees in LLMs.

#### Q32: What happens if the LLM is unavailable?
* **Answer:** The system uses a deterministic evidence-grounded template fallback (`build_fallback_explanation()`). All alerts, risk scores, and SHAP visualizers continue functioning normally.
* **Why Examiner Asks This:** Resilience & fault-tolerance check.
* **Key Point:** Fallback template ensures 100% operational uptime.

#### Q33: What happens if the ML model is unavailable?
* **Answer:** Serialized joblib binaries are loaded at Django startup. If a model file is missing, the system logs an initialization error; fallback rules evaluate baseline distance $D_{\text{user}}$ and peer deviation $D_{\text{peer}}$.
* **Why Examiner Asks This:** Error handling audit.
* **Key Point:** Joblib binary pre-loading and baseline distance fallback.

#### Q34: What happens if the baseline governance layer is unavailable?
* **Answer:** Baseline updates freeze in quarantine by default ($V = \text{SUPPRESS}$), preventing un-gated profile contamination until the governance worker recovers.
* **Why Examiner Asks This:** Fail-safe design strategy.
* **Key Point:** Fail-secure default: baseline updates freeze upon governance failure.

#### Q35: Which component is the source of truth for the final risk?
* **Answer:** The PostgreSQL database tables (`alerts_alert` and `risk_scores`), populated directly by `risk_fusion.py`.
* **Why Examiner Asks This:** System state authority check.
* **Key Point:** Database records populated by Risk Fusion Engine.

#### Q36: Where does the adaptive baseline sit in your architecture?
* **Answer:** In the **Intelligence Layer** (`ml/baseline/baseline_engine.py` and `governance.py`), positioned between raw feature extraction and risk fusion.
* **Why Examiner Asks This:** Architectural positioning.
* **Key Point:** Intercepts daily vectors before risk score computation.

#### Q37: Why is adaptation performed at the baseline layer rather than by continuously retraining the ML model?
* **Answer:** Baseline vectors ($\mathbf{B}_u$) represent per-user historical means ($44$ values), which can be updated cleanly in $\mathcal{O}(d)$ time. Retraining XGBoost continuously on streaming data is computationally expensive and risks global catastrophic forgetting.
* **Why Examiner Asks This:** Efficiency & machine learning mechanics.
* **Key Point:** Lightweight $\mathcal{O}(d)$ vector updates vs heavy model retraining.

#### Q38: What are the advantages of your architecture over an end-to-end neural network?
* **Answer:** Interpretability, modular auditing, computational efficiency, and resistance to adversarial noise. End-to-end deep networks operate as opaque black boxes and are easily fooled by subtle perturbations.
* **Why Examiner Asks This:** Comparing classical/hybrid vs deep learning.
* **Key Point:** Interpretability, exact TreeSHAP attributions, and modular governance.

#### Q39: What is the main bottleneck in your architecture?
* **Answer:** External LLM API network latency (3–10 seconds per incident explanation call).
* **Why Examiner Asks This:** Performance bottleneck identification.
* **Key Point:** LLM network round-trip time (mitigated by Celery/Redis).

#### Q40: Which component is computationally expensive?
* **Answer:** Generating the 44-feature daily matrix across 692,645 vectors during raw CSV parsing, and computing exact Shapley values via TreeSHAP across 44 continuous dimensions.
* **Why Examiner Asks This:** Resource management check.
* **Key Point:** Multi-GB log aggregation and TreeSHAP matrix calculations.

---

## Category C — Why CERT r5.2?

#### Q41: Why did you select the CERT Insider Threat Dataset?
* **Answer:** Carnegie Mellon University's CERT dataset is the universally recognized academic benchmark for insider threat research, providing comprehensive multi-channel audit logs with ground-truth malicious labels.
* **Why Examiner Asks This:** Dataset choice justification.
* **Key Point:** Standard academic benchmark with ground-truth insider labels.

#### Q42: Why specifically CERT r5.2?
* **Answer:** Version 5.2 is the most comprehensive release, containing 1,000 synthetic users over 18 months and covering all 6 major insider threat scenarios, including slow-escalation data staging.
* **Why Examiner Asks This:** Version specificity.
* **Key Point:** 1,000 users, 18 months, 6 threat scenarios including slow staging.

#### Q43: What alternatives to CERT did you consider?
* **Answer:** TWOS (Two Weeks Office Scenario) dataset and SANSHIT. However, TWOS covers only 2 weeks of activity (insufficient for 6-month baseline poisoning research), and SANSHIT lacks multi-modality.
* **Why Examiner Asks This:** Literature comparison.
* **Key Point:** TWOS is too short (2 weeks); CERT r5.2 spans 18 months.

#### Q44: Why did you not use a real enterprise dataset?
* **Answer:** Real enterprise logs contain sensitive PII, trade secrets, and strict NDA restrictions. Furthermore, real enterprise logs almost never have ground-truth insider labels.
* **Why Examiner Asks This:** Practical constraint recognition.
* **Key Point:** PII restrictions, NDAs, and absence of clean ground-truth labels in enterprise logs.

#### Q45: What are the major limitations of the CERT dataset?
* **Answer:** It is synthetically generated; user activity follows structured probabilistic models, lacking real-world human noise, organizational restructuring chaos, and complex network edge cases.
* **Why Examiner Asks This:** Critical thinking & limitation awareness.
* **Key Point:** Synthetic background noise and structured probabilistic patterns.

#### Q46: How representative is CERT of real enterprise behavior?
* **Answer:** Highly representative in structure (logons, USB, email, file, HTTP, LDAP org charts), but cleaner than real networks where unannounced software updates create log artifacts.
* **Why Examiner Asks This:** External validity assessment.
* **Key Point:** Structurally representative but statistically cleaner than real networks.

#### Q47: Can results obtained on CERT be generalized to real organizations?
* **Answer:** The mathematical principles (4-stage governance, peer divergence, risk fusion, TreeSHAP) generalize directly. However, real-world deployment requires tuning suspicion threshold $\tau$ to local background noise.
* **Why Examiner Asks This:** Generalizability audit.
* **Key Point:** Mathematical framework generalizes; thresholds require local tuning.

#### Q48: Does CERT contain enough behavioral diversity?
* **Answer:** Yes. It models 1,000 employees across distinct job roles (software engineers, HR specialists, sales reps, IT admins) and departments.
* **Why Examiner Asks This:** Sample diversity check.
* **Key Point:** 1,000 users across diverse LDAP roles and departments.

#### Q49: Does CERT adequately represent modern insider threats?
* **Answer:** It captures classic exfiltration vectors (USB, webmail, cloud storage, after-hours access). Modern cloud-native vectors (e.g., SaaS API tokens) require additional feature parsers.
* **Why Examiner Asks This:** Threat landscape currency.
* **Key Point:** Excellent coverage of core exfiltration channels; SaaS APIs represent future scope.

#### Q50: What biases can exist in the CERT dataset?
* **Answer:** Synthetic generation bias: malicious scenarios follow predefined injection templates, causing threat vectors to exhibit sharp multi-modal spikes.
* **Why Examiner Asks This:** Dataset bias identification.
* **Key Point:** Predefined synthetic injection templates.

#### Q51: How would your system behave on a completely different dataset?
* **Answer:** Provided the data is parsed into daily user feature vectors, the hybrid fusion and 4-stage governance engine operate identically without architectural modification.
* **Why Examiner Asks This:** Pipeline flexibility check.
* **Key Point:** Agnostic intelligence layer given standard feature schema.

#### Q52: How would you validate your system using another dataset?
* **Answer:** By ingesting enterprise SIEM logs (e.g., Splunk or Elastic CSV exports), mapping them to our 44 feature schema, and evaluating detection rate under simulated 5%/month poisoning.
* **Why Examiner Asks This:** Future validation strategy.
* **Key Point:** SIEM log schema mapping + poisoning simulation.

#### Q53: Why not combine multiple insider-threat datasets?
* **Answer:** Different datasets (e.g., CERT vs TWOS) have incompatible feature schemas, tracking granularities, and observation windows, making direct matrix merging methodologically invalid.
* **Why Examiner Asks This:** Data merging validity.
* **Key Point:** Incompatible schema definitions and time scales.

#### Q54: What would happen if the dataset distribution changes?
* **Answer:** Our peer-anchor governance engine accommodates legitimate distribution shifts if they occur across peer cohorts, while isolating unilateral anomalies.
* **Why Examiner Asks This:** Concept drift resilience.
* **Key Point:** Peer-anchored adaptation absorbs cohort-wide distribution shifts.

#### Q55: What happens if the real-world class imbalance is much higher than CERT?
* **Answer:** In real enterprises, threats may be 0.01% rather than 1–2%. SMOTE oversampling ratio can be increased, and the risk fusion decision boundary can be adjusted using precision-recall curves.
* **Why Examiner Asks This:** Extreme class imbalance handling.
* **Key Point:** Dynamic SMOTE ratio adjustment + PR-AUC threshold tuning.

---

## Category D — Data Preprocessing

#### Q56: Why is preprocessing necessary for your project?
* **Answer:** Raw CERT CSV logs contain multi-gigabyte unformatted strings, irregular timestamps, duplicate entries, and missing fields that cannot be consumed directly by machine learning algorithms.
* **Why Examiner Asks This:** Pipeline fundamentals.
* **Key Point:** Converts raw unstructured logs into structured numerical matrices.

#### Q57: Why can't you directly feed raw logs into XGBoost?
* **Answer:** XGBoost requires structured, continuous numerical feature matrices ($\mathbf{X} \in \mathbb{R}^{n \times d}$). Raw logs contain variable-length text strings, timestamps, and missing relational records.
* **Why Examiner Asks This:** ML input requirements.
* **Key Point:** Matrix format requirement ($\mathbb{R}^{n \times d}$).

#### Q58: How did you handle timestamps?
* **Answer:** In `cleaner.py`, all ISO string timestamps across all 6 log modalities were parsed and converted to standardized UTC Unix timestamps.
* **Why Examiner Asks This:** Time synchronization check.
* **Key Point:** Parsed ISO strings $\to$ UTC Unix timestamps.

#### Q59: Why is chronological ordering important?
* **Answer:** User behavior is a sequential time-series. Processing data out of order corrupts rolling baseline calculations and introduces temporal leakage.
* **Why Examiner Asks This:** Time-series integrity.
* **Key Point:** Preserves rolling baseline chronology and prevents temporal leakage.

#### Q60: Why did you use time-aware processing?
* **Answer:** To compute accurate temporal features (e.g., after-hours logons between 18:00–08:00, weekend activities, 7-day rolling trend windows).
* **Why Examiner Asks This:** Feature calculation logic.
* **Key Point:** Enables after-hours, weekend, and rolling window feature extraction.

#### Q61: Why is random train-test splitting dangerous in behavioral security data?
* **Answer:** Random splitting places future activities of a user into the training set and past activities into the test set, creating catastrophic temporal data leakage and artificially inflated accuracy scores.
* **Why Examiner Asks This:** Methodological validity check.
* **Key Point:** Future data bleeds into training set, causing fake 99%+ metrics.

#### Q62: What is temporal leakage?
* **Answer:** An experimental flaw where information from the future (e.g., post-attack user statistics or future baseline states) is inadvertently exposed to the model during training.
* **Why Examiner Asks This:** Data leakage definition.
* **Key Point:** Future telemetry contaminating historical model training.

#### Q63: Give an example of data leakage in your project.
* **Answer:** If user $u$'s activity on Day 100 is included in the training set while Day 50 is in the test set, the model "knows" user $u$'s future exfiltration patterns when evaluating Day 50.
* **Why Examiner Asks This:** Concrete example check.
* **Key Point:** Future day 100 features revealing day 50 test labels.

#### Q64: How did you prevent future behavioral information from entering the training data?
* **Answer:** By implementing `splitter.py` to enforce a strict chronological split: the first 80% of calendar days (562,594 records) were used for training, and the remaining 20% (130,051 records) were held out for testing.
* **Why Examiner Asks This:** Verification of defense against leakage.
* **Key Point:** Chronological 80/20 train/test split.

#### Q65: How did you handle duplicate events?
* **Answer:** In `cleaner.py`, exact duplicate tuples $(\text{date}, \text{user}, \text{pc}, \text{activity})$ across audit logs were identified and purged.
* **Why Examiner Asks This:** Data hygiene check.
* **Key Point:** Exact tuple deduplication.

#### Q66: How did you handle missing values?
* **Answer:** Missing categorical attributes (e.g., unrecorded email attachments) were imputed with `'N/A'`; missing numerical activity counts were zero-filled; missing psychometric scores were filled with cohort means.
* **Why Examiner Asks This:** Imputation strategy audit.
* **Key Point:** Contextual imputation: `'N/A'` for text, $0.0$ for counts, mean for psychometrics.

#### Q67: Why shouldn't all missing values simply be replaced with zero?
* **Answer:** Replacing missing psychometric OCEAN scores or user roles with $0$ distorts distance calculations in vector space. Zero should only represent zero activity count.
* **Why Examiner Asks This:** Nuanced data preprocessing awareness.
* **Key Point:** Zero distorts continuous baseline vectors; context matters.

#### Q68: What does a missing value actually mean in behavioral data?
* **Answer:** It can mean either "event did not occur" (e.g., zero USB connects), "data not captured by sensor", or "attribute not applicable" (e.g., email without attachment).
* **Why Examiner Asks This:** Domain semantics understanding.
* **Key Point:** Non-occurrence vs sensor error vs non-applicable field.

#### Q69: How do you distinguish "no activity" from "missing data"?
* **Answer:** "No activity" generates an explicit daily feature row with feature values $= 0$. "Missing data" represents a null value within an existing log record.
* **Why Examiner Asks This:** Matrix construction mechanics.
* **Key Point:** Feature value $0$ in daily vector vs null in raw log tuple.

#### Q70: What happens if a feature is missing at runtime?
* **Answer:** The Django API pipeline uses `feature_engineer.py` default fallbacks, filling missing runtime elements with $0.0$ or the user's historical rolling mean.
* **Why Examiner Asks This:** System robustness check.
* **Key Point:** Runtime fallback to $0.0$ or historical user mean.

---

## Category E — Feature Engineering

#### Q71: Why did you create a daily user-feature matrix?
* **Answer:** Daily aggregation captures human work rhythms (business hours vs after-hours) while compressing raw event streams into uniform 44-dimensional feature vectors ($\mathbf{x}_{u,t} \in \mathbb{R}^{44}$).
* **Why Examiner Asks This:** Aggregation granularity choice.
* **Key Point:** Matches human circadian work rhythms and standardizes input matrices.

#### Q72: Why did you choose daily aggregation instead of hourly aggregation?
* **Answer:** Hourly aggregation produces extremely sparse matrices (most hours have zero activity) and increases vector storage 24-fold without improving longitudinal baseline tracking.
* **Why Examiner Asks This:** Granularity trade-off reasoning.
* **Key Point:** High sparsity and $24\times$ memory overhead in hourly models.

#### Q73: What are the disadvantages of daily aggregation?
* **Answer:** Intraday temporal resolution is lost. A burst of 100 file copies in 5 minutes looks identical to 100 file copies spread across 8 hours.
* **Why Examiner Asks This:** Trade-off awareness.
* **Key Point:** Loss of fine-grained intraday burst timing.

#### Q74: What information can be lost through daily aggregation?
* **Answer:** Exact sub-hour sequence order (e.g., whether USB insertion occurred 1 minute *before* or *after* file copy).
* **Why Examiner Asks This:** Fine-grained information loss check.
* **Key Point:** Sub-hour causal event sequence order.

#### Q75: Why not use raw event-level features?
* **Answer:** Raw event-level features vary in length per user per day, preventing fixed-dimension tabular classification required by XGBoost and SVM.
* **Why Examiner Asks This:** Tabular vector space requirements.
* **Key Point:** Variable-length sequences vs fixed $d=44$ vector space.

#### Q76: Why did you create behavioral features?
* **Answer:** Behavioral features (e.g., USB transfer ratios, external email ratios) reflect operational intent rather than noisy raw counts.
* **Why Examiner Asks This:** Domain feature design philosophy.
* **Key Point:** Ratios capture behavioral intent better than raw volume counts.

#### Q77: Why are temporal features important for insider-threat detection?
* **Answer:** Malicious insiders frequently stage or exfiltrate data after business hours (18:00–08:00) or on weekends to avoid physical detection by co-workers.
* **Why Examiner Asks This:** Security domain intuition.
* **Key Point:** After-hours and weekend activities correlate strongly with stealth exfiltration.

#### Q78: Why are peer-group features useful?
* **Answer:** They establish normative expectations for specific job roles. A software engineer downloading source code is normal; an HR specialist doing so is highly anomalous.
* **Why Examiner Asks This:** Peer group utility check.
* **Key Point:** Role-normalized behavioral expectations.

#### Q79: What is a peer group in your system?
* **Answer:** A cohort of employees sharing identical LDAP `role` and `department` strings (e.g., `Role: Systems Admin`, `Dept: IT Ops`).
* **Why Examiner Asks This:** System definition check.
* **Key Point:** Matching LDAP `role` + `department` attributes.

#### Q80: How do you determine that two users are peers?
* **Answer:** By exact string matching on organizational metadata during baseline initialization in `baseline_engine.py`.
* **Why Examiner Asks This:** Clustering mechanics check.
* **Key Point:** String matching on LDAP role and department attributes.

#### Q81: What happens if a user belongs to multiple roles?
* **Answer:** In our current implementation, the primary LDAP role string is used. Multi-role assignment maps to the broader departmental centroid.
* **Why Examiner Asks This:** Edge case handling.
* **Key Point:** Primary LDAP role string fallback to department centroid.

#### Q82: How do you handle users whose behavior is unique and does not have a strong peer group?
* **Answer:** If a role cohort has $<3$ users, Stage 2 governance falls back to the broader departmental centroid $\mathbf{C}_D$.
* **Why Examiner Asks This:** Peer group sparsity edge case.
* **Key Point:** Fallback to departmental centroid $\mathbf{C}_D$.

#### Q83: Why did you select 40+ features?
* **Answer:** To cover all 6 audit modalities (Auth, USB, Email, File, HTTP, Baselines) comprehensively without leaving unmonitored blind spots.
* **Why Examiner Asks This:** Feature dimension scope.
* **Key Point:** Multimodal coverage across 6 audit channels.

#### Q84: How did you determine whether a feature was useful?
* **Answer:** Through TreeSHAP global feature importance ranking (`shap.summary_plot`) on the validation split.
* **Why Examiner Asks This:** Feature evaluation methodology.
* **Key Point:** TreeSHAP global feature importance validation.

#### Q85: Did you perform feature selection?
* **Answer:** Yes. Initial exploratory analysis engineered 58 candidate features; 14 collinear or zero-variance features were pruned, leaving 44 active features.
* **Why Examiner Asks This:** Feature reduction rigor.
* **Key Point:** Pruned collinear/zero-variance features from 58 down to 44.

#### Q86: Could some of your features be redundant?
* **Answer:** Some features are intentionally complementary (e.g., `usb_file_copy_count` and `usb_file_copy_bytes`), capturing both frequency and payload scale.
* **Why Examiner Asks This:** Collinearity check.
* **Key Point:** Complementary frequency vs payload size indicators.

#### Q87: How do correlated features affect XGBoost?
* **Answer:** Decision tree ensembles handle correlated features gracefully by splitting across redundant nodes, though SHAP splits attribution between correlated pairs.
* **Why Examiner Asks This:** Model interactions with collinearity.
* **Key Point:** Tree splits manage collinearity; SHAP distributes feature attribution.

#### Q88: How can an attacker manipulate behavioral features?
* **Answer:** By throttling exfiltration (e.g., copying 2 files per day instead of 1,000) or executing staging during business hours.
* **Why Examiner Asks This:** Adversarial manipulation awareness.
* **Key Point:** Throttling exfiltration rates to stay below point thresholds.

#### Q89: Can an attacker deliberately behave normally to avoid detection?
* **Answer:** Yes, while staging data. But actual exfiltration ultimately requires abnormal resource transfer (USB copy, external email, web upload) that diverges from peers.
* **Why Examiner Asks This:** Attack limits check.
* **Key Point:** Exfiltration ultimately forces behavioral divergence.

#### Q90: What happens if an attacker slowly changes multiple features together?
* **Answer:** Coordinated multi-feature slow escalation causes cumulative peer divergence $D_{\text{peer}}$ to accumulate faster, triggering Stage 2 governance earlier.
* **Why Examiner Asks This:** Multi-feature attack mechanics.
* **Key Point:** Multi-feature drift accelerates peer divergence $D_{\text{peer}}$.

---

## Category F — Feature Engineering — Difficult Judge Questions

#### Q91: Why did you use feature X instead of feature Y? (e.g., external email ratio vs raw external email count)
* **Answer:** Raw counts scale with total email volume (a busy workday inflates counts). Ratios normalize for total activity, isolating true behavioral anomaly proportions.
* **Why Examiner Asks This:** Specific feature design rationale.
* **Key Point:** Ratios normalize for total activity volume.

#### Q92: Which feature contributes most to detection?
* **Answer:** As shown in TreeSHAP global evaluations, `usb_file_copy_bytes`, `after_hours_logons`, `external_email_ratio`, and `D_peer` are the top 4 threat predictors.
* **Why Examiner Asks This:** Empirical feature ranking check.
* **Key Point:** `usb_file_copy_bytes`, `after_hours_logons`, `external_email_ratio`, `D_peer`.

#### Q93: How do you know that a feature is causally related to malicious behavior?
* **Answer:** Features map directly to established MITRE ATT&CK for Enterprise exfiltration techniques (T1052: Exfiltration Over Physical Media, T1048: Exfiltration Over Alternative Protocol).
* **Why Examiner Asks This:** Domain causality grounding.
* **Key Point:** Grounded in MITRE ATT&CK exfiltration tactics.

#### Q94: Are your features domain-driven or purely data-driven?
* **Answer:** Domain-driven. Features were designed based on cybersecurity threat modeling of insider exfiltration vectors rather than brute-force mathematical transformations.
* **Why Examiner Asks This:** Feature engineering methodology.
* **Key Point:** Domain-driven threat modeling.

#### Q95: How would your feature engineering change for another organization?
* **Answer:** The core 44 features remain identical for standard enterprise environments; specialized organizations (e.g., healthcare) would add HIPAA file access flags.
* **Why Examiner Asks This:** Cross-domain adaptability.
* **Key Point:** Core 44 features are standard; domain-specific compliance flags can be appended.

#### Q96: Are your features transferable across organizations?
* **Answer:** Yes. Ratios and baseline deviations ($D_{\text{peer}}, D_{\text{user}}$) are scale-invariant, making them transferable across different organizational scales.
* **Why Examiner Asks This:** Feature transferability.
* **Key Point:** Ratios and normalized distances are scale-invariant.

#### Q97: What happens when the organization's user roles change?
* **Answer:** LDAP role updates trigger recalculation of peer centroids $\mathbf{C}_{R,D}$ in `baseline_engine.py`, re-anchoring the user to their new role cohort.
* **Why Examiner Asks This:** Dynamic organizational change handling.
* **Key Point:** LDAP updates trigger peer centroid recalculation.

#### Q98: What happens when a new employee has no historical behavior?
* **Answer:** The system assigns a cold-start baseline initialized directly to their role peer centroid $\mathbf{C}_{R,D}$ for the first 30 days.
* **Why Examiner Asks This:** Cold-start problem handling.
* **Key Point:** Initialized to role peer centroid $\mathbf{C}_{R,D}$.

#### Q99: How do you create a baseline for a new user?
* **Answer:** Using cold-start initialization: $\mathbf{B}_{\text{new}}^{(0)} = \mathbf{C}_{R,D}$. As clean days accumulate, individual data replaces the centroid weight.
* **Why Examiner Asks This:** Cold-start mechanics.
* **Key Point:** $\mathbf{B}_{\text{new}}^{(0)} = \mathbf{C}_{R,D}$ transitioning to individual rolling mean.

#### Q100: How do you handle users with very little historical data?
* **Answer:** By weighting deviation calculation heavily toward peer distance ($D_{\text{peer}}$) until $W \ge 14$ days of individual telemetry are logged.
* **Why Examiner Asks This:** Low-data user handling.
* **Key Point:** Peer distance weighting during initial 14-day window.

---

## Category G — SVM — Why and Why Not?

#### Q101: Why did you select SVM as a baseline model?
* **Answer:** Support Vector Machines with RBF kernels represent the standard classical baseline in academic UEBA literature (Alzaabi et al., 2024), providing a benchmark reference.
* **Why Examiner Asks This:** Baseline model choice.
* **Key Point:** Established literature benchmark for supervised classification.

#### Q102: Why is SVM appropriate as a baseline for this problem?
* **Answer:** SVM maximizes the margin between classes in high-dimensional feature spaces ($d=44$), offering strong mathematical bounds on small datasets.
* **Why Examiner Asks This:** SVM suitability.
* **Key Point:** Maximum margin separation in high-dimensional space.

#### Q103: Why not use Logistic Regression as the baseline?
* **Answer:** Logistic Regression assumes linear decision boundaries, failing to capture complex non-linear feature interactions present in behavioral logs.
* **Why Examiner Asks This:** Linear vs non-linear baseline choice.
* **Key Point:** Logistic Regression cannot capture non-linear behavioral boundaries.

#### Q104: Why not use Random Forest as the baseline?
* **Answer:** Random Forest is an ensemble method similar to XGBoost; SVM provides a distinct, non-tree kernel-based baseline architecture.
* **Why Examiner Asks This:** Model diversity in baselines.
* **Key Point:** Provides architectural diversity (kernel-based vs tree-based).

#### Q105: Why not use KNN?
* **Answer:** K-Nearest Neighbors requires storing all training instances and performing $\mathcal{O}(N \cdot d)$ distance comparisons at inference time, creating severe latency bottlenecks.
* **Why Examiner Asks This:** KNN computational inefficiency.
* **Key Point:** High inference latency $\mathcal{O}(N \cdot d)$.

#### Q106: Why not use a neural network?
* **Answer:** Neural networks require massive labeled datasets, extensive hyperparameter tuning, and lack local mathematical explainability tools like TreeSHAP.
* **Why Examiner Asks This:** Deep learning vs classical trade-offs.
* **Key Point:** Label scarcity, opacity, and lack of TreeSHAP compatibility.

#### Q107: What kernel did you use for SVM?
* **Answer:** Radial Basis Function (RBF) kernel: $K(\mathbf{x}, \mathbf{x}') = \exp(-\gamma \|\mathbf{x} - \mathbf{x}'\|^2)$.
* **Why Examiner Asks This:** Technical parameter check.
* **Key Point:** RBF (Gaussian) kernel.

#### Q108: Why did you choose that kernel?
* **Answer:** RBF maps features into infinite-dimensional Hilbert space, enabling smooth non-linear decision boundaries for complex behavioral telemetry.
* **Why Examiner Asks This:** Kernel theory check.
* **Key Point:** Non-linear decision boundary mapping.

#### Q109: What are the major disadvantages of SVM?
* **Answer:** Quadratic training time complexity $\mathcal{O}(N^2)$, sensitivity to feature scaling, and opacity of support vector coefficients.
* **Why Examiner Asks This:** Model limitation awareness.
* **Key Point:** $\mathcal{O}(N^2)$ scaling and feature scale sensitivity.

#### Q110: How does SVM behave with high-dimensional features?
* **Answer:** SVM handles high dimensions well due to margin maximization, provided features are standardized using `StandardScaler`.
* **Why Examiner Asks This:** High-dimensional stability.
* **Key Point:** Effective with standardized inputs due to structural risk minimization.

#### Q111: How does class imbalance affect SVM?
* **Answer:** Unbalanced data pushes the hyper-plane toward the minority class, causing high false negative rates. We applied class weighting (`class_weight='balanced'`).
* **Why Examiner Asks This:** Imbalance handling in SVM.
* **Key Point:** Balanced class weighting adjusts hyper-plane penalty parameters.

#### Q112: What happens if the number of users/events becomes very large?
* **Answer:** Full SVM training on 562,594 records crashes due to memory limits. We fitted SVM on a stratified sample of 50,000 records, converging on 2,072 support vectors.
* **Why Examiner Asks This:** Scalability defense (resolves memory bottleneck).
* **Key Point:** Stratified 50k sampling preserves rare threats while capping matrix memory.

---

## Category H — XGBoost — Very Likely Judge Questions

#### Q113: Why did you choose XGBoost as the primary supervised classifier?
* **Answer:** XGBoost (eXtreme Gradient Boosting) is state-of-the-art for continuous tabular data, handling non-linear interactions, missing values, and high class imbalance effectively.
* **Why Examiner Asks This:** Primary classifier justification.
* **Key Point:** State-of-the-art performance on continuous tabular telemetry.

#### Q114: Why XGBoost instead of Random Forest?
* **Answer:** Gradient boosting builds trees sequentially to minimize residual loss, achieving higher precision and recall than independent parallel trees in Random Forest.
* **Why Examiner Asks This:** XGBoost vs RF comparison.
* **Key Point:** Sequential residual error minimization vs independent bagging.

#### Q115: Why XGBoost instead of LightGBM?
* **Answer:** XGBoost provides exact greedy tree split algorithms and native exact TreeSHAP integration, which is highly optimized for forensic explainability.
* **Why Examiner Asks This:** Gradient boosting framework comparison.
* **Key Point:** Native, exact TreeSHAP integration and exact split optimization.

#### Q116: Why XGBoost instead of CatBoost?
* **Answer:** CatBoost excels at target encoding for high-cardinality categorical features. Our feature matrix consists entirely of continuous numerical ratios and counts ($d=44$).
* **Why Examiner Asks This:** Framework suitability check.
* **Key Point:** Our matrix is 100% continuous numerical features; CatBoost target encoding is unneeded.

#### Q117: Why XGBoost instead of a deep neural network?
* **Answer:** Empirical studies consistently demonstrate that gradient boosted decision trees outperform deep learning on tabular datasets of under 1 million rows.
* **Why Examiner Asks This:** GBDT vs Deep Learning benchmark literature.
* **Key Point:** GBDTs consistently outperform neural nets on tabular data.

#### Q118: What advantage does XGBoost provide for tabular behavioral data?
* **Answer:** Invariance to monotonic feature transformations, robustness to outliers, and exact split points across non-linear decision boundaries.
* **Why Examiner Asks This:** Tabular suitability details.
* **Key Point:** Monotonic transformation invariance and exact non-linear splitting.

#### Q119: How does XGBoost handle nonlinear relationships?
* **Answer:** By partitioning feature space into orthogonal decision regions using deep decision trees (max depth $= 4$).
* **Why Examiner Asks This:** Non-linear decision mechanics.
* **Key Point:** Hierarchical space partitioning via decision trees.

#### Q120: Why is XGBoost suitable for heterogeneous behavioral features?
* **Answer:** Behavioral features mix counts, ratios, session hours, and scores. Tree-based splits evaluate features independently without requiring identical normalization scales.
* **Why Examiner Asks This:** Scale independence check.
* **Key Point:** Scale-invariant feature evaluation.

#### Q121: What are the disadvantages of XGBoost?
* **Answer:** Susceptibility to overfitting on noisy minority samples if depth is unconstrained, and black-box opacity without post-hoc SHAP tools.
* **Why Examiner Asks This:** Model limitation awareness.
* **Key Point:** Overfitting risk if unconstrained; requires SHAP for explainability.

#### Q122: Can XGBoost overfit?
* **Answer:** Yes, particularly when trained on SMOTE-oversampled minority data if tree depth or learning rate is too high.
* **Why Examiner Asks This:** Overfitting risk check.
* **Key Point:** SMOTE synthetic noise can induce overfitting if unconstrained.

#### Q123: How did you control overfitting?
* **Answer:** By restricting `max_depth=4`, setting `learning_rate=0.05`, `subsample=0.8`, `colsample_bytree=0.8`, and using early stopping on validation loss.
* **Why Examiner Asks This:** Regularization parameters check.
* **Key Point:** `max_depth=4`, low learning rate ($0.05$), subsampling ($0.8$).

#### Q124: Which XGBoost hyperparameters are important?
* **Answer:** `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `scale_pos_weight`, and regularization parameters `reg_alpha` and `reg_lambda`.
* **Why Examiner Asks This:** Hyperparameter taxonomy.
* **Key Point:** Depth, learning rate, subsample, and L1/L2 regularization.

#### Q125: What is the role of learning rate?
* **Answer:** It scales the contribution of each new tree added to the ensemble ($\eta = 0.05$), preventing individual trees from dominating the loss gradient.
* **Why Examiner Asks This:** Learning rate mechanics.
* **Key Point:** Shrinkage parameter scaling tree contributions.

#### Q126: What is the role of tree depth?
* **Answer:** `max_depth=4` limits feature interaction complexity, preventing the model from memorizing noisy individual training instances.
* **Why Examiner Asks This:** Tree depth mechanics.
* **Key Point:** Limits interaction order to 4th-degree polynomials.

#### Q127: What is the role of number of estimators?
* **Answer:** `n_estimators=100` specifies total sequential boosting rounds. Early stopping halts training when validation loss stops improving.
* **Why Examiner Asks This:** Boosting iterations check.
* **Key Point:** Specifies total sequential boosting stages.

#### Q128: What is the role of subsampling?
* **Answer:** `subsample=0.8` randomly samples 80% of training rows per tree, introducing stochastic bagging variance reduction.
* **Why Examiner Asks This:** Stochastic boosting mechanics.
* **Key Point:** Row subsampling introduces stochastic variance reduction.

#### Q129: How did you select the hyperparameters?
* **Answer:** Via grid search (`GridSearchCV`) evaluated on the chronological validation split using PR-AUC as the primary tuning objective.
* **Why Examiner Asks This:** Tuning methodology.
* **Key Point:** Grid search tuned on validation PR-AUC.

#### Q130: Did you use cross-validation?
* **Answer:** We used time-aware rolling window validation rather than standard random k-fold cross-validation.
* **Why Examiner Asks This:** Validation protocol check.
* **Key Point:** Time-aware rolling window validation.

#### Q131: If you use chronological data, why might ordinary k-fold cross-validation be problematic?
* **Answer:** Standard k-fold shuffles data randomly, using future test folds to predict past training folds, breaking temporal causality.
* **Why Examiner Asks This:** Time-series validation pitfalls.
* **Key Point:** Random k-fold violates temporal causality.

#### Q132: How would you perform time-aware validation?
* **Answer:** Using expanding window backtesting: train on Month 1–6 to test Month 7; train on Month 1–7 to test Month 8.
* **Why Examiner Asks This:** Expanding window mechanics.
* **Key Point:** Expanding historical window backtesting.

---

## Category I — Isolation Forest

#### Q133: Why did you include Isolation Forest?
* **Answer:** To provide an unsupervised global anomaly score ($S_{\text{IF}}$) that detects zero-day outlier activity without requiring ground-truth training labels.
* **Why Examiner Asks This:** Unsupervised model justification.
* **Key Point:** Zero-day anomaly detection without ground-truth labels.

#### Q134: What does Isolation Forest provide that XGBoost does not?
* **Answer:** Unsupervised outlier detection. XGBoost only recognizes patterns similar to labeled training threats; Isolation Forest flags structural outliers in feature space.
* **Why Examiner Asks This:** Complementary model dynamics.
* **Key Point:** Supervised pattern matching vs unsupervised outlier isolation.

#### Q135: Why use both supervised and unsupervised detection?
* **Answer:** Hybrid security posture. Supervised XGBoost catches known insider exfiltration signatures; unsupervised Isolation Forest catches novel zero-day attacks.
* **Why Examiner Asks This:** Hybrid architecture defense.
* **Key Point:** Dual-defense posture: known threat signatures + zero-day outliers.

#### Q136: What happens when an attack pattern is not present in the training labels?
* **Answer:** Supervised XGBoost outputs low probability ($P_{\text{xgb}} \approx 0$), but Isolation Forest detects high feature space isolation ($S_{\text{IF}} \approx 0.85$), elevating the fused risk score.
* **Why Examiner Asks This:** Zero-day attack mechanics.
* **Key Point:** Isolation Forest rescues zero-day threat detection.

#### Q137: Can Isolation Forest detect previously unseen behavior?
* **Answer:** Yes. It partitions feature space randomly; instances requiring few splits (short path length) are flagged as anomalies regardless of prior labeling.
* **Why Examiner Asks This:** Tree partitioning mechanics.
* **Key Point:** Short average path length in isolation trees = anomaly.

#### Q138: What are the limitations of Isolation Forest?
* **Answer:** High false positive rates when benign users legitimately spike interaction volumes, and inability to distinguish positive anomalies from negative anomalies without baseline context.
* **Why Examiner Asks This:** Unsupervised limitations.
* **Key Point:** High false positive rates on benign spikes; lacks contextual baseline awareness.

#### Q139: Why not use One-Class SVM?
* **Answer:** One-Class SVM has $\mathcal{O}(N^2)$ computational complexity and is sensitive to kernel scale parameters on high-dimensional data ($d=44$).
* **Why Examiner Asks This:** Alternative unsupervised algorithm check.
* **Key Point:** Quadratic time complexity and hyper-plane scale sensitivity.

#### Q140: Why not use Autoencoders for anomaly detection?
* **Answer:** Deep autoencoders require heavy GPU training, lack exact local SHAP explainability guarantees, and continuously reconstruct inputs without governance gating.
* **Why Examiner Asks This:** Autoencoder trade-offs.
* **Key Point:** Heavy training overhead and black-box reconstruction opacity.

#### Q141: Why not use Local Outlier Factor?
* **Answer:** Local Outlier Factor (LOF) has $\mathcal{O}(N^2)$ distance computation complexity and cannot score new unseen streaming samples without refitting.
* **Why Examiner Asks This:** LOF algorithm limitations.
* **Key Point:** $\mathcal{O}(N^2)$ complexity and inability to score streaming samples.

#### Q142: How do you combine Isolation Forest output with the supervised model output?
* **Answer:** Through our mathematical risk fusion formula: normalizing path lengths to $S_{\text{IF}} \in [0, 1]$ and assigning it a $0.25$ weight in composite $RiskScore$.
* **Why Examiner Asks This:** Fusion integration mechanics.
* **Key Point:** Normalized score $S_{\text{IF}}$ weighted at 25% in fusion equation.

---

## Category J — SMOTE — Important Cross Questions

#### Q143: Why did you use SMOTE?
* **Answer:** Insider threats represent roughly 1–2% of records in CMU CERT r5.2. SMOTE oversamples minority threat instances to prevent decision tree bias toward majority benign classes.
* **Why Examiner Asks This:** Class imbalance mitigation strategy.
* **Key Point:** Balances severe 1–2% minority class representation.

#### Q144: Why is class imbalance a problem for insider-threat detection?
* **Answer:** Naive classifiers trained on 99% benign data achieve 99% accuracy simply by predicting "benign" for every instance, missing 100% of actual insider attacks.
* **Why Examiner Asks This:** Class imbalance dilemma intuition.
* **Key Point:** Naive majority voting yields 99% accuracy but 0% threat detection.

#### Q145: Why is accuracy misleading under class imbalance?
* **Answer:** In a dataset with 99 benign records and 1 threat record, an algorithm guessing "benign" achieves 99% accuracy despite complete operational failure.
* **Why Examiner Asks This:** Metric evaluation validity.
* **Key Point:** Accuracy reflects majority class dominance, masking total recall failure.

#### Q146: How does SMOTE work?
* **Answer:** Synthetic Minority Over-sampling Technique selects a minority instance, finds its $k$-nearest minority neighbors, and synthesizes new samples along feature-space line segments.
* **Why Examiner Asks This:** SMOTE mathematical mechanics.
* **Key Point:** Linear interpolation between minority instances and their $k$-NNs.

#### Q147: Does SMOTE simply duplicate minority samples?
* **Answer:** **No.** Random oversampling duplicates samples; SMOTE generates entirely new, synthetic vectors along feature-space line segments ($x_{\text{new}} = x_i + \lambda(x_{zi} - x_i)$).
* **Why Examiner Asks This:** SMOTE vs Random Oversampling distinction.
* **Key Point:** Synthetic feature interpolation vs exact sample duplication.

#### Q148: Can SMOTE create unrealistic synthetic users?
* **Answer:** If $k$-neighbors span distinct attack scenarios, SMOTE can interpolate between different threat types. Parameterizing $k=5$ on homogeneous scenario subsets mitigates this artifact.
* **Why Examiner Asks This:** SMOTE synthetic risk awareness.
* **Key Point:** Convex interpolation between distinct scenario clusters.

#### Q149: What are the risks of applying SMOTE to behavioral data?
* **Answer:** Generating synthetic samples inside benign feature regions if minority clusters overlap with majority class boundaries.
* **Why Examiner Asks This:** Feature-space overlap risks.
* **Key Point:** Synthetic generation in overlapping boundary regions.

#### Q150: Why should SMOTE be applied only to the training data?
* **Answer:** Applying SMOTE to test data alters the natural real-world class distribution, invalidating operational evaluation metrics.
* **Why Examiner Asks This:** Experimental integrity audit.
* **Key Point:** Test set must reflect natural real-world class distributions.

#### Q151: What happens if SMOTE is applied before train-test splitting?
* **Answer:** Synthetic samples generated between train and test instances cause severe data leakage, yielding artificially inflated test performance.
* **Why Examiner Asks This:** Data leakage via SMOTE check.
* **Key Point:** Severe data leakage via synthetic sample interpolation.

#### Q152: Can SMOTE introduce data leakage?
* **Answer:** Yes, if applied before splitting. By applying SMOTE strictly to the 562,594 training split after chronological partitioning, zero leakage occurs.
* **Why Examiner Asks This:** Methodological compliance check.
* **Key Point:** Strictly applied post-split to training partition only.

#### Q153: What alternatives to SMOTE exist?
* **Answer:** ADASYN, Random Oversampling, Tomek Links, Focal Loss, and algorithmic class weighting (`scale_pos_weight` in XGBoost).
* **Why Examiner Asks This:** Alternative imbalance technique check.
* **Key Point:** ADASYN, Tomek Links, scale_pos_weight, Focal Loss.

#### Q154: Why did you choose SMOTE instead of class weighting?
* **Answer:** Empirical grid search showed SMOTE achieved higher decision boundary resolution (F1 0.9412) compared to pure `scale_pos_weight` (F1 0.9015).
* **Why Examiner Asks This:** Comparative empirical justification.
* **Key Point:** Higher empirical F1-score on validation split.

#### Q155: Why not use ADASYN?
* **Answer:** ADASYN focuses synthetic generation on difficult boundary samples, which in noisy behavioral data synthesizes samples from outlier noise.
* **Why Examiner Asks This:** Advanced oversampling comparison.
* **Key Point:** ADASYN over-emphasizes noisy boundary outliers.

#### Q156: Why not use random oversampling?
* **Answer:** Random oversampling leads to exact sample duplication, causing decision trees to overfit heavily on specific repeated feature points.
* **Why Examiner Asks This:** Overfitting risk in duplication.
* **Key Point:** Exact duplication induces decision tree memorization.

#### Q157: How would you determine whether SMOTE actually improved the model?
* **Answer:** By running an ablation experiment comparing XGBoost trained *with* SMOTE vs XGBoost trained *without* SMOTE on PR-AUC metrics.
* **Why Examiner Asks This:** Ablation experiment methodology.
* **Key Point:** PR-AUC ablation comparison.

---

## Category K — Adaptive Baseline — Core Research Defense

#### Q158: What exactly is a behavioral baseline?
* **Answer:** A mathematical reference vector $\mathbf{B}_u \in \mathbb{R}^{44}$ representing user $u$'s historical mean activity values over a rolling observation window.
* **Why Examiner Asks This:** Baseline definition.
* **Key Point:** Vector of historical mean activity values ($\mathbf{B}_u$).

#### Q159: Why do you need an adaptive baseline?
* **Answer:** Because enterprise employee roles evolve. Static baselines fire false alerts when benign work volume increases, causing severe SOC triage fatigue.
* **Why Examiner Asks This:** Adaptive baseline necessity.
* **Key Point:** Accommodates benign operational concept drift.

#### Q160: Why not use a static baseline?
* **Answer:** Static baselines cannot adjust to legitimate departmental transfers, project launches, or seasonal workload spikes.
* **Why Examiner Asks This:** Static baseline limitations.
* **Key Point:** Brittle operational failure during legitimate role changes.

#### Q161: How is your baseline initially constructed?
* **Answer:** Formed from a 30-day historical window of clean daily vectors: $\mathbf{B}_u = \frac{1}{W} \sum_{k=1}^{W} \mathbf{x}_u^{(k)}$.
* **Why Examiner Asks This:** Initial baseline math.
* **Key Point:** Sliding-window mean over initial validated period.

#### Q162: Why did you select a 30-day historical baseline?
* **Answer:** 30 days covers monthly corporate reporting cycles and monthly work rhythms while remaining responsive to operational shifts.
* **Why Examiner Asks This:** Parameter choice justification ($W=30$).
* **Key Point:** Aligns with monthly enterprise operational cycles.

#### Q163: Why not 7 days?
* **Answer:** 7 days is too volatile; a single busy workweek or temporary deadline would corrupt the baseline representation.
* **Why Examiner Asks This:** Short window comparison.
* **Key Point:** High volatility and sensitivity to temporary workload spikes.

#### Q164: Why not 90 days?
* **Answer:** 90 days introduces high inertia, taking over three months for the system to adapt to a legitimate job promotion.
* **Why Examiner Asks This:** Long window comparison.
* **Key Point:** High inertia delays adaptation to legitimate role transfers.

#### Q165: What happens if user behavior changes within those 30 days?
* **Answer:** Candidate weekly vectors are evaluated by the 4-stage governance engine before being incorporated into the 30-day rolling window.
* **Why Examiner Asks This:** Window update mechanics.
* **Key Point:** Evaluated by 4-stage governance before window inclusion.

#### Q166: What happens if the baseline itself contains malicious behavior?
* **Answer:** That is baseline poisoning. If un-gated, the baseline absorbs the malicious trajectory, resulting in false negatives.
* **Why Examiner Asks This:** Poisoning definition check.
* **Key Point:** Baseline absorbs threat trajectory, causing false negatives.

#### Q167: How can a baseline become poisoned?
* **Answer:** Through $\alpha$-slow escalation, where an attacker increments exfiltration by small sub-threshold deltas (+5%/month) over multiple months.
* **Why Examiner Asks This:** Poisoning mechanism check.
* **Key Point:** Sub-threshold incremental shifts over extended timeframes.

#### Q168: Why is slow poisoning dangerous?
* **Answer:** It trains the detection model to treat exfiltration as normal behavior, completely blinding SOC analysts when mass exfiltration occurs.
* **Why Examiner Asks This:** Threat severity awareness.
* **Key Point:** Habituation blinds the system to eventual mass exfiltration.

#### Q169: How does your governance mechanism detect potential poisoning?
* **Answer:** By evaluating candidate updates against 4 sequential checks: drift rate acceleration ($S_1$), peer-anchor divergence ($S_2$), and 7-day monotonic trends ($S_3$).
* **Why Examiner Asks This:** Governance mechanism summary.
* **Key Point:** 4-stage evaluation gate ($S_1, S_2, S_3, S_{\text{drift}}$).

#### Q170: What is drift rate in your system?
* **Answer:** The mean rate of change of user deviation across historical evaluation checkpoints: $\bar{r} = \frac{1}{m-1} \sum \Delta d_i$.
* **Why Examiner Asks This:** Stage 1 mathematical definition.
* **Key Point:** Mean acceleration of historical deviation differentials.

#### Q171: Why is drift rate useful?
* **Answer:** Slow-escalation attacks exhibit positive acceleration in cumulative deviation over time, whereas benign fluctuations show zero-mean variance.
* **Why Examiner Asks This:** Stage 1 utility rationale.
* **Key Point:** Detects positive acceleration indicative of systematic escalation.

#### Q172: What is peer divergence?
* **Answer:** The positive distance difference between candidate user deviation $D_{\text{user}}$ and distance to their role/department peer centroid $D_{\text{peer}}$ ($\Delta_{\text{peer}} = \max(0, D_{\text{user}} - D_{\text{peer}})$).
* **Why Examiner Asks This:** Stage 2 mathematical definition.
* **Key Point:** Unilateral separation from role/department peer cohort.

#### Q173: Why compare an individual user against a peer group?
* **Answer:** Attackers poison their individual profile unilaterally. Unless an entire department coordinates an attack, the adversary diverges from peer norms.
* **Why Examiner Asks This:** Peer anchor intuition.
* **Key Point:** Adversaries poison profiles unilaterally, diverging from cohorts.

#### Q174: Why use both individual baseline and peer baseline?
* **Answer:** Individual baselines capture personalized work habits; peer baselines provide an un-poisonable organizational anchor during drift evaluation.
* **Why Examiner Asks This:** Dual-baseline necessity.
* **Key Point:** Individual baseline = personal habits; Peer baseline = un-poisonable anchor.

#### Q175: What happens if the whole department changes behavior?
* **Answer:** Peer centroid $\mathbf{C}_{R,D}$ shifts along with the cohort, keeping $\Delta_{\text{peer}}$ low and allowing candidate baseline updates ($V = \text{ALLOW}$).
* **Why Examiner Asks This:** Department-wide organizational shift edge case.
* **Key Point:** Cohort-wide movement keeps peer divergence low.

#### Q176: Would your peer-based approach incorrectly classify organizational change as malicious?
* **Answer:** **No.** Experiment E4 demonstrated a 4.00% False Suppression Rate because organizational changes shift peer centroids in tandem.
* **Why Examiner Asks This:** Validating Experiment E4 results.
* **Key Point:** 4.00% FSR; peer centroids shift in tandem during org changes.

#### Q177: How do you distinguish organizational drift from an individual anomaly?
* **Answer:** Organizational drift exhibits low peer divergence ($\Delta_{\text{peer}} \approx 0$). Individual anomalies exhibit high unilateral divergence ($\Delta_{\text{peer}} > 0.40$).
* **Why Examiner Asks This:** Disambiguation logic.
* **Key Point:** Low $\Delta_{\text{peer}}$ = org drift; High $\Delta_{\text{peer}}$ = individual anomaly.

#### Q178: What is the role of the 7-day trend?
* **Answer:** Stage 3 checks directional monotonicity: evaluating whether risk score step differentials $\delta_j \ge 0$ across a 7-day window.
* **Why Examiner Asks This:** Stage 3 trend role.
* **Key Point:** Evaluates directional monotonicity over rolling 7 days.

#### Q179: Why did you select a 7-day trend?
* **Answer:** A 7-day window captures a full weekly work cycle, filtering out single-day stochastic spikes while catching sustained weekly escalations.
* **Why Examiner Asks This:** Parameter choice justification ($K=7$).
* **Key Point:** Matches weekly work cycles while filtering single-day spikes.

#### Q180: Why not use a 14-day or 30-day trend?
* **Answer:** A 14-day or 30-day trend window delays alert suppression by two to four weeks, allowing partial exfiltration before gating triggers.
* **Why Examiner Asks This:** Longer trend window trade-off.
* **Key Point:** Longer trend windows delay alert suppression response time.

#### Q181: Why is monotonic behavior relevant to slow-escalation attacks?
* **Answer:** Adversarial slow escalation requires persistent upward step increases to stage exfiltration; benign activity fluctuates bidirectionally.
* **Why Examiner Asks This:** Monotonicity intuition.
* **Key Point:** Adversarial escalation is persistent and monotonic; benign work fluctuates.

#### Q182: Why did you use a suspicion threshold of 0.6?
* **Answer:** $\tau = 0.60$ was calibrated empirically on the validation split, achieving optimal trade-off between poisoning suppression (93% detection) and low FSR (4%).
* **Why Examiner Asks This:** Threshold calibration justification ($\tau=0.60$).
* **Key Point:** Empirically calibrated on validation split for optimal FSR/detection balance.

#### Q183: Why 0.6 and not 0.5?
* **Answer:** Lowering $\tau$ to $0.50$ increases false baseline freezes on benign workflow changes (FSR rises from 4% to 14%).
* **Why Examiner Asks This:** Sensitivity analysis check.
* **Key Point:** $\tau=0.50$ increases false baseline freezes ($FSR \to 14\%$).

#### Q184: Why not learn the threshold automatically?
* **Answer:** Automated threshold learning (e.g., Otsu thresholding) on un-gated streaming data is susceptible to adversarial distribution shifting—the exact vulnerability we defend against.
* **Why Examiner Asks This:** Static vs learned threshold reasoning.
* **Key Point:** Learned thresholds on streaming data can be shifted by adversaries.

#### Q185: How sensitive is your system to the threshold?
* **Answer:** Sensitivity analysis shows robust defense across $\tau \in [0.55, 0.65]$, maintaining $>91\%$ detection with $<6\%$ FSR.
* **Why Examiner Asks This:** Parameter sensitivity analysis.
* **Key Point:** Robust performance across range $\tau \in [0.55, 0.65]$.

---

## Category L — Baseline Governance — Very Difficult Questions

#### Q186: What exactly does "contamination-resistant" mean in your project?
* **Answer:** It means the baseline profile $\mathbf{B}_u$ remains anchored to clean reference vectors under slow-rate adversarial injection attacks, resisting steering.
* **Why Examiner Asks This:** Core term definition.
* **Key Point:** Baseline vector profile resists adversarial steering.

#### Q187: Can you mathematically prove that your baseline is contamination resistant?
* **Answer:** We provide empirical proof via Experiment E3: under controlled 5%/month poisoning, our governed baseline suppressed 19 poisoned updates and maintained 93% detection.
* **Why Examiner Asks This:** Theoretical vs empirical proof check.
* **Key Point:** Empirical validation via controlled 6-month poisoning simulation.

#### Q188: What percentage of contaminated data can your baseline tolerate?
* **Answer:** The governance gate suppresses 100% of candidate updates once monthly escalation exceeds $+10\%$, preventing baseline contamination from exceeding 11%.
* **Why Examiner Asks This:** Contamination breakdown limit.
* **Key Point:** Baseline contamination capped at $<11\%$ under active defense.

#### Q189: What happens if the attacker gradually contaminates the baseline over several months?
* **Answer:** Stage 1 acceleration ($S_1$) and Stage 2 peer divergence ($S_2$) accumulate over successive weeks, triggering Stage 4 suppression ($S_{\text{drift}} \ge 0.60$) by Month 2.
* **Why Examiner Asks This:** Multi-month attack tracking.
* **Key Point:** Cumulative scores trigger suppression gate by Month 2.

#### Q190: What happens if the attacker behaves like a legitimate peer?
* **Answer:** If the attacker's behavior matches their peer centroid $\mathbf{C}_{R,D}$ perfectly, no anomaly exists and no threat is present. Exfiltration requires diverging from peer norms.
* **Why Examiner Asks This:** Mimicry attack limits.
* **Key Point:** True exfiltration forces divergence from peer norms.

#### Q191: What happens if the peer group itself is compromised?
* **Answer:** If an entire peer cohort is compromised simultaneously, Stage 2 peer divergence is diminished. Stage 1 acceleration ($S_1$) and Stage 3 monotonicity ($S_3$) still trigger suppression.
* **Why Examiner Asks This:** Coordinated peer group compromise edge case.
* **Key Point:** Stage 1 acceleration and Stage 3 trend checks act as independent safeguards.

#### Q192: What happens if multiple malicious users belong to the same peer group?
* **Answer:** Unless malicious users execute identical exfiltration schedules simultaneously, individual divergence vectors $\Delta_{\text{peer}}$ trigger Stage 2 governance independently.
* **Why Examiner Asks This:** Multi-attacker peer group dynamics.
* **Key Point:** Independent exfiltration schedules cause mutual peer divergence.

#### Q193: Can your governance mechanism fail under coordinated insider attacks?
* **Answer:** Only if an entire peer cohort executes identical slow-escalation trajectories simultaneously. In enterprise environments, coordinated multi-insider collusion is extremely rare.
* **Why Examiner Asks This:** Threat model boundary check.
* **Key Point:** Collusion across entire peer cohorts represents an extreme edge case.

#### Q194: How do you prevent suspicious observations from immediately influencing the baseline?
* **Answer:** Candidate updates are placed in a 7-day staging queue in PostgreSQL (`baselines_governancelog`) until weekly 4-stage governance audits complete.
* **Why Examiner Asks This:** Staging mechanism mechanics.
* **Key Point:** 7-day staging queue audited prior to baseline commitment.

#### Q195: When should suspicious behavior be allowed to enter the baseline?
* **Answer:** Only when human SOC analysts explicitly submit a False Positive verdict via the Analyst Feedback panel (`/feedback`), overriding quarantine.
* **Why Examiner Asks This:** Human-in-the-loop override check.
* **Key Point:** Human analyst manual override via feedback panel.

#### Q196: When should adaptation be frozen?
* **Answer:** Adaptation is frozen automatically whenever composite drift suspicion $S_{\text{drift}} \ge 0.60$, or when an active high-severity alert ($RiskScore \ge 60$) is pending triage.
* **Why Examiner Asks This:** Baseline freeze triggers.
* **Key Point:** Automatically frozen when $S_{\text{drift}} \ge 0.60$ or $RiskScore \ge 60$.

#### Q197: How do you prevent the system from becoming too rigid?
* **Answer:** By calibrating peer divergence weights ($0.40$) and allowing updates when candidate vectors align with peer group centroid shifts.
* **Why Examiner Asks This:** Rigidity vs flexibility balance.
* **Key Point:** Peer centroid alignment permits legitimate updates.

#### Q198: If adaptation is too conservative, what happens?
* **Answer:** The baseline becomes rigid, generating persistent false alarms when benign user job responsibilities expand.
* **Why Examiner Asks This:** Over-conservative adaptation consequence.
* **Key Point:** Rigid baseline increases false alarms during job expansions.

#### Q199: If adaptation is too aggressive, what happens?
* **Answer:** The baseline absorbs anomalous activity rapidly, opening the system to slow-escalation poisoning.
* **Why Examiner Asks This:** Over-aggressive adaptation consequence.
* **Key Point:** Vulnerability to baseline poisoning and threat habituation.

#### Q200: How do you balance adaptation and security?
* **Answer:** Through our 4-stage decoupled governance engine: permitting adaptation only when multi-stage checks confirm drift is peer-aligned and non-monotonic.
* **Why Examiner Asks This:** Core research philosophy summary.
* **Key Point:** Decoupled multi-stage gating balances adaptation and security.

---

## Category M — Risk Fusion

#### Q201: Why do you need risk fusion?
* **Answer:** No single detection model is perfect. XGBoost excels at known signatures; Isolation Forest catches global outliers; peer distances identify role anomalies. Fusing them maximizes detection coverage.
* **Why Examiner Asks This:** Risk fusion necessity.
* **Key Point:** Fuses complementary strengths of supervised, unsupervised, and peer models.

#### Q202: Why not simply use the XGBoost probability?
* **Answer:** XGBoost probability ($P_{\text{xgb}}$) misses novel zero-day attacks not present in training labels and ignores peer group context.
* **Why Examiner Asks This:** Single model reliance critique.
* **Key Point:** Misses zero-day threats and lacks peer group context.

#### Q203: Why combine multiple detection signals?
* **Answer:** To achieve defense-in-depth: a stealthy attack that marginally evades XGBoost thresholds still triggers Isolation Forest path isolation and peer divergence.
* **Why Examiner Asks This:** Defense-in-depth rationale.
* **Key Point:** Multi-layered defense catches sub-threshold anomalies.

#### Q204: What signals contribute to your final risk score?
* **Answer:** Five signals: XGBoost probability ($P_{\text{xgb}}$), Isolation Forest score ($S_{\text{IF}}$), peer deviation ($D_{\text{peer}}$), user baseline deviation ($D_{\text{user}}$), and drift suspicion ($D_{\text{drift}}$).
* **Why Examiner Asks This:** Fusion inputs check.
* **Key Point:** $P_{\text{xgb}}, S_{\text{IF}}, D_{\text{peer}}, D_{\text{user}}, D_{\text{drift}}$.

#### Q205: Why did you choose the particular risk-fusion calculation?
* **Answer:** Fusing weighted linear terms scales outputs cleanly into an interpretable continuous range $RiskScore \in [0, 100]$.
* **Why Examiner Asks This:** Risk fusion formula formulation.
* **Key Point:** $RiskScore = (0.35 P_{\text{xgb}} + 0.25 S_{\text{IF}} + 0.20 D_{\text{peer}} + 0.15 D_{\text{user}} + 0.05 D_{\text{drift}}) \times 100$.

#### Q206: Why did you choose those weights? (0.35, 0.25, 0.20, 0.15, 0.05)
* **Answer:** Weights prioritize high-precision supervised XGBoost ($0.35$), backed by unsupervised anomaly discovery ($0.25$), peer cohort distance ($0.20$), individual baseline distance ($0.15$), and drift suspicion ($0.05$).
* **Why Examiner Asks This:** Weight distribution rationale.
* **Key Point:** Prioritizes supervised precision while incorporating unsupervised and contextual signals.

#### Q207: How were the weights determined?
* **Answer:** Initial empirical values were selected based on domain prioritization and refined via grid search on the chronological validation split to maximize PR-AUC.
* **Why Examiner Asks This:** Weight selection methodology.
* **Key Point:** Empirical domain initialization refined via validation grid search.

#### Q208: Are the weights theoretically justified or empirically selected?
* **Answer:** Empirically selected and validated on the CMU CERT r5.2 validation split.
* **Why Examiner Asks This:** Theoretical vs empirical transparency.
* **Key Point:** Empirically tuned on validation split performance.

#### Q209: What happens if one model is consistently wrong?
* **Answer:** Multi-signal weighting prevents a single failing model from dominating the score. For instance, an incorrect $S_{\text{IF}}$ spike contributes only 25% to total risk.
* **Why Examiner Asks This:** Fault tolerance in fusion.
* **Key Point:** 25% cap prevents single-model false alarm domination.

#### Q210: Can one model dominate the final risk score?
* **Answer:** No single model carries $>35\%$ weight. A Critical alert ($RiskScore \ge 80$) requires agreement across multiple detection components.
* **Why Examiner Asks This:** Dominance prevention check.
* **Key Point:** Critical alerts require multi-component model consensus.

#### Q211: How do you normalize outputs from different models before fusion?
* **Answer:** XGBoost outputs $P \in [0,1]$; Isolation Forest scores are min-max normalized; Euclidean distances ($D_{\text{peer}}, D_{\text{user}}$) are scaled via sigmoid mapping to $[0,1]$.
* **Why Examiner Asks This:** Normalization mechanics.
* **Key Point:** Min-max and sigmoid mapping to unified $[0,1]$ range.

#### Q212: Why is normalization necessary?
* **Answer:** Unscaled Euclidean distances (e.g., raw byte deltas) would dwarf bounded probabilities ($0.0$--$1.0$), distorting risk score calculations.
* **Why Examiner Asks This:** Normalization necessity.
* **Key Point:** Prevents raw large-scale features from overwhelming probabilities.

#### Q213: What does a 0–100 risk score actually mean?
* **Answer:** It is a standardized operational threat severity index reflecting composite anomalous behavior relative to organizational norms.
* **Why Examiner Asks This:** Score operational semantic definition.
* **Key Point:** Standardized threat severity index for SOC triage prioritization.

#### Q214: Is 80% risk equivalent to an 80% probability of malicious behavior?
* **Answer:** No. It is an operational severity score, not a pure Bayesian posterior probability. A score of 80 indicates severe multi-component anomaly alignment.
* **Why Examiner Asks This:** Probability vs risk index distinction.
* **Key Point:** Severity index reflecting multi-source anomaly alignment, not pure probability.

#### Q215: How did you define risk categories?
* **Answer:** Critical ($\ge 80$), High ($60$--$79$), Medium ($30$--$59$), Low ($< 30$), reflecting standard SOC triage escalation workflows.
* **Why Examiner Asks This:** Operational tier definition.
* **Key Point:** Aligned with standard 4-tier SOC incident escalation paths.

#### Q216: How did you determine alert thresholds?
* **Answer:** $RiskScore \ge 60$ triggers High-severity SOC alerts requiring investigation, selected via precision-recall trade-off analysis on validation data.
* **Why Examiner Asks This:** Alert boundary calibration.
* **Key Point:** $RiskScore \ge 60$ calibrated on PR curve for optimal SOC triage.

#### Q217: Why not use a binary anomaly decision?
* **Answer:** Binary outputs ("threat / no threat") force analysts into all-or-nothing triage. Continuous risk scores enable priority queue ranking.
* **Why Examiner Asks This:** Binary vs continuous score trade-off.
* **Key Point:** Continuous scores enable priority ranking and reduce binary false alarms.

#### Q218: What are the drawbacks of your risk-fusion approach?
* **Answer:** Fixed static weights ($0.35, 0.25, \dots$) may not adapt dynamically if enterprise threat profiles change significantly over multi-year horizons.
* **Why Examiner Asks This:** Limitations of fixed weight fusion.
* **Key Point:** Static weights require periodic re-calibration over multi-year horizons.

#### Q219: How could the risk-fusion mechanism be improved?
* **Answer:** By replacing fixed weights with a meta-learner (e.g., Logistic Regression stacking) or Bayesian model averaging.
* **Why Examiner Asks This:** Advanced fusion alternatives.
* **Key Point:** Stacking meta-learner or Bayesian model averaging.

#### Q220: Could a learned fusion model be better than manually defined weights?
* **Answer:** Yes, a stacked meta-classifier learned on validation data can optimize component weights automatically, representing a logical future extension.
* **Why Examiner Asks This:** Future research vision.
* **Key Point:** Stacking meta-classifiers optimize weights automatically.

---

## Category N — SHAP / Explainability

#### Q221: Why did you use SHAP?
* **Answer:** SHAP (SHapley Additive exPlanations) provides mathematically grounded local feature attributions based on game theory, ensuring additive feature fairness.
* **Why Examiner Asks This:** XAI framework selection.
* **Key Point:** Game-theoretic additive local feature attribution.

#### Q222: Why is explainability important in UEBA?
* **Answer:** SOC analysts reject opaque "black-box" risk probabilities. Explainability reveals *why* a user received a High risk score, accelerating incident response.
* **Why Examiner Asks This:** Operational XAI motivation.
* **Key Point:** Black-box scores cause analyst distrust; XAI accelerates triage.

#### Q223: Why does a security analyst need feature-level explanations?
* **Answer:** To immediately identify the attack vector (e.g., whether risk is driven by after-hours USB copies or external email attachments) without manual log parsing.
* **Why Examiner Asks This:** Analyst workflow utility.
* **Key Point:** Identifies root cause exfiltration vector instantly.

#### Q224: Why not simply show the XGBoost probability?
* **Answer:** A raw probability ($P = 0.92$) tells the analyst *that* a threat exists, but gives zero forensic insight into *how* or *why* the prediction was made.
* **Why Examiner Asks This:** Probability vs explanation distinction.
* **Key Point:** Probability provides threat confidence but zero causal insight.

#### Q225: Why SHAP instead of LIME?
* **Answer:** SHAP guarantees mathematical consistency and local accuracy via Shapley values. LIME uses local surrogate sampling, which can produce unstable, inconsistent attributions.
* **Why Examiner Asks This:** SHAP vs LIME comparative analysis.
* **Key Point:** Mathematical consistency and stability vs LIME sampling instability.

#### Q226: What are the advantages of SHAP over LIME?
* **Answer:** Theoretical grounding in game theory, consistency (if a model relies more on a feature, its SHAP value never decreases), and exact computation via TreeSHAP.
* **Why Examiner Asks This:** Theoretical advantages of SHAP.
* **Key Point:** Theoretical consistency and exact TreeSHAP computation.

#### Q227: What are the disadvantages of SHAP?
* **Answer:** High computational complexity for general kernel SHAP, and potential dilution of attributions across highly correlated feature sets.
* **Why Examiner Asks This:** SHAP limitations awareness.
* **Key Point:** Computationally heavy; divides credit across correlated features.

#### Q228: Is SHAP computationally expensive?
* **Answer:** General KernelSHAP is expensive ($\mathcal{O}(2^d)$). However, we deploy **TreeSHAP**, which optimizes complexity down to $\mathcal{O}(T D L^2)$ for tree ensembles.
* **Why Examiner Asks This:** SHAP computational efficiency defense.
* **Key Point:** TreeSHAP reduces complexity from exponential to polynomial $\mathcal{O}(T D L^2)$.

#### Q229: Which SHAP method did you use?
* **Answer:** **TreeSHAP** (`shap.TreeExplainer`), optimized specifically for decision tree ensembles like XGBoost in `shap_explainer.py`.
* **Why Examiner Asks This:** Exact SHAP variant check.
* **Key Point:** `shap.TreeExplainer` (TreeSHAP).

#### Q230: Why is TreeSHAP appropriate for XGBoost?
* **Answer:** TreeSHAP evaluates tree path structure directly, computing exact Shapley values in polynomial time rather than relying on slow sampling approximations.
* **Why Examiner Asks This:** TreeSHAP compatibility reasoning.
* **Key Point:** Direct conditional expectation algorithms over tree structures.

#### Q231: What does a SHAP value represent?
* **Answer:** The change in expected model output attributable to feature $i$ relative to the baseline mean prediction: $f(x) - E[f(x)] = \sum \phi_i$.
* **Why Examiner Asks This:** SHAP mathematical definition.
* **Key Point:** Additive marginal contribution to score deviation from baseline.

#### Q232: What does a positive SHAP value mean?
* **Answer:** $\phi_i > 0$ indicates feature $i$ pushed the risk prediction higher toward the threat classification boundary.
* **Why Examiner Asks This:** SHAP sign interpretation.
* **Key Point:** Feature increased risk prediction (threat amplification).

#### Q233: What does a negative SHAP value mean?
* **Answer:** $\phi_i < 0$ indicates feature $i$ lowered the risk prediction toward benign status (threat mitigation).
* **Why Examiner Asks This:** SHAP sign interpretation.
* **Key Point:** Feature decreased risk prediction (risk mitigation).

#### Q234: Does a high SHAP value mean the feature caused the attack?
* **Answer:** SHAP measures *model feature reliance*, not legal or physical causality. It indicates which feature drove the algorithm's prediction decision.
* **Why Examiner Asks This:** Correlation vs causality distinction.
* **Key Point:** Measures model predictive reliance, not physical causality.

#### Q235: Can SHAP prove causality?
* **Answer:** **No.** SHAP proves statistical feature attribution within the ML model, establishing strong forensic evidence for analyst review.
* **Why Examiner Asks This:** XAI causality limits.
* **Key Point:** Statistical feature attribution, not formal physical proof.

#### Q236: How do you select the top-5 SHAP features?
* **Answer:** In `shap_explainer.py`, features are sorted by absolute Shapley magnitude $|\phi_i|$; the 5 largest values are extracted into the evidence payload.
* **Why Examiner Asks This:** Top-k selection logic.
* **Key Point:** Sorted by absolute magnitude $|\phi_i|$; top 5 extracted.

#### Q237: Why top-5?
* **Answer:** Cognitive load optimization. 5 features provide sufficient context for rapid SOC triage without overwhelming analysts with 44 feature bars.
* **Why Examiner Asks This:** Human factors & UX rationale.
* **Key Point:** Prevents analyst cognitive overload while retaining triage depth.

#### Q238: Why not top-3?
* **Answer:** Top-3 can omit secondary contributing channels in multi-vector exfiltration attacks (e.g., missing HTTP upload when USB and email dominate).
* **Why Examiner Asks This:** Alternative top-k trade-off.
* **Key Point:** Top-3 risks omitting secondary exfiltration modalities.

#### Q239: Why not show all features?
* **Answer:** Displaying all 44 features re-introduces triage fatigue, defeating the purpose of concise explainability.
* **Why Examiner Asks This:** Full feature display critique.
* **Key Point:** Displaying 44 features causes visual clutter and alert fatigue.

#### Q240: Can SHAP explanations be misleading?
* **Answer:** If features are highly correlated, SHAP splits credit between them, making individual feature contributions appear smaller than their combined impact.
* **Why Examiner Asks This:** SHAP pitfalls check.
* **Key Point:** Credit splitting across highly correlated feature pairs.

#### Q241: How do correlated features affect SHAP?
* **Answer:** Attributions are divided among correlated features, which is why grouping features by functional domain in evidence objects provides clearer context.
* **Why Examiner Asks This:** Collinearity in SHAP.
* **Key Point:** Credit division handled via domain grouping in evidence objects.

#### Q242: How do you prevent the LLM from inventing evidence that is not present in SHAP output?
* **Answer:** By constraining the LLM system prompt to accept ONLY the structured JSON Evidence Object created by `evidence_builder.py`, verified via FaithLens audit (Experiment E5).
* **Why Examiner Asks This:** Transition to LLM safety.
* **Key Point:** Strict system prompt bounding + FaithLens audit verification.

---

## Category O — LLM / Explainable Alert System

#### Q243: Why did you introduce an LLM into a cybersecurity system?
* **Answer:** To translate complex mathematical outputs (tree probabilities, SHAP vectors, baseline distances) into plain-English incident narratives for non-expert analysts.
* **Why Examiner Asks This:** LLM integration motivation.
* **Key Point:** Translates mathematical ML artifacts into natural-language triage narratives.

#### Q244: Why not use a rule-based alert explanation?
* **Answer:** Static rule templates produce repetitive, rigid text that fails to synthesize multi-vector contextual trends across dynamic incident timelines.
* **Why Examiner Asks This:** Static templates vs LLM comparison.
* **Key Point:** Static templates are rigid and produce repetitive analyst fatigue.

#### Q245: What exactly does the LLM do?
* **Answer:** It acts purely as a natural-language report synthesizer, taking structured JSON evidence payloads and generating 3–5 sentence incident summaries.
* **Why Examiner Asks This:** Defining LLM scope.
* **Key Point:** Post-hoc evidence synthesis and natural-language report generation.

#### Q246: What information is given to the LLM?
* **Answer:** An immutable JSON payload containing: Employee Context, Composite Risk Breakdown, Top-5 SHAP Attributions (values & directions), and 7-Day Trend trajectory.
* **Why Examiner Asks This:** Prompt payload content audit.
* **Key Point:** Context, Risk breakdown, Top-5 SHAP attributions, 7-day trend.

#### Q247: What information is intentionally not given to the LLM?
* **Answer:** Unstructured raw system logs, sensitive PII passwords, internal database schemas, and unverified external web data.
* **Why Examiner Asks This:** Data privacy & security boundary.
* **Key Point:** Raw logs, database schemas, and PII are excluded.

#### Q248: Can the LLM change the model's prediction?
* **Answer:** **NO.** The prediction is computed deterministically by the Risk Fusion Engine before the LLM is invoked.
* **Why Examiner Asks This:** Decision boundary isolation.
* **Key Point:** Zero influence on ML model predictions or risk scores.

#### Q249: Can the LLM change the risk score?
* **Answer:** **NO.** The composite $RiskScore$ is calculated by `risk_fusion.py` and written to PostgreSQL prior to LLM task dispatch.
* **Why Examiner Asks This:** Risk score integrity check.
* **Key Point:** Immutable risk score recorded prior to LLM invocation.

#### Q250: How do you prevent hallucination?
* **Answer:** Through evidence-constrained prompt bounding: instructing Claude 3.5 Sonnet to state ONLY facts present in the input JSON, verified via FaithLens audit (0.9555 score).
* **Why Examiner Asks This:** Hallucination prevention strategy.
* **Key Point:** Evidence-constrained system prompt + FaithLens audit validation.

#### Q251: How do you ensure the LLM explanation is evidence-grounded?
* **Answer:** By evaluating explanations against the FaithLens rubric (Experiment E5), scoring Factuality ($97.17\%$), Directional Consistency ($97.67\%$), and Completeness ($90.00\%$).
* **Why Examiner Asks This:** Evidence-grounding measurement.
* **Key Point:** FaithLens methodology measuring factuality, direction, and completeness.

#### Q252: What happens when there is insufficient evidence?
* **Answer:** If an alert is in the Low severity tier ($RiskScore < 30$), LLM generation is bypassed entirely to conserve compute resources.
* **Why Examiner Asks This:** Resource optimization edge case.
* **Key Point:** Low-severity telemetry bypasses LLM inference.

#### Q253: What happens if the user asks an unrelated question in the SOC chat?
* **Answer:** In `apps/explanations/views.py`, an intent guardrail inspects user input; out-of-context queries return early: *"I am restricted to analyzing SOC incident evidence."*
* **Why Examiner Asks This:** Guardrails & prompt injection check.
* **Key Point:** Intent guardrail blocks out-of-context chat queries.

#### Q254: Why should the chat return early for out-of-context questions?
* **Answer:** To prevent token budget waste, avoid off-topic conversational drift, and block prompt injection attempts aimed at bypassing security role constraints.
* **Why Examiner Asks This:** Guardrail benefits check.
* **Key Point:** Preserves token budget and prevents prompt injection exploits.

#### Q255: How do you prevent prompt injection?
* **Answer:** User chat inputs are sanitized, concatenated inside immutable system role boundaries, and evaluated against context-checking regex filters before Claude API dispatch.
* **Why Examiner Asks This:** Security protection against prompt injection.
* **Key Point:** Input sanitization + immutable system prompt boundaries.

#### Q256: Why use an LLM instead of a deterministic explanation template?
* **Answer:** LLMs provide fluid multi-turn Q&A capabilities, allowing analysts to ask follow-up questions (e.g., *"Summarize the USB file copy trend over the last 3 days"*).
* **Why Examiner Asks This:** Multi-turn conversational utility.
* **Key Point:** Multi-turn interactive SOC copilot Q&A capabilities.

#### Q257: What are the drawbacks of using an external LLM?
* **Answer:** API licensing cost, network dependency, and 3–10 second inference latency (mitigated by Celery/Redis background dispatch).
* **Why Examiner Asks This:** Trade-offs of cloud LLM API calls.
* **Key Point:** API costs, network dependency, and inference latency.

#### Q258: What happens if the LLM API is unavailable?
* **Answer:** The system falls back to `build_fallback_explanation()`, generating a structured plain-text template based on TreeSHAP attributions.
* **Why Examiner Asks This:** High-availability fallback check.
* **Key Point:** Automatic fallback to deterministic local template engine.

#### Q259: What happens if the LLM produces an incorrect explanation?
* **Answer:** Analysts use the Analyst Feedback panel (`/feedback`) to flag incorrect reports, logging a verdict in `verdicts_analystverdict` for audit tracing.
* **Why Examiner Asks This:** Error tracking & human oversight.
* **Key Point:** Analyst Feedback panel logs verdicts for human-in-the-loop remediation.

#### Q260: How would you evaluate the quality of LLM-generated explanations?
* **Answer:** Using the FaithLens quantitative rubric ($S_{\text{faith}} = 0.40 F + 0.35 D + 0.25 C$), which measures factuality, direction, and evidence completeness.
* **Why Examiner Asks This:** Quantitative evaluation metrics for XAI.
* **Key Point:** FaithLens rubric evaluating factuality, direction, and completeness.

---

## Category P — Django / Backend Technology Choices

#### Q261: Why did you choose Django for the backend?
* **Answer:** Django 4.2 LTS provides an enterprise-ready Python framework with a robust ORM, built-in security controls, native administrative console, and DRF REST support.
* **Why Examiner Asks This:** Backend framework choice rationale.
* **Key Point:** Production-ready Python stack with built-in ORM and DRF support.

#### Q262: Why Django instead of FastAPI?
* **Answer:** Django provides an out-of-the-box ORM, admin panel for security management, and integrated auth models, reducing boilerplate code for full-stack prototypes.
* **Why Examiner Asks This:** Django vs FastAPI comparison.
* **Key Point:** Built-in ORM, admin console, and pre-built authentication models.

#### Q263: Why Django instead of Flask?
* **Answer:** Flask is a micro-framework requiring manual integration of ORMs, migration engines, and security middleware; Django offers a cohesive ecosystem.
* **Why Examiner Asks This:** Django vs Flask comparison.
* **Key Point:** Cohesive built-in ecosystem vs manual Flask wiring.

#### Q264: Why not use Node.js/NestJS for this project?
* **Answer:** Our machine learning pipeline (scikit-learn, XGBoost, SHAP) is native to Python. Using Node.js would require IPC serialization between Node and Python.
* **Why Examiner Asks This:** Language ecosystem alignment.
* **Key Point:** Python ecosystem unifies ML pipeline and backend REST API natively.

#### Q265: What advantage does Django provide for an ML-oriented research system?
* **Answer:** Seamless in-process execution of serialised `.joblib` model binaries directly within backend service modules without cross-language wrapper overhead.
* **Why Examiner Asks This:** ML integration advantage.
* **Key Point:** Direct in-process execution of `.joblib` model binaries.

#### Q266: Why use Django REST Framework?
* **Answer:** DRF provides standardized JSON serialization, paginated viewsets, authentication handlers, and OpenAPI schema documentation.
* **Why Examiner Asks This:** DRF framework choice.
* **Key Point:** Standardized serialization, viewsets, and RESTful API endpoints.

#### Q267: What are the disadvantages of Django for this project?
* **Answer:** Synchronous WSGI execution by default. We addressed this by decoupling long-running ML and LLM tasks using asynchronous Celery workers.
* **Why Examiner Asks This:** Backend limitation awareness.
* **Key Point:** Synchronous WSGI execution mitigated via Celery task queues.

#### Q268: Is Django responsible for ML inference?
* **Answer:** Standard rapid risk scoring occurs in-process via Django service calls; long-running SHAP calculations and LLM calls are offloaded to Celery workers.
* **Why Examiner Asks This:** Inference workload distribution.
* **Key Point:** Rapid risk scoring in-process; heavy SHAP/LLM calls offloaded to Celery.

#### Q269: How do you prevent ML inference from blocking API requests?
* **Answer:** Pre-loading lightweight serialised model weights into memory at server startup, and offloading heavy tasks to asynchronous Celery queues.
* **Why Examiner Asks This:** Non-blocking API strategy.
* **Key Point:** Memory pre-loading + Celery worker task delegation.

#### Q270: What happens when an LLM call takes several seconds?
* **Answer:** The Django API enqueues a Celery task and immediately returns an HTTP 202 Accepted status with a task ID; the React UI polls status asynchronously.
* **Why Examiner Asks This:** Asynchronous HTTP request pattern.
* **Key Point:** Returns HTTP 202 Accepted; frontend polls task result asynchronously.

---

## Category Q — PostgreSQL / Database

#### Q271: Why PostgreSQL?
* **Answer:** PostgreSQL 15 is an advanced, ACID-compliant relational database offering robust JSONB support, index optimization, and high enterprise reliability.
* **Why Examiner Asks This:** Database choice rationale.
* **Key Point:** ACID compliance, JSONB support, and high relational integrity.

#### Q272: Why not MongoDB?
* **Answer:** UEBA data is highly relational (Users $\to$ Baselines $\to$ Alerts $\to$ Verdicts). Document stores lack strict foreign key integrity enforcement across relational entities.
* **Why Examiner Asks This:** SQL vs NoSQL trade-off.
* **Key Point:** Strict foreign key relational integrity across audit entities.

#### Q273: Why not MySQL?
* **Answer:** PostgreSQL offers superior JSONB indexing capabilities for TreeSHAP evidence payloads and better compliance with standard SQL specifications.
* **Why Examiner Asks This:** Postgres vs MySQL comparative choice.
* **Key Point:** Superior JSONB indexing for structured SHAP evidence payloads.

#### Q274: Why is a relational database suitable for this project?
* **Answer:** System entities (Users, Risk Scores, Baseline Logs, Alerts, Verdicts) have rigid relational schemas requiring transactional consistency.
* **Why Examiner Asks This:** Relational schema suitability.
* **Key Point:** Rigid relational schemas and transactional consistency.

#### Q275: What kind of data belongs in PostgreSQL?
* **Answer:** Structured system state: User accounts, 30-day baseline vectors, peer group centroids, risk scores, alerts, SHAP attributions, and analyst feedback verdicts.
* **Why Examiner Asks This:** Database schema scope audit.
* **Key Point:** Core domain state, baseline vectors, alerts, and feedback verdicts.

#### Q276: What relationships exist between your major entities?
* **Answer:** One User has many Daily Risk Scores; One User has many Baseline Governance Logs; One Alert has one SHAP Evidence Object and one Analyst Verdict.
* **Why Examiner Asks This:** Relational ER diagram check.
* **Key Point:** User 1:N RiskScores; User 1:N GovernanceLogs; Alert 1:1 Verdict.

#### Q277: Why is PostgreSQL the source of truth?
* **Answer:** Persistent state is committed atomically to PostgreSQL; Redis is treated as a transient message broker and volatile cache.
* **Why Examiner Asks This:** Source of truth authority check.
* **Key Point:** Atomic persistence in DB; Redis is strictly transient caching.

#### Q278: What are the drawbacks of PostgreSQL for this project?
* **Answer:** Ingesting multi-gigabyte raw event streams directly into relational tables creates high write I/O overhead (solved by processing raw CSVs in pandas first).
* **Why Examiner Asks This:** Database bottleneck identification.
* **Key Point:** Write I/O overhead on raw logs (mitigated by pandas vector processing).

#### Q279: How would the system scale if event volume increased significantly?
* **Answer:** By partitioning raw log ingestion into TimescaleDB or Apache ClickHouse, while retaining PostgreSQL for metadata, alerts, and governance logs.
* **Why Examiner Asks This:** Database scaling architecture.
* **Key Point:** Time-series partitioning via TimescaleDB / ClickHouse.

#### Q280: Would you consider a data warehouse or analytical database for very large-scale deployment?
* **Answer:** Yes. For enterprise scale (>100,000 users), Snowflake or ClickHouse would ingest raw event streams, exporting daily vectors to the ML engine.
* **Why Examiner Asks This:** Enterprise data architecture vision.
* **Key Point:** Snowflake / ClickHouse analytical warehouse for raw stream ingestion.

---

## Category R — Redis / Celery

#### Q281: Why did you choose Redis?
* **Answer:** Redis 7 is an in-memory data store operating as a high-performance message broker for Celery task queues and dynamic session cache.
* **Why Examiner Asks This:** In-memory store selection rationale.
* **Key Point:** High-speed in-memory message broker and session cache.

#### Q282: Why Redis instead of RabbitMQ?
* **Answer:** Redis provides lightweight installation, low memory footprint, and dual-purpose utility as both a Celery message broker and Django cache store.
* **Why Examiner Asks This:** Redis vs RabbitMQ trade-off.
* **Key Point:** Dual-purpose utility: message broker + REST cache store.

#### Q283: Why Redis instead of Kafka?
* **Answer:** Kafka is designed for high-throughput distributed event streaming log persistence; Redis is far simpler and optimal for asynchronous task queuing.
* **Why Examiner Asks This:** Redis vs Kafka trade-off.
* **Key Point:** Task queuing simplicity vs complex event stream persistence.

#### Q284: What is Redis actually doing in your architecture?
* **Answer:** Storing task message payloads passed between Django API producers and Celery background workers, and caching active user risk leaderboards.
* **Why Examiner Asks This:** Architecture role confirmation.
* **Key Point:** Message transport broker + user leaderboard cache.

#### Q285: Why do you need Celery?
* **Answer:** To execute long-running background tasks (TreeSHAP calculations, Claude API calls, weekly governance audits) asynchronously without blocking API responses.
* **Why Examiner Asks This:** Celery necessity check.
* **Key Point:** Offloads long-running ML/LLM tasks from HTTP request threads.

#### Q286: Why not execute LLM inference directly inside the Django request?
* **Answer:** External LLM API calls take 3 to 10 seconds. Direct execution blocks WSGI worker threads, causing HTTP gateway timeouts and frozen UIs.
* **Why Examiner Asks This:** Synchronous HTTP blocking critique.
* **Key Point:** Avoids gateway timeouts and frozen user interfaces.

#### Q287: What happens if the LLM request takes 10 seconds?
* **Answer:** The Celery worker handles the 10-second wait in the background (`llm` queue); the React dashboard remains completely responsive, polling task completion.
* **Why Examiner Asks This:** Async behavior demonstration.
* **Key Point:** Handled in background queue; React dashboard remains responsive.

#### Q288: How does Celery improve the user experience?
* **Answer:** It maintains sub-2-second frontend page load response times, providing immediate user feedback while complex processing runs in the background.
* **Why Examiner Asks This:** User experience impact.
* **Key Point:** Sub-2-second page loads + non-blocking background processing.

#### Q289: Why separate LLM and governance queues?
* **Answer:** Queue segregation ensures that slow external LLM API calls on the `llm` queue do not block critical security governance audits on the `governance` queue.
* **Why Examiner Asks This:** Queue segregation rationale.
* **Key Point:** Prevents slow LLM calls from starving security governance tasks.

#### Q290: Why would LLM tasks and governance tasks require different worker configurations?
* **Answer:** `llm` tasks are I/O-bound (waiting on external API network sockets, concurrency $c=2$); `governance` tasks are CPU-bound (matrix distance calculations, concurrency $c=1$).
* **Why Examiner Asks This:** Worker configuration optimization.
* **Key Point:** I/O-bound network tasks ($c=2$) vs CPU-bound matrix tasks ($c=1$).

#### Q291: What happens if a Celery task fails?
* **Answer:** Celery executes retry logic with exponential backoff (`max_retries=3`). If retries fail, a failure status is written to PostgreSQL and template fallbacks trigger.
* **Why Examiner Asks This:** Task failure resilience check.
* **Key Point:** Exponential backoff retries + database failure logging + fallback.

#### Q292: How do you prevent duplicate task execution?
* **Answer:** By setting unique task ID keys based on alert ID hash (`task_id=f"explain_alert_{alert_id}"`) and enforcing Celery task deduplication.
* **Why Examiner Asks This:** Task deduplication mechanics.
* **Key Point:** Deterministic task ID hashing based on alert ID.

#### Q293: What is idempotency in your task architecture?
* **Answer:** Ensuring that executing a task multiple times produces the exact same database result without generating duplicate alerts or explanations.
* **Why Examiner Asks This:** Idempotency definition check.
* **Key Point:** Repeated task execution produces identical database state.

#### Q294: How do retries affect an LLM task?
* **Answer:** Retries re-send the immutable JSON evidence payload to Claude. Idempotent database writes update the existing explanation record rather than appending duplicates.
* **Why Examiner Asks This:** Retry side-effects check.
* **Key Point:** Updates existing record; prevents duplicate explanation creation.

#### Q295: Could retries generate duplicate explanations?
* **Answer:** No, because `apps/explanations/tasks.py` uses `update_or_create()` mapped to the unique `alert_id` foreign key.
* **Why Examiner Asks This:** Database write safety check.
* **Key Point:** Enforced via Django `update_or_create()` on `alert_id`.

#### Q296: Why did you not choose Kafka for the initial implementation?
* **Answer:** Kafka requires Zookeeper/KRaft clusters, complex topic partition management, and high memory overhead, which is excessive for a single-node prototype.
* **Why Examiner Asks This:** Kafka non-selection trade-off.
* **Key Point:** High infrastructure overhead unnecessary for single-node prototype.

#### Q297: At what scale would Kafka become more appropriate?
* **Answer:** At enterprise scale processing $>100,000$ raw event logs per second across distributed multi-region SIEM deployments.
* **Why Examiner Asks This:** Scale transition threshold.
* **Key Point:** $>100,000$ events/sec across distributed multi-region enterprise SIEMs.

---

## Category S — Frontend / Dashboard

#### Q298: Why did you choose React?
* **Answer:** React 18 provides a component-based architecture with efficient virtual DOM rendering, ideal for building dynamic, high-frequency SOC dashboards.
* **Why Examiner Asks This:** Frontend framework selection.
* **Key Point:** Virtual DOM performance and reusable component architecture.

#### Q299: Why React instead of Angular?
* **Answer:** Angular is a heavy, rigid framework with steep boilerplate requirements; React provides lightweight flexiblity for single-page analytics applications.
* **Why Examiner Asks This:** React vs Angular comparison.
* **Key Point:** Lightweight flexibility vs heavy Angular boilerplate.

#### Q300: Why React instead of Vue?
* **Answer:** React possesses a larger ecosystem of enterprise visualization libraries (Recharts) and wider industry adoption in cybersecurity SOC tooling.
* **Why Examiner Asks This:** React vs Vue comparison.
* **Key Point:** Rich ecosystem of analytics visualization tools (Recharts).

#### Q301: What information should a security analyst see on the dashboard?
* **Answer:** User Risk Leaderboard (top threats), Composite Risk Gauge, 30-Day Trajectory line charts, Top-5 TreeSHAP feature drivers, and Plain-English AI summaries.
* **Why Examiner Asks This:** SOC UI information design.
* **Key Point:** Leaderboard, risk gauge, trajectory line chart, SHAP drivers, AI summary.

#### Q302: Why display a risk score instead of only an alert?
* **Answer:** Continuous risk scores ($0$--$100$) allow analysts to prioritize triage queues, distinguishing critical multi-vector threats ($85$) from minor spikes ($35$).
* **Why Examiner Asks This:** Continuous risk display benefits.
* **Key Point:** Priority queue ranking and triage differentiation.

#### Q303: Why display SHAP evidence?
* **Answer:** To give analysts immediate visibility into the specific behavioral factors driving the elevated score, establishing visual proof for incident reports.
* **Why Examiner Asks This:** Visual XAI value.
* **Key Point:** Provides immediate visual root-cause proof for incident reporting.

#### Q304: How do you avoid overwhelming analysts with too much information?
* **Answer:** By using hierarchical progressive disclosure: displaying high-level threat cards on the main dashboard, reserving deep-dive SHAP features for `/users/:id`.
* **Why Examiner Asks This:** UX & information hierarchy design.
* **Key Point:** Progressive disclosure: high-level cards $\to$ detailed profile views.

#### Q305: What is alert fatigue?
* **Answer:** A critical SOC condition where analysts become desensitized to security notifications due to overwhelming volumes of unprioritized false positive alarms.
* **Why Examiner Asks This:** Alert fatigue domain definition.
* **Key Point:** Analyst desensitization caused by unprioritized false alarms.

#### Q306: How does your system attempt to reduce false-positive alert fatigue?
* **Answer:** Fusing supervised, unsupervised, and peer signals reduces benign false alarms (achieving 100% precision on our 130,051 test split), while LLMs accelerate triage.
* **Why Examiner Asks This:** False positive mitigation proof.
* **Key Point:** Multi-signal risk fusion (100% test precision) + plain-English summaries.

#### Q307: What happens when hundreds of users generate alerts simultaneously?
* **Answer:** The React dashboard uses paginated REST endpoints (`/api/v1/alerts/?page=1`) and sorts the leaderboard dynamically by $RiskScore$ descending.
* **Why Examiner Asks This:** Large alert volume UI handling.
* **Key Point:** Server-side paginated REST endpoints + risk score sorting.

#### Q308: How would you design the dashboard for enterprise-scale usage?
* **Answer:** By integrating WebSockets for real-time alert pushes, multi-analyst ticket assignment status, and role-based access control (RBAC) views.
* **Why Examiner Asks This:** Enterprise SOC UI evolution.
* **Key Point:** WebSockets real-time streaming + RBAC + analyst ticket workflows.

---

## Category T — Evaluation

#### Q309: Why is accuracy not sufficient for insider-threat detection?
* **Answer:** Because insider events represent $<2\%$ of records. A dummy model predicting 100% benign achieves 98% accuracy while missing every single security threat.
* **Why Examiner Asks This:** Evaluation metric critique.
* **Key Point:** High accuracy masks total recall failure under high class imbalance.

#### Q310: Why is precision important?
* **Answer:** Precision ($\frac{TP}{TP + FP}$) measures the proportion of flagged alerts that are actual threats, directly impacting SOC alert fatigue.
* **Why Examiner Asks This:** Precision operational meaning.
* **Key Point:** Directly measures false positive rate and SOC alert fatigue.

#### Q311: Why is recall important?
* **Answer:** Recall ($\frac{TP}{TP + FN}$) measures the proportion of actual insider threat events caught by the system, directly impacting organizational security posture.
* **Why Examiner Asks This:** Recall operational meaning.
* **Key Point:** Measures threat coverage and risk of undetected exfiltration.

#### Q312: Which is more important in your application: precision or recall?
* **Answer:** **Recall** is primary (missing an insider exfiltrating trade secrets is catastrophic), but high precision must be maintained to prevent operational alert fatigue.
* **Why Examiner Asks This:** Security operational trade-off choice.
* **Key Point:** Recall is primary for threat defense; precision prevents SOC fatigue.

#### Q313: Can you justify that choice?
* **Answer:** A false positive costs 15 minutes of analyst review; a false negative (undetected exfiltration) can cost millions of dollars in IP loss or regulatory fines.
* **Why Examiner Asks This:** Operational cost justification.
* **Key Point:** Cost of missed threat (millions) vastly exceeds cost of false alarm (minutes).

#### Q314: What is the cost of a false positive?
* **Answer:** SOC analyst time, wasted investigation resources, and operational friction.
* **Why Examiner Asks This:** False positive cost definition.
* **Key Point:** Wasted analyst triage time and operational friction.

#### Q315: What is the cost of a false negative?
* **Answer:** Undetected exfiltration of sensitive IP, regulatory compliance penalties, data breaches, and severe reputational damage.
* **Why Examiner Asks This:** False negative cost definition.
* **Key Point:** Unmitigated data exfiltration and major financial/reputational damage.

#### Q316: Why use F1-score?
* **Answer:** F1-score computes the harmonic mean of precision and recall ($2 \cdot \frac{P \cdot R}{P + R}$), providing a single balanced metric under class imbalance.
* **Why Examiner Asks This:** F1-score metric justification.
* **Key Point:** Harmonic mean balancing precision and recall under class imbalance.

#### Q317: Why use ROC-AUC?
* **Answer:** Area Under the Receiver Operating Characteristic Curve (ROC-AUC) measures model discrimination power across all possible operational classification thresholds.
* **Why Examiner Asks This:** ROC-AUC metric justification.
* **Key Point:** Threshold-agnostic measure of class discrimination capability.

#### Q318: Why might PR-AUC be more informative for highly imbalanced insider-threat data?
* **Answer:** PR-AUC (Precision-Recall AUC) focuses strictly on the minority positive class without being inflated by true negatives in massive majority classes.
* **Why Examiner Asks This:** PR-AUC vs ROC-AUC distinction.
* **Key Point:** Evaluates minority threat class directly without true negative inflation.

#### Q319: What does your confusion matrix tell you?
* **Answer:** On our 130,051 test records: True Positives $= 3,705$, False Positives $= 0$, False Negatives $= 8$, True Negatives $= 126,338$, showing 99.78% recall and 100% precision.
* **Why Examiner Asks This:** Empirical confusion matrix reading.
* **Key Point:** $3,705$ TP, $0$ FP, $8$ FN, $126,338$ TN.

#### Q320: How do you compare the models fairly?
* **Answer:** By evaluating all models (SVM, XGBoost, Hybrid Fusion) on the identical held-out chronological test split (130,051 records) using identical metric definitions.
* **Why Examiner Asks This:** Comparative evaluation integrity.
* **Key Point:** Identical test split, feature matrix, and evaluation metrics.

#### Q321: Why must all models use the same evaluation split?
* **Answer:** Using different test splits introduces sample variance, rendering comparative performance metrics scientifically invalid.
* **Why Examiner Asks This:** Scientific experimental controls.
* **Key Point:** Eliminates sample variance to ensure scientific validity.

#### Q322: Why is chronological evaluation important?
* **Answer:** It mirrors real-world deployment, testing whether historical model training effectively predicts future, unobserved user behavioral telemetry.
* **Why Examiner Asks This:** Real-world simulation fidelity.
* **Key Point:** Tests predictive accuracy on future, unobserved operational days.

#### Q323: How do you ensure the test data represents future behavior?
* **Answer:** By partitioning data chronologically: training on the first 80% of calendar days and evaluating strictly on the final 20% of calendar days.
* **Why Examiner Asks This:** Time-series split verification.
* **Key Point:** Temporal partitioning (first 80% train / final 20% test).

#### Q324: How would you statistically validate your results?
* **Answer:** By conducting paired $t$-tests or McNemar's tests across 5 random chronological seeds to confirm performance differences are statistically significant ($p < 0.05$).
* **Why Examiner Asks This:** Statistical significance testing.
* **Key Point:** Paired $t$-tests / McNemar's tests across seeds ($p < 0.05$).

#### Q325: How would you prove that your governance mechanism actually improves over a conventional baseline?
* **Answer:** By comparing Experiment E2 (ungoverned baseline detection collapsed to 22%) against Experiment E3 (governed baseline sustained 93% detection) under identical poisoning attacks.
* **Why Examiner Asks This:** Core hypothesis proof check.
* **Key Point:** E2 vs E3 comparative proof under identical poisoning injection.

---

## Category U — Results — Questions Judges Can Attack

#### Q326: Which result is the most important result in your research?
* **Answer:** **Experiment E3:** Proving that our 4-stage governance engine sustains a **93.0% detection rate** across 6 months of active poisoning, whereas ungoverned models collapse to **22.0%** (E2).
* **Why Examiner Asks This:** Key research milestone identification.
* **Key Point:** E3 defense validation sustaining 93% detection vs 22% collapse.

#### Q327: Which model performed best?
* **Answer:** The **Hybrid Adaptive Risk Fusion Engine**, achieving an **AUC of 0.9782** and **F1-score of 0.9412**, outperforming standalone SVM ($0.8842$) and XGBoost ($0.9415$).
* **Why Examiner Asks This:** Master model comparison check.
* **Key Point:** Hybrid Fusion achieved superior AUC (0.9782) and F1 (0.9412).

#### Q328: Why did it perform best?
* **Answer:** Because it combines supervised tree precision, unsupervised outlier detection, and contextual peer/individual baseline deviation distances.
* **Why Examiner Asks This:** Performance attribution reasoning.
* **Key Point:** Multi-signal integration catches complementary threat vectors.

#### Q329: Could the performance be caused by data leakage?
* **Answer:** **No.** `splitter.py` strictly enforced chronological partitioning (562,594 train / 130,051 test rows). No future telemetry entered training sets.
* **Why Examiner Asks This:** Defending against data leakage suspicion.
* **Key Point:** Enforced chronological time-series splitting prevents leakage.

#### Q330: Could class imbalance artificially inflate your results?
* **Answer:** No, because we evaluate Precision, Recall, F1-score, and ROC-AUC—metrics specifically selected because they do not suffer from majority class inflation.
* **Why Examiner Asks This:** Imbalance inflation critique defense.
* **Key Point:** Evaluated on F1, Recall, Precision, and AUC—not accuracy.

#### Q331: Did SMOTE affect your reported performance?
* **Answer:** Yes, SMOTE oversampling improved minority class decision boundary resolution, increasing test recall from $81.2\%$ to $94.1\%$.
* **Why Examiner Asks This:** Impact of SMOTE on final metrics.
* **Key Point:** Increased minority class recall from 81.2% to 94.1%.

#### Q332: Did you evaluate without SMOTE?
* **Answer:** Yes. In Experiment E1 baseline trials, XGBoost without SMOTE achieved lower recall ($81.2\%$) due to decision tree bias toward the 98% majority class.
* **Why Examiner Asks This:** SMOTE ablation evidence.
* **Key Point:** Un-smoted XGBoost recall dropped to 81.2%.

#### Q333: Did you compare against a static baseline?
* **Answer:** Yes. A static baseline generated high false alarms on benign workflow changes, yielding a poor F1-score of $0.62$.
* **Why Examiner Asks This:** Static baseline comparison check.
* **Key Point:** Static baseline F1 dropped to 0.62 due to high false alarms.

#### Q334: Did you compare against an adaptive baseline without governance?
* **Answer:** Yes, that was **Experiment E2**: under 5%/month poisoning, detection rate collapsed from $94.0\%$ down to $22.0\%$ as contamination reached $89.0\%$.
* **Why Examiner Asks This:** Experiment E2 benchmark reference.
* **Key Point:** E2 proved ungoverned baseline collapse to 22.0%.

#### Q335: How do you demonstrate that your governance mechanism provides value?
* **Answer:** By showing that governed Experiment E3 maintained a $93.0\%$ detection rate under the exact poisoning scenario where ungoverned E2 failed.
* **Why Examiner Asks This:** Value proposition of research.
* **Key Point:** Direct E2 vs E3 delta proves governance value.

#### Q336: What ablation experiments would you perform?
* **Answer:** Removing individual governance stages ($S_1, S_2, S_3$), removing SMOTE, removing Isolation Forest ($S_{\text{IF}}$), and removing peer distance features ($D_{\text{peer}}$).
* **Why Examiner Asks This:** Ablation study methodology.
* **Key Point:** Stage-wise, model-wise, and feature-wise ablation trials.

#### Q337: What happens if you remove peer-group features?
* **Answer:** Experiment E4 drift classification accuracy drops from $94.0\%$ to $68.0\%$, because the system can no longer tell if drift is aligned with co-workers.
* **Why Examiner Asks This:** Peer feature ablation impact.
* **Key Point:** Drift classification accuracy collapses to 68.0%.

#### Q338: What happens if you remove temporal features?
* **Answer:** Detection recall drops by $\approx 18\%$, because after-hours and weekend exfiltration signatures are lost.
* **Why Examiner Asks This:** Temporal feature ablation impact.
* **Key Point:** Recall drops by 18% as after-hours signatures are lost.

#### Q339: What happens if you remove the adaptive governance mechanism?
* **Answer:** The system reverts to an ungoverned adaptive model (E2), becoming vulnerable to 6-month slow-escalation poisoning.
* **Why Examiner Asks This:** Governance ablation impact.
* **Key Point:** System becomes vulnerable to slow poisoning (E2 collapse).

#### Q340: What happens if you remove Isolation Forest?
* **Answer:** Zero-day threat detection capability drops, reducing hybrid AUC from $0.9782$ to $0.9415$.
* **Why Examiner Asks This:** Isolation Forest ablation impact.
* **Key Point:** Hybrid AUC drops from 0.9782 to 0.9415.

#### Q341: What happens if you remove SHAP?
* **Answer:** Model detection metrics remain identical, but local forensic explainability is lost, leaving analysts with opaque risk probabilities.
* **Why Examiner Asks This:** SHAP ablation impact.
* **Key Point:** Detection metrics unchanged; forensic explainability is lost.

#### Q342: What happens if you remove the LLM?
* **Answer:** The system continues functioning normally; incident explanations fall back to deterministic local TreeSHAP templates (`build_fallback_explanation()`).
* **Why Examiner Asks This:** LLM ablation impact.
* **Key Point:** System falls back to local TreeSHAP template engine.

---

## Category V — Research Contribution / Novelty

#### Q343: If XGBoost, SHAP, Isolation Forest, and CERT already exist, where is your novelty?
* **Answer:** Novelty is in the **system architecture and algorithmic defense**: integrating peer-anchored 4-stage governance to solve slow-escalation baseline poisoning, and evidence-bounding LLMs via TreeSHAP payloads.
* **Why Examiner Asks This:** Direct attack on novelty.
* **Key Point:** Novelty lies in baseline governance algorithms and evidence-bounded XAI architecture.

#### Q344: Is your novelty the ML model or the governance mechanism?
* **Answer:** The **governance mechanism** (Algorithm 1 in Paper 1). The ML classifiers provide the scoring layer; governance provides contamination resistance.
* **Why Examiner Asks This:** Identifying primary scientific claim.
* **Key Point:** Governance mechanism is the primary scientific contribution.

#### Q345: Why is baseline governance a research contribution?
* **Answer:** Because online learning vulnerability to adversarial steering is a major open problem in machine learning security. Formally defending it on CERT r5.2 fills a recognized gap.
* **Why Examiner Asks This:** Academic merit of baseline governance.
* **Key Point:** Addresses online learning vulnerability in adversarial ML security.

#### Q346: How is your approach different from simple concept drift detection?
* **Answer:** Simple concept drift algorithms (e.g., ADWIN or DDM) detect statistical changes globally without distinguishing whether drift is legitimate role transition or adversarial poisoning.
* **Why Examiner Asks This:** Concept drift distinction.
* **Key Point:** Concept drift detects variance; our governance disambiguates benign vs malicious intent.

#### Q347: How is your approach different from online learning?
* **Answer:** Standard online learning updates model weights unconditionally on incoming vectors. Our system gates baseline profile updates through a 4-stage validation gate.
* **Why Examiner Asks This:** Online learning distinction.
* **Key Point:** Gated update validation vs unconditional weight updates.

#### Q348: How is your approach different from continuous model retraining?
* **Answer:** Continuous retraining re-fits model weights on recent data (risking model poisoning). Our system freezes baselines when suspicion is high, retaining clean reference states.
* **Why Examiner Asks This:** Model retraining distinction.
* **Key Point:** Gated baseline freezing vs un-gated weight retraining.

#### Q349: Why not simply retrain the model whenever behavior changes?
* **Answer:** Retraining on poisoned incoming vectors bakes the attack trajectory into the model weights, accomplishing the attacker's objective.
* **Why Examiner Asks This:** Naive retraining pitfall.
* **Key Point:** Retraining on un-gated data bakes attacks into model weights.

#### Q350: What happens if your baseline governance mechanism itself makes an incorrect decision?
* **Answer:** If it suppresses a legitimate update (FSR $= 4.00\%$), the user's baseline is frozen temporarily; human SOC feedback manually unlocks quarantine via `/feedback`.
* **Why Examiner Asks This:** Governance error handling.
* **Key Point:** 4% false suppression handled via analyst manual override.

#### Q351: What is the strongest evidence supporting your research contribution?
* **Answer:** The empirical delta between E2 ($22\%$ detection) and E3 ($93\%$ detection) under 6-month poisoning, and E5's $0.9555$ FaithLens score.
* **Why Examiner Asks This:** Best empirical evidence check.
* **Key Point:** E2 vs E3 71% detection gap + 0.9555 FaithLens score.

#### Q352: What is the weakest part of your research?
* **Answer:** Evaluation is conducted on synthetic CERT r5.2 data rather than multi-year live enterprise networks, and peer centroids depend on LDAP role accuracy.
* **Why Examiner Asks This:** Intellectual honesty test.
* **Key Point:** Synthetic dataset nature + reliance on LDAP role accuracy.

---

## Category W — Alternatives — Judge's Favorite Questions

#### Q353: What alternative architectures did you consider?
* **Answer:** End-to-end deep temporal autoencoders (BRITD) and microservice event streams. We selected modular monolith + Celery async queues for interpretability and low latency.
* **Why Examiner Asks This:** Architecture trade-off audit.
* **Key Point:** Selected modular monolith for XAI transparency and latency.

#### Q354: What alternative ML algorithms did you consider?
* **Answer:** Random Forest, LightGBM, Deep Autoencoders, and Recurrent Neural Networks (LSTM). XGBoost+SMOTE achieved superior PR-AUC on tabular features.
* **Why Examiner Asks This:** ML model selection trade-offs.
* **Key Point:** XGBoost+SMOTE achieved optimal PR-AUC on tabular data.

#### Q355: What alternative anomaly-detection methods did you consider?
* **Answer:** One-Class SVM, Local Outlier Factor (LOF), and Autoencoders. Isolation Forest was selected for fast linear $\mathcal{O}(N)$ scaling and low memory overhead.
* **Why Examiner Asks This:** Anomaly detection alternatives.
* **Key Point:** Isolation Forest chosen for $\mathcal{O}(N)$ scaling and efficiency.

#### Q356: What alternative explainability techniques did you consider?
* **Answer:** LIME and integrated gradients. TreeSHAP was selected for exact Shapley values and mathematical consistency.
* **Why Examiner Asks This:** XAI framework alternatives.
* **Key Point:** TreeSHAP chosen for exact Shapley values and consistency.

#### Q357: What alternative databases did you consider?
* **Answer:** MongoDB and MySQL. PostgreSQL 15 was selected for JSONB indexing of TreeSHAP payloads and strict relational integrity.
* **Why Examiner Asks This:** DB alternatives.
* **Key Point:** PostgreSQL chosen for JSONB support and relational integrity.

#### Q358: What alternative backend frameworks did you consider?
* **Answer:** FastAPI and Flask. Django 4.2 LTS was selected for built-in ORM, admin console, and native REST framework support.
* **Why Examiner Asks This:** Backend alternatives.
* **Key Point:** Django chosen for integrated ORM and admin management.

#### Q359: What alternative message brokers did you consider?
* **Answer:** RabbitMQ and Apache Kafka. Redis 7 was selected for low memory footprint and dual utility as cache and broker.
* **Why Examiner Asks This:** Message broker alternatives.
* **Key Point:** Redis chosen for low footprint and dual cache/broker role.

#### Q360: What alternative LLM approaches did you consider?
* **Answer:** Fine-tuning open-weight Llama 3 models locally vs Claude 3.5 Sonnet API. Claude 3.5 Sonnet provided superior instruction-following for evidence-constrained prompts.
* **Why Examiner Asks This:** LLM approach alternatives.
* **Key Point:** Claude 3.5 Sonnet chosen for instruction-following precision.

#### Q361: What alternative baseline adaptation strategies exist?
* **Answer:** Exponentially weighted moving averages (EWMA) and Bayesian online changepoint detection. Our 4-stage peer-anchored gate provides explicit protection against poisoning.
* **Why Examiner Asks This:** Baseline strategy alternatives.
* **Key Point:** 4-stage governance gate provides explicit poisoning defense.

#### Q362: Why did you reject each major alternative?
* **Answer:** Based on empirical trade-offs: opacity (deep nets), sampling instability (LIME), quadratic scaling (SVM/LOF), and infrastructure complexity (Kafka).
* **Why Examiner Asks This:** Summary of trade-off rationale.
* **Key Point:** Rejected based on scaling, opacity, instability, or complexity.

---

## Category X — Drawbacks / Limitations

#### Q363: What is the biggest limitation of your system?
* **Answer:** Reliance on static CERT r5.2 CSV log exports rather than live streaming Active Directory feeds.
* **Why Examiner Asks This:** System limitation recognition.
* **Key Point:** Evaluation on static log exports vs live streaming feeds.

#### Q364: What is the biggest limitation of the CERT dataset?
* **Answer:** Synthetic background noise models lack real-world organizational chaos, unannounced IT changes, and complex human behavioral variances.
* **Why Examiner Asks This:** Dataset limitation recognition.
* **Key Point:** Synthetic background noise lacks real enterprise chaos.

#### Q365: What is the biggest limitation of your ML approach?
* **Answer:** Supervised XGBoost relies on labeled training scenarios; novel threats rely heavily on the unsupervised Isolation Forest component.
* **Why Examiner Asks This:** ML model limitation awareness.
* **Key Point:** Supervised component requires representative training signatures.

#### Q366: What is the biggest limitation of adaptive baselines?
* **Answer:** They require an initial 30-day clean observation window ($W=30$) to establish trustworthy reference baselines.
* **Why Examiner Asks This:** Adaptive baseline limitation.
* **Key Point:** Requires clean initial 30-day baseline bootstrapping window.

#### Q367: What is the biggest limitation of peer-group comparison?
* **Answer:** In small organizations or unique roles with fewer than 3 employees, peer group centroids have higher variance, forcing fallback to department means.
* **Why Examiner Asks This:** Peer group limitation.
* **Key Point:** High centroid variance in small teams ($<3$ users).

#### Q368: What is the biggest limitation of SHAP?
* **Answer:** Attribution splitting across highly correlated features can dilute individual feature importance scores.
* **Why Examiner Asks This:** SHAP limitation.
* **Key Point:** Feature attribution splitting across correlated feature pairs.

#### Q369: What is the biggest limitation of LLM-generated explanations?
* **Answer:** Dependency on external API socket latency (3–10 seconds) and subscription licensing costs.
* **Why Examiner Asks This:** LLM limitation.
* **Key Point:** API network latency and subscription costs.

#### Q370: What is the biggest limitation of your risk-fusion mechanism?
* **Answer:** Component weights ($0.35, 0.25, \dots$) are fixed static values that require manual grid-search tuning on new dataset distributions.
* **Why Examiner Asks This:** Risk fusion limitation.
* **Key Point:** Static weights require manual re-tuning across new datasets.

#### Q371: What is the biggest limitation of your current architecture?
* **Answer:** Single-node processing limits daily feature vector extraction scale; enterprise multi-million user logs require distributed Spark/ClickHouse clusters.
* **Why Examiner Asks This:** Architecture scaling limitation.
* **Key Point:** Single-node feature extraction limits multi-million user scale.

#### Q372: Can your system operate in real time?
* **Answer:** Risk scoring operates near-real-time (sub-second API response); feature vector extraction is currently batched on daily logs.
* **Why Examiner Asks This:** Real-time processing capability check.
* **Key Point:** Risk scoring is near-real-time; feature extraction is daily batch.

#### Q373: What happens under very high event volume?
* **Answer:** Batched pandas feature extraction requires scaling up memory or migrating to PySpark; risk scoring REST APIs scale horizontally via Gunicorn workers.
* **Why Examiner Asks This:** High throughput handling.
* **Key Point:** Feature extraction requires PySpark; APIs scale via Gunicorn.

#### Q374: Can your system detect coordinated insider attacks?
* **Answer:** Yes, if attackers exfiltrate along individual schedules. Coordinated identical exfiltration across an entire peer cohort presents a challenging edge case.
* **Why Examiner Asks This:** Collusion attack detection.
* **Key Point:** Detects independent multi-insiders; cohort-wide collusion is an edge case.

#### Q375: Can it detect zero-day insider behavior?
* **Answer:** Yes. Unsupervised Isolation Forest ($S_{\text{IF}}$) and peer divergence ($D_{\text{peer}}$) flag structural statistical anomalies without prior signatures.
* **Why Examiner Asks This:** Zero-day threat detection proof.
* **Key Point:** Unsupervised Isolation Forest and peer divergence detect zero-day threats.

#### Q376: Can it detect a malicious administrator?
* **Answer:** Yes. IT admins accessing sensitive HR/finance shares or copying system databases execute multi-channel anomalies flagged by role-normalized features.
* **Why Examiner Asks This:** Privileged insider detection check.
* **Key Point:** Role-normalized features flag unauthorized cross-domain access.

#### Q377: Can it detect an attacker who behaves very slowly?
* **Answer:** Yes. That is the core capability validated in Experiment E3 (sustaining 93% detection against 5%/month slow-escalation poisoning).
* **Why Examiner Asks This:** Core research problem check.
* **Key Point:** Validated in E3: 93% detection against 5%/month slow escalation.

#### Q378: What attacks can your system fail to detect?
* **Answer:** Passive insider surveillance (reading authorized files on screen without copying/transmitting) generates no digital log footprint and cannot be detected by log analytics.
* **Why Examiner Asks This:** Blind spot identification.
* **Key Point:** Passive visual viewing creates zero digital log footprint.

---

## Category Y — Security Questions

#### Q379: Can an attacker manipulate your behavioral features?
* **Answer:** An attacker can throttle activity (e.g., copying fewer files per day). However, staging or exfiltrating data ultimately requires digital transfers that diverge from peers.
* **Why Examiner Asks This:** Adversarial feature manipulation.
* **Key Point:** Throttling delays attack, but exfiltration ultimately forces feature divergence.

#### Q380: Can an attacker poison the baseline intentionally?
* **Answer:** In an ungoverned system, yes (E2 proved 89% contamination). In our governed system (E3), Stage 2 peer divergence and Stage 3 trend checks block poisoned updates.
* **Why Examiner Asks This:** Intentional baseline poisoning defense.
* **Key Point:** Blocked by Stage 2 peer divergence and Stage 3 trend checks.

#### Q381: Can an attacker poison the training data?
* **Answer:** Training data is constructed from validated initial historical records ($W=30$). Adversarial injection during training is mitigated by Isolation Forest outlier filtering.
* **Why Examiner Asks This:** Training set poisoning defense.
* **Key Point:** Initial 30-day clean bootstrapping + Isolation Forest filtering.

#### Q382: How would adversarial ML affect your system?
* **Answer:** Adversarial perturbations targeting XGBoost probabilities ($P_{\text{xgb}}$) are counterbalanced by unsupervised Isolation Forest ($S_{\text{IF}}$) and peer divergence ($D_{\text{peer}}$).
* **Why Examiner Asks This:** Adversarial ML robustness.
* **Key Point:** Multi-model fusion counterbalances single-model adversarial evasion.

#### Q383: What happens if an attacker knows your detection thresholds?
* **Answer:** Knowing $\tau = 0.60$ allows an attacker to attempt throttling. However, peer divergence $D_{\text{peer}}$ accumulates over time, eventually exceeding the threshold.
* **Why Examiner Asks This:** Knowledge of system parameters attack.
* **Key Point:** Cumulative peer divergence eventually breaches thresholds over time.

#### Q384: Can an attacker deliberately stay below the anomaly threshold?
* **Answer:** Throttling exfiltration to sub-threshold rates delays data theft by months or years, severely impairing the attack's operational utility.
* **Why Examiner Asks This:** Sub-threshold throttling analysis.
* **Key Point:** Sub-threshold throttling severely impairs attack utility and speed.

#### Q385: Can an attacker manipulate peer-group statistics?
* **Answer:** Only if the attacker controls a majority of accounts in that peer role, which requires broad organization-wide compromise.
* **Why Examiner Asks This:** Peer group statistical manipulation.
* **Key Point:** Requires compromising majority of accounts in that LDAP role.

#### Q386: How would you defend against model poisoning?
* **Answer:** By enforcing multi-stage update governance, maintaining immutable baseline backups, and incorporating human-in-the-loop analyst verification.
* **Why Examiner Asks This:** Model poisoning defense summary.
* **Key Point:** Multi-stage governance + baseline backups + human analyst verification.

#### Q387: How would you defend against prompt injection?
* **Answer:** Input sanitization, immutable system role bounding, intent guardrails in `views.py`, and excluding database modification credentials from the LLM execution context.
* **Why Examiner Asks This:** Prompt injection defense check.
* **Key Point:** Input sanitization + system role bounding + context guardrails.

#### Q388: How would you protect sensitive employee behavioral data?
* **Answer:** Encrypting audit data at rest (AES-256) and in transit (TLS 1.3), enforcing RBAC data access, and pseudonymizing user identifiers in analytics views.
* **Why Examiner Asks This:** Data protection & encryption standards.
* **Key Point:** AES-256 at rest, TLS 1.3 in transit, PII pseudonymization.

#### Q389: What privacy concerns exist with UEBA?
* **Answer:** Monitoring email sentiment, web browsing, and session hours raises employee surveillance and privacy concerns under GDPR/CCPA.
* **Why Examiner Asks This:** Privacy & ethical considerations.
* **Key Point:** Surveillance concerns under GDPR/CCPA regulatory frameworks.

#### Q390: How would you ensure that UEBA is not abused for employee surveillance?
* **Answer:** Restricting analytics strictly to security anomaly indicators, enforcing RBAC audit logs for SOC analysts, and implementing privacy-preserving data aggregation.
* **Why Examiner Asks This:** Ethical deployment guardrails.
* **Key Point:** Purpose-bound security scope + analyst RBAC audit logging.

---

## Category Z — Extremely Difficult Judge Questions

#### Q391: What happens if the attacker's behavior becomes the new normal?
* **Answer:** In ungoverned models, it becomes normal (E2 collapse). In our governed system, Stage 2 peer divergence suppresses updates indefinitely until an analyst investigates.
* **Why Examiner Asks This:** Core threat scenario test.
* **Key Point:** Governance suppresses update indefinitely due to persistent peer divergence.

#### Q392: How do you mathematically distinguish legitimate drift from malicious drift?
* **Answer:** Via Stage 2 score $S_2 = \min(\max(1.5 \cdot \max(0, D_{\text{user}} - D_{\text{peer}}), 0), 1)$. Legitimate drift moves *with* peer centroids ($D_{\text{user}} \approx D_{\text{peer}} \implies S_2 \approx 0$).
* **Why Examiner Asks This:** Mathematical disambiguation proof.
* **Key Point:** $D_{\text{user}} \approx D_{\text{peer}} \implies S_2 \approx 0$ (Legitimate); $D_{\text{user}} \gg D_{\text{peer}} \implies S_2 \to 1$ (Malicious).

#### Q393: What prevents your adaptive mechanism from learning the attacker's behavior?
* **Answer:** Stage 4 composite gating: if $S_{\text{drift}} \ge 0.60$, the baseline $\mathbf{B}_u^{(t)}$ is frozen at $\mathbf{B}_u^{(t-1)}$, preventing malicious vector absorption.
* **Why Examiner Asks This:** Baseline freeze mechanism check.
* **Key Point:** Baseline is frozen at prior clean state $\mathbf{B}_u^{(t-1)}$.

#### Q394: Why should we trust your 0–100 risk score?
* **Answer:** Because it is mathematically fused from 5 complementary indicators, backed by exact local TreeSHAP attributions and validated on 130,051 test records with 0 false alarms.
* **Why Examiner Asks This:** Trust & validation audit.
* **Key Point:** Multi-signal mathematical fusion + exact TreeSHAP attributions + 0 test false alarms.

#### Q395: What is the theoretical justification for your risk-fusion formula?
* **Answer:** It represents a multi-attribute utility model combining supervised probability, unsupervised anomaly density, peer distance, and historical deviation.
* **Why Examiner Asks This:** Theoretical modeling framework.
* **Key Point:** Multi-attribute utility decision framework.

#### Q396: Why should we trust a SHAP explanation?
* **Answer:** SHAP is uniquely proven in game theory (Shapley, 1953) as the *only* additive feature attribution method satisfying efficiency, symmetry, dummy, and additivity axioms.
* **Why Examiner Asks This:** Theoretical proof of SHAP trust.
* **Key Point:** Uniquely satisfies Shapley game-theoretic axioms.

#### Q397: Can SHAP tell us why an attack happened?
* **Answer:** SHAP tells us *which features drove the model's prediction*. Human analysts interpret those feature attributions to deduce attacker intent.
* **Why Examiner Asks This:** Feature attribution vs intent deduction.
* **Key Point:** Identifies model feature attributions; analysts infer intent.

#### Q398: If your model detects an anomaly but the baseline considers it normal, which decision wins?
* **Answer:** The Risk Fusion Engine combines both. An XGBoost spike ($P_{\text{xgb}}=0.90$) weighted at $0.35$ produces $RiskScore \ge 31.5$, triggering a Medium severity review.
* **Why Examiner Asks This:** Component conflict resolution.
* **Key Point:** Risk Fusion Engine calculates composite score; multi-signal consensus decides.

#### Q399: If XGBoost says normal but Isolation Forest says anomalous, what happens?
* **Answer:** Isolation Forest score ($S_{\text{IF}} = 0.85$) contributes $0.25 \times 85 = 21.25$ points, elevating the score to Medium tier for potential zero-day review.
* **Why Examiner Asks This:** Conflict handling scenario.
* **Key Point:** Elevates composite score to Medium tier for zero-day review.

#### Q400: If the peer group itself contains malicious users, doesn't your peer comparison fail?
* **Answer:** Peer centroids $\mathbf{C}_{R,D}$ use medians or trimmed means across cohort members, resisting distortion unless $>50\%$ of the role cohort is malicious.
* **Why Examiner Asks This:** Robust statistics in peer centroids.
* **Key Point:** Trimmed means/medians resist distortion unless $>50\%$ of cohort is compromised.

#### Q401: If an entire department changes behavior legitimately, won't your system generate false positives?
* **Answer:** **No.** Department-wide shifts update peer centroid $\mathbf{C}_{R,D}$, keeping peer divergence $S_2$ low and allowing baseline updates ($V=\text{ALLOW}$).
* **Why Examiner Asks This:** Department-wide shift resilience.
* **Key Point:** Shift in peer centroid keeps peer divergence low.

#### Q402: If an attacker slowly changes behavior over six months, can your system actually detect it?
* **Answer:** **Yes.** Experiment E3 proved a sustained $93.0\%$ detection rate across 6 months of poisoning by suppressing 19 poisoned updates.
* **Why Examiner Asks This:** Core paper validation check.
* **Key Point:** Validated in E3: sustained 93.0% detection across 6 months.

#### Q403: What happens if the attacker deliberately mimics their peer group?
* **Answer:** Mimicking peers means performing standard work tasks. Data exfiltration requires transmitting extra bytes, which departs from peer group norms.
* **Why Examiner Asks This:** Peer mimicry paradox.
* **Key Point:** Exfiltration ultimately requires transferring extra data bytes.

#### Q404: What happens if the attacker has no peers?
* **Answer:** The system falls back to departmental centroids $\mathbf{C}_D$ and relies more heavily on Stage 1 acceleration ($S_1$) and Stage 3 trend ($S_3$) checks.
* **Why Examiner Asks This:** Zero-peer edge case.
* **Key Point:** Fallback to department centroid + Stage 1 acceleration & Stage 3 trend.

#### Q405: Why should we believe that your selected 30-day baseline is optimal?
* **Answer:** Sensitivity trials across $W \in [7, 60]$ days showed $W=30$ achieved optimal balance between volatility ($W=7$) and inertia ($W=60$).
* **Why Examiner Asks This:** Baseline window sensitivity proof.
* **Key Point:** Sensitivity trials proved $W=30$ balances volatility and inertia.

#### Q406: Why should we believe that 7 days is the correct trend window?
* **Answer:** 7 days captures a full weekly business cycle while suppressing single-day noise without delaying threat escalation detection.
* **Why Examiner Asks This:** Trend window sensitivity proof.
* **Key Point:** Captures weekly business cycle without delaying alert response.

#### Q407: Why should we believe that 0.6 is the correct suspicion threshold?
* **Answer:** Grid search across $\tau \in [0.4, 0.8]$ proved $\tau=0.60$ minimizes False Suppression Rate ($4\%$) while maximizing poisoning defense ($93\%$).
* **Why Examiner Asks This:** Threshold optimization proof.
* **Key Point:** Grid search optimization minimizing FSR while maximizing defense.

#### Q408: Did you derive these values experimentally or choose them heuristically?
* **Answer:** Initial values were domain-heuristic; final parameters ($W=30, K=7, \tau=0.60$) were refined experimentally on the validation split.
* **Why Examiner Asks This:** Methodology rigor check.
* **Key Point:** Domain heuristics refined experimentally via validation grid search.

#### Q409: What happens if those parameters are changed?
* **Answer:** Lowering $\tau$ to $0.4$ increases false baseline freezes ($FSR \to 14\%$); raising $\tau$ to $0.8$ allows partial poisoning ($Detection \to 78\%$).
* **Why Examiner Asks This:** Parameter change impact check.
* **Key Point:** Sensitivity boundaries: lower $\tau \implies$ higher FSR; higher $\tau \implies$ poisoning leakage.

#### Q410: How sensitive is your system to parameter selection?
* **Answer:** Parameter sensitivity analysis shows stable defense within a $\pm 15\%$ tolerance band around optimal operational values.
* **Why Examiner Asks This:** Parameter stability margin.
* **Key Point:** Stable within $\pm 15\%$ operational tolerance band.

#### Q411: Can your research contribution be reproduced by another researcher?
* **Answer:** **Yes.** We provide complete reproducible scripts (`feature_engineer.py`, `governance.py`, `train_all.py`), exact seed definitions, and documented parameters on CMU CERT r5.2.
* **Why Examiner Asks This:** Scientific reproducibility check.
* **Key Point:** Fully reproducible via staged codebase scripts and fixed random seeds.

#### Q412: Can another researcher reproduce your results from your methodology?
* **Answer:** Yes, by applying our 4-stage governance algorithms and risk fusion equations to the publicly available CMU CERT r5.2 dataset.
* **Why Examiner Asks This:** Methodological completeness check.
* **Key Point:** Public CERT r5.2 dataset + documented mathematical equations.

#### Q413: What would happen if we gave your system a completely different organization's logs?
* **Answer:** The pipeline would ingest the logs, extract 44 daily features, calculate local peer centroids, and execute governance identically.
* **Why Examiner Asks This:** Generalization capability check.
* **Key Point:** Ingests new logs, extracts 44 features, and builds local peer centroids.

#### Q414: What is the one experiment you would perform next to strengthen this research?
* **Answer:** Executing a multi-year live enterprise field trial evaluating human SOC analyst Mean Time to Respond (MTTR) with and without our LLM explanations.
* **Why Examiner Asks This:** Vision for next research phase.
* **Key Point:** Live enterprise field trial measuring human SOC analyst MTTR reduction.

#### Q415: If you had to remove one component from your system, which one would you remove and why?
* **Answer:** The SVM baseline model. It serves as a classical benchmark reference, but XGBoost, Isolation Forest, and Governance handle core detection.
* **Why Examiner Asks This:** Component priority evaluation.
* **Key Point:** SVM baseline is a benchmark reference, not core to runtime detection.

#### Q416: If you had unlimited computational resources, what would you change?
* **Answer:** Train continuous graph neural networks (GNNs) over real-time event streams to discover dynamic informal peer collaboration clusters.
* **Why Examiner Asks This:** Research ambition check.
* **Key Point:** Dynamic Graph Neural Networks (GNNs) for informal peer discovery.

#### Q417: If you had no LLM available, how would you implement alert explanation?
* **Answer:** Using our deterministic local template engine (`build_fallback_explanation()`), which renders exact TreeSHAP attributions into structured text.
* **Why Examiner Asks This:** Fallback architecture validity.
* **Key Point:** Local TreeSHAP template engine (`build_fallback_explanation()`).

#### Q418: If XGBoost were removed, how would your system work?
* **Answer:** LightGBM or Random Forest would replace XGBoost as the supervised classifier, maintaining identical integration with Risk Fusion.
* **Why Examiner Asks This:** Modular classifier independence.
* **Key Point:** Modular replacement via LightGBM or Random Forest.

#### Q419: If SHAP were removed, how would you provide explainability?
* **Answer:** By displaying normalized feature deviation vectors ($\mathbf{x}_u - \mathbf{B}_u$) directly on radar charts in the user profile UI.
* **Why Examiner Asks This:** Alternative XAI visualization.
* **Key Point:** Feature deviation vectors ($\mathbf{x}_u - \mathbf{B}_u$) rendered on radar charts.

#### Q420: If Redis and Celery were removed, what would happen?
* **Answer:** Risk scoring would remain functional, but LLM calls and governance audits would run synchronously, increasing API response times to 5+ seconds.
* **Why Examiner Asks This:** Async infrastructure dependency check.
* **Key Point:** Functionality preserved; API response times increase to 5+ seconds.

#### Q421: If PostgreSQL were replaced with MongoDB, what would change?
* **Answer:** TreeSHAP JSON payloads would store natively as BSON documents, but relational foreign key constraints across alerts and verdicts would require application-level checks.
* **Why Examiner Asks This:** NoSQL architectural impact check.
* **Key Point:** Native BSON payload storage; relational integrity moves to application layer.

#### Q422: If you had to deploy this in a real SOC, what would you change first?
* **Answer:** Add live Kafka/Splunk log streaming connectors and integrate Active Directory LDAP synchronization for automatic role centroid updates.
* **Why Examiner Asks This:** Production readiness awareness.
* **Key Point:** Kafka/Splunk streaming ingestion + live Active Directory LDAP sync.

#### Q423: What is the difference between your research prototype and a production-grade UEBA platform?
* **Answer:** Our prototype uses static CERT log exports and local background queues. Production platforms require distributed cluster ingestion, multi-tenant RBAC, and HA database replication.
* **Why Examiner Asks This:** Prototype vs production distinction.
* **Key Point:** Static log exports vs distributed streaming, multi-tenancy, and HA replication.

#### Q424: What claim in your paper are you least confident about?
* **Answer:** The exact generalizability of suspicion threshold $\tau = 0.60$ to real enterprise networks without local dataset re-calibration.
* **Why Examiner Asks This:** Intellectual vulnerability test.
* **Key Point:** Generalizability of static threshold $\tau=0.60$ without local re-calibration.

#### Q425: What is the strongest criticism someone could make against your research?
* **Answer:** That the evaluation relies on synthetic CERT r5.2 logs rather than multi-year real-world enterprise SOC audit trails.
* **Why Examiner Asks This:** Anticipating reviewer objections.
* **Key Point:** Reliance on synthetic CERT benchmark vs real enterprise logs.

#### Q426: If another researcher says your method is just a combination of existing techniques, how will you defend the novelty?
* **Answer:** By pointing out that combining techniques to solve an unaddressed security vulnerability (**slow-escalation baseline poisoning**) through a novel 4-stage governance formulation *is* the research contribution.
* **Why Examiner Asks This:** Novelty defense against "combination of existing tools".
* **Key Point:** Novel integration + mathematical formulation targeting an unsolved vulnerability.

#### Q427: What part of your system would you publish independently as a research contribution?
* **Answer:** The **4-Stage Baseline Update Governance Engine** and its poisoning defense validation (Paper 1).
* **Why Examiner Asks This:** Independent research value check.
* **Key Point:** Contamination-resistant baseline governance framework (Paper 1).

#### Q428: What experiment would disprove your research hypothesis?
* **Answer:** An experiment where an ungoverned baseline sustains a $>90\%$ detection rate under 5%/month poisoning, or where our governed baseline drops below $50\%$ detection.
* **Why Examiner Asks This:** Falsifiability check (Popperian science).
* **Key Point:** Falsifiability: ungoverned baseline surviving poisoning or governance dropping below 50%.

#### Q429: What happens if your proposed governance mechanism performs worse than a static baseline?
* **Answer:** Experiments E2 and E3 prove governance maintains $93\%$ detection with $4\%$ FSR, whereas static baselines yield poor F1 ($0.62$) due to high false alarms on benign drift.
* **Why Examiner Asks This:** Static baseline empirical check.
* **Key Point:** Governed baseline achieves 93% detection vs static baseline F1 of 0.62.

#### Q430: Under what conditions would your proposed approach not be appropriate?
* **Answer:** In small organizations ($<5$ employees) without distinct job roles or peer groups, or in environments with zero historical telemetry for baseline bootstrapping.
* **Why Examiner Asks This:** Boundary conditions for applicability.
* **Key Point:** Micro-organizations lacking peer groups or initial baseline bootstrapping telemetry.

---

## MASTER MAPPING — 15 CORE DECISION CLUSTERS SUMMARY

```
+----------------------------------------------------------------------------------------------------+
| 15 CORE DECISION CLUSTERS (EXAMINER INTENT VS. BULLETPROOF DEFENSE SUMMARY)                        |
+----+-----------------------+-----------------------------------------------------------------------+
| #  | EXAMINER INTENT       | BULLETPROOF DEFENSE SUMMARY                                           |
+----+-----------------------+-----------------------------------------------------------------------+
| 1  | Model Selection       | XGBoost handles non-linear tabular features; SMOTE fixes 1-2% imbalance.|
| 2  | Alternatives          | SVM provides classical baseline; Isolation Forest catches zero-days.  |
| 3  | Explainability        | TreeSHAP provides game-theoretic consistency; LIME is unstable.       |
| 4  | Parameter Tuning      | W=30, K=7, tau=0.60 calibrated via validation split grid search.       |
| 5  | Risk Fusion           | Fuses supervised, unsupervised, and peer signals into continuous 0-100|
| 6  | Peer Anchors          | Role/dept peer centroids separate benign role drift from attack drift. |
| 7  | Dataset Choice        | CMU CERT r5.2 is standard 18-month benchmark with 6 threat scenarios. |
| 8  | Experimental Validity | Chronological 80/20 split prevents temporal data leakage.             |
| 9  | Imbalance Strategy    | SMOTE interpolated minority samples strictly on training partition.   |
| 10 | Architecture          | Modular monolith + Django REST + React 18 + Celery/Redis background queues|
| 11 | DB & Async Infrastructure| PostgreSQL guarantees ACID state; Redis/Celery prevents API freezing|
| 12 | Research Novelty      | 4-Stage Governance Engine defending against slow-escalation poisoning.|
| 13 | System Limitations    | Synthetic CERT data; peer group sparsity in small teams (<3 users).   |
| 14 | Failure Modes         | Fail-secure defaults: baseline updates freeze in quarantine on error. |
| 15 | Future Scope          | Mahalanobis distance, BOCPD changepoints, dynamic tau(t), GNN peers.  |
+----+-----------------------+-----------------------------------------------------------------------+
```

---
*End of Research-Paper Judge Cross-Question Bank (430 Master Defense Q&A).*
