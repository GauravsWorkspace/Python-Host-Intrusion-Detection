# 🛡️ Python-HIDS: File Integrity Monitor (FIM)

A lightweight, high-performance **Host Intrusion Detection System (HIDS)** developed in Python. This tool ensures data integrity by monitoring sensitive directories for unauthorized modifications using cryptographic hashing.

![FIM Demo](./Screenshot_2026-04-05_20_41_35.jpg)

## 🌟 Key Features
- **SHA-256 Integrity Verification:** Generates unique digital fingerprints for every file to detect even a single-character change.
- **Real-Time Monitoring:** Implements a continuous polling loop to catch threats the moment they happen.
- **Full Lifecycle Detection:** Tracks file **Creations**, **Modifications**, and **Deletions**.
- **Automated Logging:** Generates a `security_events.log` file for forensic auditing and incident response.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Environment:** Kali Linux / Linux
- **Core Modules:** `hashlib` (Security), `os` (System), `time` (Monitoring), `datetime` (Forensics)

## 🚀 How It Works
1. **Baseline Creation:** The script scans the target folder and creates a "Golden Image" hash of all files.
2. **Continuous Comparison:** It periodically re-scans the folder and compares the current hashes against the baseline.
3. **Alerting:** If a mismatch is found (indicating a hack or unauthorized change), a high-priority alert is triggered.

## 📂 Project Structure
- `fim.py`: The core detection engine.
- `baseline.txt`: The stored digital signatures of protected files.
- `security_events.log`: The historical record of all detected security incidents.
- `my_secure_files/`: The target directory protected by the HIDS.

## 📝 Use Case
This project simulates the core functionality of enterprise-grade security tools like **Tripwire** or **Wazuh**. It is ideal for protecting configuration files (`/etc/`), web server directories, or sensitive database exports from tampering.

---
**Developed by [Your Name]** *MCA Final Year Student | Aspiring SOC Analyst*
