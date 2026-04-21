# COMP2152 — Term Project: CTF Bug Bounty

## Team Name
COMP2152-JamshaidMirpour

## Team Members

| Member | Vulnerability Found | Branch Name |
|--------|-------------------|-------------|
| Jamshaid Mirpour | Exposed API keys allow unauthorized token verification | jamshaid_backup_exposure |

## Videos

Each team member records a short video (max 3 minutes) explaining their vulnerability. Add your YouTube links below:

- Jamshaid Mirpour: https://youtu.be/yf6GgpB-3t4

## Target

- Server: `0x10.cloud` and its subdomains
- Submission: http://submit.0x10.cloud
- Leaderboard: http://ranking.0x10.cloud

## Important: Rate Limit

The server allows **10 requests per second** per IP address. If you send requests too fast, you will get blocked (HTTP 429). Add a small delay between requests:

```python
import time
time.sleep(0.15)  # wait 150ms between requests

```
## Getting Started

1. Look at the three example scripts:
   - `example_http_check.py` — checks if a site uses HTTPS (uses `urllib`)
   - `example_port_check.py` — checks if a port is open (uses `socket`)
   - `example_header_check.py` — reads HTTP response headers for info leaks (uses `urllib`)
2. Run all examples: `python3 main.py`
3. Create your own branch: `git checkout -b your_vuln_name`
4. Write a Python script that finds and demonstrates a vulnerability
5. Submit your finding at http://submit.0x10.cloud
6. Merge your branch into master when done

## Rules

- **Python standard library only** — `socket`, `urllib`, `ssl`, `json`, `base64`, `time`. No pip packages.
- **Only scan `*.0x10.cloud`** — do not scan any other domain.
- **Respect the rate limit** — 10 requests/second max.

## Final Finding

- **Vulnerability:** Exposed API keys allow unauthorized token verification
- **Subdomain:** `api.0x10.cloud`
- **Summary:** The `/users` endpoint exposed API keys for different users without authentication. Those leaked keys were then accepted as Bearer tokens by `/auth/verify`, which returned `{"message":"Token accepted","valid":true}`.
- **Status:** Resubmitted through `submit.0x10.cloud` and awaiting review

## Repository Files

- `main.py`
- `example_http_check.py`
- `example_port_check.py`
- `example_header_check.py`
- `verify_auth_key.py`
- `README.md`
- `.gitignore`
- `AI Usage Declaration - Jamshaid Mirpour.docx`