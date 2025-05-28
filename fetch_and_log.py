name: Auto Fetch Weather Data

on:
  schedule:
    - cron: '*/5 * * * *'
  workflow_dispatch:

jobs:
  fetch-data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x

      - name: Install requests
        run: pip install requests

      - name: Run fetch script
        run: python fetch_and_log.py

      - name: Commit changes
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add data/history.json
          git commit -m "Auto-update data" || echo "No changes"
          git push
