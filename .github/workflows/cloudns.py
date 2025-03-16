name: cloudns登录

on:
  schedule:
    # 每天凌晨 2 点运行（UTC 时间）
    - cron: '0 2 * * *'
  workflow_dispatch:  # 允许手动触发

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run main script
        env:
          CLOUDNS_API_ID: ${{ secrets.CLOUDNS_API_ID }}
          CLOUDNS_API_PASSWORD: ${{ secrets.CLOUDNS_API_PASSWORD }}
          TG_BOT_TOKEN: ${{ secrets.TG_BOT_TOKEN }}
          TG_USER_ID: ${{ secrets.TG_USER_ID }}
        run: |
          python main.py
