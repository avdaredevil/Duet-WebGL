param([Switch]$OnlyImports)
cc php,bower,Node-Extensions
function global:server {start cmd "/c cd package& php -S localhost:8080"}
function global:game {nw .}
if ($OnlyImports) {exit}
start gulp
Write-AP "xns![Waiting]"
do {sleep 1} while ((test-path "./package/main.html") -and (New-TimeSpan (ls .\package\main.html | % LastWriteTime) (Get-Date) | % TotalMinutes) -gt 5);Write-AP "ns+ Gulp Complete...";server
