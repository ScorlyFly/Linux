#!/bin/bash
#
grep='/bin/grep';
sed='/bin/sed';
xdotool='/usr/bin/xdotool';

var=$($xdotool getmouselocation);

X=`echo "$var" getmouselocation | $grep -Po 'x:[0-9]*[ ]' | $sed 's/x://'`;
Y=`echo "$var" getmouselocation | $grep -Po 'y:[0-9]*[ ]' | $sed 's/y://'`;
eval xdotool mousemove 1360 0 click 1;
$(xdotool mousemove $X $Y);

