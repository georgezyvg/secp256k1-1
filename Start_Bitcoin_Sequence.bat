@Echo off
title Bitcoin_sequence.py
Pushd "%~dp0"
pip install alive_progress
:loop
python Bitcoin_sequence.py
goto loop
