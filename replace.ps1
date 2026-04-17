$lines = Get-Content -Path "d:\New folder\index.html" -Encoding UTF8
$startIdx = -1
$endIdx = -1
for ($i=0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match "/\* Per Card Styles \*/") {
        $startIdx = $i
    }
    if ($lines[$i] -match "/\* Deck Card Layout \*/" -and $startIdx -ne -1) {
        $endIdx = $i
        break
    }
}

if ($startIdx -ne -1 -and $endIdx -ne -1) {
    $before = $lines[0..($startIdx-1)]
    $after = $lines[($endIdx+1)..($lines.Length-1)]
    $insert = @"
        /* Per Card Styles (Images) */
        .dc-1 { background-image: url('./1.jpg'); }
        .dc-2 { background-image: url('./2.jpg'); }
        .dc-3 { background-image: url('./3.jpg'); }
        .dc-4 { background-image: url('./4.jpg'); }
        .dc-5 { background-image: url('./5.jpg'); }
        .dc-6 { background-image: url('./6.jpg'); }

        .no-image.dc-1 { background-image: linear-gradient(145deg, #1a3329 0%, #0d1f18 40%, #2d5244 100%) !important; }
        .no-image.dc-2 { background-image: linear-gradient(145deg, #0f1a16 0%, #1e3d30 50%, #3E5E51 100%) !important; }
        .no-image.dc-3 { background-image: linear-gradient(145deg, #080f0c 0%, #1a3329 60%, #DCD0C4 100%) !important; }
        .no-image.dc-4 { background-image: linear-gradient(145deg, #1C2B25 0%, #3E5E51 70%, #B8D4C0 100%) !important; }
        .no-image.dc-5 { background-image: linear-gradient(145deg, #0a0f0c 0%, #162019 40%, #4A7A68 100%) !important; }
        .no-image.dc-6 { background-image: linear-gradient(145deg, #0d1a15 0%, #1a3329 50%, #3E5E51 100%) !important; }

        /* Deck Card Layout */
"@
    $newLines = $before -join "`n"
    $newLines += "`n" + $insert + "`n"
    $newLines += $after -join "`n"
    Set-Content -Path "d:\New folder\index.html" -Value $newLines -Encoding UTF8
    Write-Host "Success"
} else {
    Write-Host "Failed to find blocks"
}
