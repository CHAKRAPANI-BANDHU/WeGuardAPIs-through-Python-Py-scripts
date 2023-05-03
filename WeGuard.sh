#!/usr/bin/env bash/bin/sh

FILE="Report_$(date +%Y%m%d_%H%M%S).html"
echo $FILE
python3 -m pytest --capture=sys --html=$FILE