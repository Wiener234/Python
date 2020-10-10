@echo off

set fn=%1
set flag=%2

If "%1"==""(
    echo "error"
) else (
    gitcreate.py %fn%