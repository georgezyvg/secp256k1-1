@Echo off
title HASH160_sequence.py
Pushd "%~dp0"
:loop
python HASH160_sequence.py
goto loop