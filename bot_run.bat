@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5450702099:AAFvGq4Awgd5htX2amk5h8umgX-sl3lzWp4

python bot_telegram.py

pause