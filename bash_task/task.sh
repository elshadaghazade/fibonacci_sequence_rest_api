#!/bin/bash

cat /etc/passwd | grep -v '.*[/bin/false|/bin/nologin]$' | awk -F':' '{print $7 " " $1}'