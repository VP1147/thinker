#! /bin/bash

# SPEED=$(find /sys/devices/platform/ -name speed)
# SENS=$(find /sys/devices/platform/ -name sensitivity)

#if [ "$SPEED" ]; then
#    	echo "$SPEED"
#    	echo "$SENS"
#    	sudo chmod 666 $SPEED
#    	sudo chmod 666 $SENS
#	python3 thinker.py $SPEED $SENS
#else
#    echo "Couldn't find trackpoint device."
#fi

DEVICE=$(xinput list | grep "TrackPoint" | grep "pointer" | cut -d '=' -f 2 | cut -f 1)

echo "Device: $(xinput list --name-only $i)"

python3 thinker.py $DEVICE