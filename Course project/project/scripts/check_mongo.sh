#!/bin/bash
pgrep mongo
sudo lsof -i -P -n | grep LISTEN