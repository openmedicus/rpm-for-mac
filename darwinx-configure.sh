#!/bin/sh -
eval "`rpm --eval "%{_darwinx_configure}"`" '"$@"'
