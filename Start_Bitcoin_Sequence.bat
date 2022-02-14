@Echo off
title Bitcoin_sequence_Divison.py
Pushd "%~dp0"
pip install alive_progress
:loop
python Bitcoin_sequence_Divison.py
goto loop
