#!/usr/bin/env python3
"""Submit yuchienpsy.com sitemap through the Search Console Sitemaps API."""

from __future__ import annotations

import os
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/webmasters"]
SITE_URL = "sc-domain:yuchienpsy.com"
SITEMAP_URL = "https://yuchienpsy.com/sitemap.xml"


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


def main() -> None:
    service = build("webmasters", "v3", credentials=credentials())
    service.sitemaps().submit(
        siteUrl=SITE_URL,
        feedpath=SITEMAP_URL,
    ).execute()
    print(f"Submitted sitemap: {SITEMAP_URL}")


if __name__ == "__main__":
    main()
