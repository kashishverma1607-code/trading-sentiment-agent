@echo off
cd /d "D:\Kashish\trading-sentiment-agent"
"D:\Kashish\trading-sentiment-agent\venv\Scripts\python.exe" "D:\Kashish\trading-sentiment-agent\run_automated.py" >> "D:\Kashish\trading-sentiment-agent\logs\scheduled_run.log" 2>&1
