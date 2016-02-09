#!/bin/bash
declare -i count=1
for url in $(cat listOfEpisodes); do
	curl -o $count "$url"
	let "count+=1"
done
