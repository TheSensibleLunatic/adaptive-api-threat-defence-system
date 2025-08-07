
# Adaptive API Threat Defense System

<p align="center">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

<p align="center">
  A security system that proactively hunts for malicious intent within API traffic by analyzing behavioral patterns, neutralizing sophisticated attacks that traditional security models are blind to.
</p>

---

## 💡 The Problem Statement

I was reading a technical breakdown of a recent, high-profile data breach. What struck me was that the attackers didn't use a brute-force attack; they were much smarter. They used legitimate API keys and scraped data very slowly over several weeks, perfectly mimicking normal user traffic. Their activity never triggered any of the company's standard alarms because their request volume was always below the security thresholds. It made me realize that traditional security, which often just counts requests, is effectively blind to these modern, 'low-and-slow' attacks. That's the problem I wanted to solve.

## 🚀 The Solution: A Technical Deep-Dive

This led me to architect an **Adaptive API Threat Defense System**. The system is designed as a high-performance, non-blocking proxy, which I wrote in **Go** for its concurrency capabilities. This proxy sits in front of the main application and asynchronously forwards sanitized request logs—including endpoint, HTTP method, user-agent, IP, and key-specific metadata—to a processing pipeline.

For the core logic, I used Python. For each API key, the system constructs a multi-dimensional behavioral profile. This isn't just a simple counter; it includes **histograms of endpoint frequency**, **parameter value distributions**, and **time-of-day access patterns**. These profiles are stored in a **Redis** cache for low-latency retrieval.

The real-time detection is handled by an **Isolation Forest algorithm** from Scikit-learn. I chose this model because it's highly efficient at identifying outliers in high-dimensional data. Each incoming request's features are compared against the established profile for that key. If the model returns a high anomaly score, it signifies a significant deviation from normal behavior. An anomalous event triggers a webhook that can integrate with a SIEM platform like Splunk or send an immediate alert to a SecOps team. This architecture allows the system to detect malicious intent based on context, rather than relying on crude volumetric thresholds.

## 🛠️ Tech Stack

- **Primary Language:** Go (for proxy), Python (for ML analysis)
- **Machine Learning:** Scikit-learn (Isolation Forest), Pandas
- **Infrastructure:** Docker, Redis
- **Core Concepts:** API Security, Anomaly Detection, Behavioral Analysis, Microservices

## ⚙️ Getting Started

### Prerequisites

Ensure you have Go, Python 3.8+, and Docker installed.

```bash
pip install -r requirements.txt
```

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[YourUsername]/adaptive-api-threat-defense-system.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd adaptive-api-threat-defense-system
    ```
3.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
