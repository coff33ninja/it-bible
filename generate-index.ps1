# Delegates to Python version for proper UTF-8 handling
$scriptDir = Split-Path -Parent $PSCommandPath
$py = if (Get-Command "python" -ErrorAction SilentlyContinue) { "python" }
      elseif (Get-Command "py" -ErrorAction SilentlyContinue) { "py" }
      else { throw "Python not found. Install Python from python.org" }
& $py (Join-Path $scriptDir "generate-index.py") @args
