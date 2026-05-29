param(
    [string]$SourceDir = (Split-Path -Parent $PSCommandPath),
    [string]$OutputFile = "index.json"
)

$chapters = Get-ChildItem -LiteralPath $SourceDir -Filter "*.md" | Where-Object { $_.Name -ne "README.md" -and $_.Name -ne $OutputFile -and $_.BaseName -match '^\d{2}' } | Sort-Object Name

$result = @()

foreach ($file in $chapters) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    $lines = $content -split "`n"

    $title = ""
    $description = ""
    $warnings = @()
    $currentWarning = ""
    $currentBullets = @()
    $inWarning = $false

    foreach ($line in $lines) {
        $trimmed = $line.Trim()

        # Extract chapter subtitle (## heading)
        if ($trimmed -match "^##\s+(.+)$") {
            $title = $matches[1]
        }

        # Detect warning start: **BEFORE YOU ...**
        if ($trimmed -match "^\*\*(BEFORE\s+.+)\*\*\.\.\.$") {
            if ($inWarning -and $currentWarning) {
                $warnings += @{
                    title = $currentWarning
                    bullets = $currentBullets
                }
            }
            $currentWarning = $matches[1]
            $currentBullets = @()
            $inWarning = $true
        }
        elseif ($trimmed -match "^\*\*(BEFORE\s+.+)\*\*$") {
            if ($inWarning -and $currentWarning) {
                $warnings += @{
                    title = $currentWarning
                    bullets = $currentBullets
                }
            }
            $currentWarning = $matches[1]
            $currentBullets = @()
            $inWarning = $true
        }
        # Extract bullet points
        elseif ($trimmed -match "^-\s+(.+)$" -and $inWarning) {
            $currentBullets += $matches[1]
        }
        # Extract note as last bullet
        elseif ($trimmed -match "^\*Note:\s+(.+)\*$" -and $inWarning) {
            $currentBullets += "Note: $($matches[1])"
        }
    }

    # Capture last warning
    if ($inWarning -and $currentWarning) {
        $warnings += @{
            title = $currentWarning
            bullets = $currentBullets
        }
    }

    # Extract brief description from first line after subtitle
    $descLines = $lines | Where-Object { $_.Trim() -ne "" -and $_ -notmatch "^(⚠️|#|\*Note:|---)" }
    $description = if ($title -match "^(.+)\s+[&&].+") { $matches[1] } else { $title }

    $chapterNum = [int]($file.BaseName -replace '^(\d+).*', '$1')

    $result += @{
        id = $file.BaseName
        number = $chapterNum
        file = $file.Name
        title = $title
        description = $description
        warningCount = $warnings.Count
        totalBullets = ($warnings | ForEach-Object { $_.bullets.Count }) | Measure-Object -Sum | Select-Object -ExpandProperty Sum
        warnings = $warnings
    }
}

$result | ConvertTo-Json -Depth 5 | Out-File -LiteralPath (Join-Path -Path $SourceDir -ChildPath $OutputFile) -Encoding utf8

$totalWarnings = ($result | ForEach-Object { $_.warningCount }) | Measure-Object -Sum | Select-Object -ExpandProperty Sum
Write-Host "Generated index.json with $($result.Count) chapters, $totalWarnings warnings"
