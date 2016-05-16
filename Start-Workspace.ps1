function global:server {start cmd "/c cd package& php -S localhost:8080"}
start gulp
Write-AP "xns![Waiting]"
sleep 10;Write-AP "ns+ Gulp Complete...";server