#!/usr/bin/env bash

read -a arr
count=0
for elem in ${arr[@]}
do
  count=$((count+${elem#-}))
done
echo $count
