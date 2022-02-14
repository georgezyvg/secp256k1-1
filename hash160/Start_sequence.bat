@Echo off
title HASH160_sequence_Divison.py
Pushd "%~dp0"
pip install alive_progress
:loop
python HASH160_sequence_Divison.py
goto loop
