def log_event(message):
    with open("fim_log.txt", "a") as log:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")
import hashlib
import os
import time

# Configuration
TARGET_FOLDER = "./my_secure_files"
BASELINE_FILE = "baseline.txt"

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None

def create_baseline():
    print(f"[*] Scanning {TARGET_FOLDER} and creating baseline...")
    with open(BASELINE_FILE, "w") as f:
        for root, dirs, files in os.walk(TARGET_FOLDER):
            for file in files:
                path = os.path.join(root, file)
                hash_val = calculate_sha256(path)
                if hash_val:
                    f.write(f"{path}|{hash_val}\n")
    print("[+] Baseline saved to baseline.txt.")

def monitor():
    if not os.path.exists(BASELINE_FILE):
        print("[!] Error: No baseline found. Run Option 1 first.")
        return

    # Load baseline
    baseline_dict = {}
    with open(BASELINE_FILE, "r") as f:
        for line in f:
            path, hash_val = line.strip().split("|")
            baseline_dict[path] = hash_val

    print("[*] Monitoring ACTIVE... (Press Ctrl+C to stop)")
    try:
        while True:
            # Check for changes and new files
            current_files = []
            for root, dirs, files in os.walk(TARGET_FOLDER):
                for file in files:
                    path = os.path.join(root, file)
                    current_files.append(path)
                    
                    # 1. Check for modified files
                    if path in baseline_dict:
                        current_hash = calculate_sha256(path)
                        if current_hash != baseline_dict[path]:
                            print(f"\n[!!!] ALERT: FILE MODIFIED: {path}")
                            # Update baseline so we don't spam the alert
                            baseline_dict[path] = current_hash 
                    
                    # 2. Check for new files
                    else:
                        print(f"\n[!] ALERT: NEW FILE CREATED: {path}")
                        baseline_dict[path] = calculate_sha256(path)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")

if __name__ == "__main__":
    print("--- Kali Linux FIM Tool ---")
    print("1. Create Baseline\n2. Start Monitoring")
    choice = input("Select: ")
    if choice == "1":
        create_baseline()
    elif choice == "2":
        monitor()
