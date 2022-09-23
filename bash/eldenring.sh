#!/bin/bash

echo "You died!"

beast=$(( $RANDOM % 2 ))

echo "Your first beast approaches. Prepare to battle. Pick a number between 0-1 (0/1)"

read tarnished

if [[ $beast == $tarnished ]]; then
	echo "Beast VANQUISHED!! Congrats fellow tarnished"
else 
	echo "you Died"
	exit 1
fi

sleep 3

echo "Your first beast approaches. Prepare to battle. Pick a number between 0-10 (0-10)"

read tarnished

beast=$(( $RANDOM % 10))

if [[ $beast == $tarnished || $tarnished == "coffee"  ]]; then
	echo "Beast VANQUISHED!! Congrats fellow tarnished"
else
	echo "you Died"
fi
