@Echo off
title HASH160_sequence.py
Pushd "%~dp0"
pip install alive_progress
:loop
python HASH160_sequence.py
goto loop
