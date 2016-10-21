param([Switch]$OnlyImports)
cc php,bower,Node-Extensions
function global:server {start cmd "/c cd game& php -S localhost:8080"}
function global:game {nw .}
if ($OnlyImports) {exit}
start gulp
$GameSrc = Path-Join . "game\index.html"
Write-AP "xns![Waiting]"
do {sleep 1} while ((test-path $GameSrc) -and (New-TimeSpan (ls $GameSrc | % LastWriteTime) (Get-Date) | % TotalMinutes) -gt 5);Write-AP "ns+ Gulp Complete...";server
