cc php,bower,Node-Extensions
function global:server {start cmd "/c cd package& php -S localhost:8080"}
function global:game {nw .}
start gulp
Write-AP "xns![Waiting]"
do {sleep 1} while (test-path "$PSScriptRoot/package");Write-AP "ns+ Gulp Complete...";server