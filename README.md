# Adaptive UEBA — AI-Powered Insider Threat & Baseline Poisoning Defense System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2%20LTS-green.svg)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-Academic-orange.svg)]()

> An end-to-end, contamination-resistant **User and Entity Behavior Analytics (UEBA)** platform engineered to detect insider threats and prevent **slow-escalation baseline poisoning attacks**. Combines hybrid machine learning, post-hoc SHAP explainability, evidence-bounded LLM triage, and a 4-stage baseline governance engine.

---

## 📌 Executive Summary (For Hiring Managers & Recruiters)

Traditional adaptive UEBA baselines update continuously, making them vulnerable to **slow-escalation poisoning**: an attacker who gradually increments malicious activity by ~5% per month tricks standard ML models into absorbing attacks as "new normal." In ungoverned systems, detection rates plummet from **94% down to 22%** within 6 months.

This project introduces a **4-stage contamination-resistant baseline governance engine** sitting on top of a hybrid ML detection pipeline trained on the 15+ GB **CMU CERT Insider Threat Dataset (r5.2)**.

### Key Metrics & Measurable Achievements
* 🎯 **0.9782 AUC & 0.9412 F1-Score:** Outperforms standalone XGBoost (0.9415 AUC) and baseline SVM (0.8842 AUC).
* 🛡️ **93% Threat Detection Preservation:** Maintains ~93% detection rate under 6-month slow-escalation poisoning attacks (where standard baselines fail completely).
* ⚖️ **94.0% Drift Classification Accuracy:** Successfully distinguishes legitimate organizational role shifts from malicious unilateral drift with only a **4.0% false suppression rate**.
* 🧠 **95.6% Explanation Faithfulness:** Evidence-bounded Claude LLM alert explanations evaluated via FaithLens rubric (97.5% factuality, zero hallucinations).
* ⚡ **< 2s UI Load Time:** Decoupled Celery + Redis task queue ensures async non-blocking LLM triage while maintaining fast dashboard performance.

---

## 🏗️ System Architecture

The application is built using a decoupled 5-layer modular architecture:

```mermaid
flowchart TD
    subgraph Data_Layer ["1. Data Layer"]
        A[CMU CERT r5.2 Raw CSVs] --> B[cert_ingestor.py]
        B --> C[cleaner.py & feature_engineer.py]
        C --> D[(40+ Daily User-Feature Vectors)]
    end

    subgraph Intelligence_Layer ["2. Intelligence Layer"]
        D --> E[XGBoost + SMOTE]
        D --> F[Isolation Forest]
        D --> G[SVM Baseline]
        E --> H[SHAP Explainer]
        E & F & G & H --> I[Risk Fusion Engine]
        I --> J[4-Stage Governance Engine]
    end

    subgraph Backend_Layer ["3. Backend & Async Layer"]
        J --> K[Django REST Framework API]
        K <--> L[(PostgreSQL / SQLite)]
        K --> M[Celery 5.3 Worker]
        M <--> N[(Redis 7 Queue)]
        M <--> O[Anthropic Claude LLM API]
    end

    subgraph Presentation_Layer ["4. Presentation Layer"]
        K <--> P[React 18 Dashboard]
        P --> Q[Risk Leaderboard]
        P --> R[User Profile & 30-Day History]
        P --> S[SHAP Feature Breakdown]
        P --> T[AI Analyst Chatbot Panel]
    end
