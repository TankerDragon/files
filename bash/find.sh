#!/bin/bash

for i in {200..256}
do
	#echo "Pinging number $i"
	out=$(ping -c 1 -W 1 142.250.178.$i)
	echo "number $i"
	if [[ $out == *"statistics"* ]]; then
		echo "server is up"
	else
		echo "no $out"
	fi
done


#if [[ $output == *"fin"* ]]; then
#	echo "yes"
#fi
#	
#echo "$output"
