#!/bin/bash
sudo mongod --configsvr --dbpath /data/db --port 30001 --replSet r1 &
sudo mongos --configdb "r1/localhost:30001" --port 40001 &
sudo mongod --shardsvr --port 50001 --dbpath /data/sh1 --replSet shard1Repl &
sudo mongod --port 60001 --dbpath /data/repl1 --replSet shard1Repl &
sudo mongod --shardsvr --port 50002 --dbpath /data/sh2 -replSet shard2Repl &
sudo mongod --port 60002 --dbpath /data/repl2 --replSet shard2Repl &