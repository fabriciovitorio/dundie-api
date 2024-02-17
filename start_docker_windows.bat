@echo off
setlocal
set "CURRENT_DIR=%cd%"
docker run --rm -it -v "%CURRENT_DIR%":/home/app/api -p 8000:8000 dundie