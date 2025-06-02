import requests
from urllib.parse import urljoin

def load_paths(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]

def scan_sensitive_paths(base_url, path_list):
    found = []
    for path in path_list:
        full_url = urljoin(base_url, path)
        try:
            res = requests.get(full_url, timeout=5)
            if res.status_code == 200 and "not found" not in res.text.lower():
                found.append((full_url, res.status_code))
        except:
            continue
    return found
