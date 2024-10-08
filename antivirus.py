import os

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning: {file_path}")
            scan_file(file_path)

def scan_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()

            if b"malicious_code_signature" in content:
                print(f"Virus found in: {file_path}")
    except:
        print(f"Could not scan: {file_path}")

scan_directory("C:/")
