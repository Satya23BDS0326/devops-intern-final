#!/bin/bash
# sysinfo.sh - Prints basic system information
# Usage: ./sysinfo.sh

echo "===== SYSTEM INFO ====="

echo ""
echo "--- Current User ---"
whoami

echo ""
echo "--- Current Date ---"
date

echo ""
echo "--- Disk Usage ---"
df -h

echo ""
echo "========================"
