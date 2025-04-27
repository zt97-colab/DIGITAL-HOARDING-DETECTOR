# Digital Hoarding Detector 🔍🧹

**A smart tool that detects digital hoarding behavior based on real system analysis and psychological profiling.**  
Built with Python — combining file system scanning and emotional behavior analysis to help users declutter and optimize their devices.

---

## 🚀 Project Overview

Millions of users unknowingly hoard digital files, causing system slowdowns, disorganization, and data loss risk.  
This project automatically analyzes a user's system (file counts, folder structures, archive depth) and combines it with a psychological quiz to accurately detect digital hoarding tendencies.

**Final Output:**  
- Detects risk level (Normal, Borderline Hoarder, Severe Hoarder)
- Provides actionable cleaning recommendations
- Suggests real-world tools to help users clean their system

---

## 🧠 Features

- 📂 Deep file system scanning (including inside `.zip`, `.rar`, `.7z` archives)
- 🏠 Recursively counts files, folders, subfolders, special folders
- 🧹 Psychological 10-question MCQ quiz to assess emotional attachment to digital clutter
- 🧠 Combines technical and emotional behavior for final risk diagnosis
- 🎯 Personalized cleaning and optimization advice
- 🖥️ Designed for Windows, Mac, and Linux users

---

## 🛠️ Technologies Used

- Python 3
- `os`, `zipfile` (standard libraries)
- `rarfile` (for RAR archive reading)
- `py7zr` (for 7z archive reading)
- Git, GitHub, VS Code

---

## 📥 How to Install

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DIGITAL-HOARDING-DETECTOR.git
cd DIGITAL-HOARDING-DETECTOR

2. Install dependencies:

pip install rarfile py7zr

3. Run the project:

python digital_hoarding_detector.py


## 📸 Screenshots

### 🔍 System Scan Example
![System Scan](screenshots/system_scan.png)

### 🧠 Psychological Quiz Example
![Psych Quiz](screenshots/quiz.png)

### 🎯 Final Risk Report Example
![Final Report](screenshots/system_scan.png)


📈 Future Improvements

Add a full GUI (Graphical User Interface) for non-technical users

Generate downloadable reports (PDF/HTML)

Extend archive support to additional formats (e.g., tar.gz)

Provide automatic smart cleanup actions (detect and remove unnecessary files safely)

Add Disk Usage Risk Detection (coming soon)


⭐ Star This Project

If you found this tool helpful, please consider giving it a ⭐ on GitHub to support the project!