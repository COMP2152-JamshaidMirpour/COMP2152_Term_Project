# COMP2152 — Term Project: CTF Bug Bounty

## Team Name
SOLO-CTF-Research

## Team Members

| Member | Vulnerability Found | Branch Name |
|--------|-------------------|-------------|
| Jamshaid Mirpour | Open directory listing exposes backup files and sensitive credentials | jamshaid_backup_exposure |

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