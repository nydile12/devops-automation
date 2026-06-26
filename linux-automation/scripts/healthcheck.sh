#!/bin/bash
echo "=============================="
echo "System Health Check"
echo "=============================="

echo ""
echo "Disk space"
df -h | awk 'NR>1{print "Used:"$3" |Free:"$4" |Usage:"$5}'

echo ""
echo "=============================="
echo "Memory Usage"
free -m | awk 'NR>1{print "Used:" $2 "MB | Free:" $3 "MB"}'

echo ""
echo "=============================="
echo " Top 5 processes"
ps aux --sort=-%cpu | head -6 | awk '{print $1, $2, $3"%", $11}'


echo ""
echo "=============================="
echo "Network Ports in Use"
ss -tulpn | grep LISTEN

echo ""
echo "============================="
echo "    CHECK COMPLETE"
echo "============================="
