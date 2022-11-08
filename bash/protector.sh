#!/bin/bash

print_name() {
	neme=$1
	sleep 3s
	echo "My name is $neme"
}

echo "calling the function for the first time"
print_name alita &
echo "calling the function for the second time"
print_name molita &
