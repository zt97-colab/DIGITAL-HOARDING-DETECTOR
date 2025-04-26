import os
import zipfile
import rarfile
import py7zr

# ======== SYSTEM SCANNER CONFIG ========

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
SPECIAL_EXTENSIONS = ['.zip', '.rar', '.7z']

NORMAL_FILES = []
NORMAL_FOLDERS = []
ARCHIVE_SUMMARY = []
TOTAL_FILES_IN_ARCHIVES = 0
TOTAL_FOLDERS_IN_ARCHIVES = 0
MAX_NESTING_DEPTH = 0

# ======== SCANNER FUNCTIONS ========

def scan_normal_filesystem(target_folder):
    for root, dirs, files in os.walk(target_folder):
        for dir in dirs:
            NORMAL_FOLDERS.append(os.path.join(root, dir))
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            if ext in SPECIAL_EXTENSIONS:
                scan_archive(file_path, 1)
            else:
                NORMAL_FILES.append(file_path)

def scan_archive(archive_path, current_level):
    global TOTAL_FILES_IN_ARCHIVES, TOTAL_FOLDERS_IN_ARCHIVES, MAX_NESTING_DEPTH

    try:
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as archive:
                for info in archive.infolist():
                    if info.is_dir():
                        TOTAL_FOLDERS_IN_ARCHIVES += 1
                    else:
                        TOTAL_FILES_IN_ARCHIVES += 1
                    nesting = info.filename.count('/')
                    MAX_NESTING_DEPTH = max(MAX_NESTING_DEPTH, current_level + nesting)
                ARCHIVE_SUMMARY.append(archive_path)

        elif archive_path.endswith('.rar'):
            with rarfile.RarFile(archive_path) as archive:
                for info in archive.infolist():
                    if info.isdir():
                        TOTAL_FOLDERS_IN_ARCHIVES += 1
                    else:
                        TOTAL_FILES_IN_ARCHIVES += 1
                    nesting = info.filename.count('/')
                    MAX_NESTING_DEPTH = max(MAX_NESTING_DEPTH, current_level + nesting)
                ARCHIVE_SUMMARY.append(archive_path)

        elif archive_path.endswith('.7z'):
            with py7zr.SevenZipFile(archive_path, mode='r') as archive:
                for info in archive.list():
                    if info.is_directory:
                        TOTAL_FOLDERS_IN_ARCHIVES += 1
                    else:
                        TOTAL_FILES_IN_ARCHIVES += 1
                    nesting = info.filename.count('/')
                    MAX_NESTING_DEPTH = max(MAX_NESTING_DEPTH, current_level + nesting)
                ARCHIVE_SUMMARY.append(archive_path)

    except Exception as e:
        print(f"⚠️ Skipping archive (could not open): {archive_path}")

# ======== PSYCHOLOGICAL QUIZ ========

def psychological_quiz():
    questions = [
        "Do you feel anxious deleting old files?",
        "Do you often save things 'just in case' you might need them later?",
        "Do you have multiple copies of the same document or picture?",
        "Is your desktop cluttered with many files and shortcuts?",
        "Do you find it hard to organize your folders?",
        "Have you ever bought extra storage because you ran out of space?",
        "Do you rarely clean or sort your Downloads folder?",
        "Do you keep old versions of files you don't use anymore?",
        "Do you feel overwhelmed when trying to clean your computer?",
        "Do you avoid deleting things even if you know they're not important?"
    ]

    score = 0
    print("\n=== PSYCHOLOGICAL QUIZ ===")
    print("Answer each question: (0 = Never, 1 = Sometimes, 2 = Always)\n")
    
    for i, question in enumerate(questions, start=1):
        while True:
            try:
                ans = int(input(f"Q{i}: {question} [0-2]: "))
                if ans in [0, 1, 2]:
                    score += ans
                    break
                else:
                    print("❌ Please enter 0, 1, or 2 only.")
            except:
                print("❌ Invalid input. Please enter 0, 1, or 2.")
    return score

# ======== FINAL RISK ANALYZER ========

def analyze_final(system_score, psychological_score):
    print("\n=== FINAL DIGITAL HOARDING RISK REPORT ===\n")

    # System Risk
    if system_score <= 1:
        system_risk = "Normal"
    elif system_score == 2:
        system_risk = "Borderline"
    else:
        system_risk = "Severe"

    # Psychological Risk
    if psychological_score <= 5:
        psych_risk = "Low Emotional Hoarding"
    elif psychological_score <= 12:
        psych_risk = "Medium Emotional Hoarding"
    else:
        psych_risk = "High Emotional Hoarding"

    # Combine
    if system_risk == "Severe" or psych_risk == "High Emotional Hoarding":
        final_risk = "🚨 Severe Digital Hoarder"
    elif system_risk == "Borderline" or psych_risk == "Medium Emotional Hoarding":
        final_risk = "⚠️ Borderline Digital Hoarder"
    else:
        final_risk = "✅ Normal User"

    # Print report
    print(f"🖥️ System Behavior Risk: {system_risk}")
    print(f"🧠 Psychological Behavior Risk: {psych_risk}")
    print(f"\n🎯 FINAL RISK LEVEL: {final_risk}\n")

    # Personalized Advice
    if final_risk == "✅ Normal User":
        print("✅ You have healthy digital habits. Keep organizing your files regularly!")
    elif final_risk == "⚠️ Borderline Digital Hoarder":
        print("⚠️ You are starting to accumulate too many files.\n- Clean up old files.\n- Organize folders.\n- Delete unused apps.\n- Backup important data.")
    else:
        print("🚨 Severe Digital Hoarding Detected!\n- Immediately delete duplicates.\n- Uninstall unused applications.\n- Backup and organize data.\n- Use tools like CCleaner, Gemini, fdupes.\n- Consider a fresh system reinstall if performance is very poor.")

# ======== MAIN PROGRAM ========

if __name__ == "__main__":
    print("🔎 SCANNING SYSTEM...\n")
    scan_normal_filesystem(DOWNLOADS_PATH)

    # Analyze system risk
    system_points = 0
    if len(NORMAL_FILES) > 50000:
        system_points += 1
    if len(NORMAL_FOLDERS) > 10000:
        system_points += 1
    if TOTAL_FILES_IN_ARCHIVES > 10000:
        system_points += 1
    if MAX_NESTING_DEPTH > 5:
        system_points += 1

    print("\n✅ SYSTEM SCAN COMPLETE!")
    print(f"Total Normal Files: {len(NORMAL_FILES)}")
    print(f"Total Normal Folders: {len(NORMAL_FOLDERS)}")
    print(f"Files Inside Archives: {TOTAL_FILES_IN_ARCHIVES}")
    print(f"Folders Inside Archives: {TOTAL_FOLDERS_IN_ARCHIVES}")
    print(f"Deepest Nesting Level: {MAX_NESTING_DEPTH}")

    # Take psychological quiz
    psych_score = psychological_quiz()

    # Final analysis
    analyze_final(system_points, psych_score)
