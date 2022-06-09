#!/bin/bash
# xdotool script (US)
# Execution time : 59.934 secs

# Coordinates
CENTER=(886 1227)
SRS1=(126 574)
AWAY=(2305 859)

# Scroll delays
VERY_FAST=12
FAST=30
MED=70
SLOW=100
VERY_SLOW=200

# functions
click_center() {
    xdotool mousemove --sync ${CENTER[0]} ${CENTER[1]} click 1
}
click_srs1() {
    xdotool mousemove --sync ${SRS1[0]} ${SRS1[1]} click 1 click 1
}

# $1 : How many times to scroll
# $2 : Delay between each scroll
scroll_next() {
    SCROLL_NEXT_N=""
    for i in $(seq 1 $1); do
        SCROLL_NEXT_N="$SCROLL_NEXT_N Down"
    done
    # Scroll up
    xdotool key --delay $2 $SCROLL_NEXT_N
}
scroll_prev() {
    SCROLL_PREV_N=""
    for i in $(seq 1 $1); do
        SCROLL_PREV_N="$SCROLL_PREV_N Up"
    done
    xdotool key --delay $2 $SCROLL_PREV_N
}
scroll_pause() {
    sleep 0.2
}
mouse_away() {
    xdotool mousemove --sync ${AWAY[0]} ${AWAY[1]}
}

click_center

sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 1
scroll_prev 7 $SLOW
sleep 3
scroll_next 5 $VERY_SLOW

sleep 1
scroll_next 7 $MED
sleep 2
scroll_next 10 $MED
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 3
scroll_prev 5 $VERY_SLOW
sleep 1
scroll_prev 10 $MED
scroll_pause
scroll_prev 10 $MED

sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 3

scroll_next 3 $VERY_SLOW
sleep 3
scroll_prev 5 $SLOW
scroll_pause
scroll_prev 10 $SLOW
scroll_pause
scroll_prev 10 $MED
sleep 4
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 1
scroll_prev 7 $SLOW
sleep 3
scroll_next 5 $VERY_SLOW
sleep 5

scroll_next 5 $MED
sleep 2
scroll_next 13 $FAST
scroll_pause
scroll_next 10 $VERY_FAST
scroll_pause
scroll_next 10 $VERY_FAST
sleep 3
scroll_prev 10 $VERY_FAST
sleep 2
scroll_prev 10 $MED
scroll_pause
scroll_prev 5 $SLOW
sleep 2

# sleep 1
# scroll_next 7 $MED
# sleep 2
# scroll_next 10 $MED
# scroll_pause
# scroll_next 10 $FAST
# scroll_pause
# scroll_next 10 $FAST
# sleep 5
# scroll_prev 5 $VERY_SLOW
# sleep 3
# scroll_prev 10 $MED
# scroll_pause
# scroll_prev 10 $MED

# sleep 1
# scroll_next 10 $VERY_FAST

mouse_away