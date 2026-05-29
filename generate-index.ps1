# Delegates to Python version for proper UTF-8 handling
$scriptDir = Split-Path -Parent $PSCommandPath
& "C:\Python314\python.exe" (Join-Path $scriptDir "generate-index.py") @args
