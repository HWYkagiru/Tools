@echo off
powershell -Command "Invoke-WebRequest -Uri https://raw.githubusercontent.com/HWYkagiru/Tools/main/Servercloner_bot.py -OutFile Servercloner_bot.py"
python Servercloner_bot.py
pause
