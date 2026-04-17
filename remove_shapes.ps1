$path = "d:\New folder\index.html"
$content = Get-Content -Path $path -Raw
$content = $content -replace "(?sm)\s*<div class=`"deck-shape ds-\d`"></div>", ""
Set-Content -Path $path -Value $content -Encoding UTF8
Write-Host "Removed shapes"
