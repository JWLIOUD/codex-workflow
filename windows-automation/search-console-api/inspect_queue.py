#!/usr/bin/env python3
"""Inspect the first actionable Search Console queue URL.

This script intentionally does not request indexing. It uses the official
Search Console URL Inspection API, which reports indexed status only.
"""

from __future__ import annotations

import datetime as dt
import os
import re
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE_URL = "sc-domain:yuchienpsy.com"
ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "WorkFlow" / "project" / "YucheinHomePage" / "docs" / "project"
QUEUE = PROJECT / "search-console-indexing-queue.md"


def credentials() -> Credentials:
    client_secret = os.environ.get("GSC_OAUTH_CLIENT_SECRET")
    token_path = os.environ.get("GSC_TOKEN_PATH")
    if not client_secret or not token_path:
        raise SystemExit("Set GSC_OAUTH_CLIENT_SECRET and GSC_TOKEN_PATH before running.")

    token = Path(token_path)
    if token.exists():
        return Credentials.from_authorized_user_file(str(token), SCOPES)

    flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
    creds = flow.run_local_server(port=0)
    token.parent.mkdir(parents=True, exist_ok=True)
    token.write_text(creds.to_json(), encoding="utf-8")
    return creds


def first_actionable_url() -> str:
    pattern = re.compile(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(pending-inspection|quota-blocked)\s*\|")
    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)
        if match:
            return match.group(1)
    raise SystemExit("No pending-inspection or quota-blocked URL found.")


def main() -> None:
    url = first_actionable_url()
    service = build("searchconsole", "v1", credentials=credentials())
    result = service.urlInspection().index().inspect(
        body={
            "inspectionUrl": url,
            "siteUrl": SITE_URL,
            "languageCode": "zh-TW",
        }
    ).execute()

    inspection = result.get("inspectionResult", {})
    index_status = inspection.get("indexStatusResult", {})
    verdict = index_status.get("verdict", "UNKNOWN")
    coverage = index_status.get("coverageState", "UNKNOWN")
    robots = index_status.get("robotsTxtState", "UNKNOWN")
    indexing = index_status.get("indexingState", "UNKNOWN")
    canonical = index_status.get("googleCanonical", "")
    checked_at = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %z")

    print(f"### Search Console API indexed-status check: {checked_at}")
    print()
    print("- Executor: Search Console API monitor")
    print(f"- Property: `{SITE_URL}`")
    print(f"- URL inspected: `{url}`")
    print(f"- API verdict: `{verdict}`")
    print(f"- Coverage state: `{coverage}`")
    print(f"- Robots state: `{robots}`")
    print(f"- Indexing state: `{indexing}`")
    print(f"- Google canonical: `{canonical}`")
    print("- Action: API monitor only; no Request indexing action is possible through this API.")
    print("- Queue update: review result and update queue manually or by a follow-up script.")


if __name__ == "__main__":
    main()
