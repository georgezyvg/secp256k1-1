@Echo off
title HASH160_random.py
Pushd "%~dp0"
:loop
python HASH160_random.py
goto loop