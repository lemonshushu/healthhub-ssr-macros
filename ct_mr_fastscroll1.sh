#!/bin/bash

# xdotool script (CT)
# Execution time : 11.705 secs

# Coordinates
CENTER=(886 1227)
SRS1=(126 574)
SRS2=(215 570)
SRS3=(314 563)
SRS4=(418 539)
SRS5=(489 553)
SRS6=(581 560)
SRS7=(700 563)
SRS8=(822 568)
SRS9=(896 560)
AWAY=(2305 859)

# Scroll delays
VERY_FAST=5
FAST=12
MED=30
SLOW=100
VERY_SLOW=200

# functions
click_center() {
    xdotool mousemove --sync ${CENTER[0]} ${CENTER[1]} click 1
}
click_srs1() {
    xdotool mousemove --sync ${SRS1[0]} ${SRS1[1]} click 1 click 1
}
click_srs2() {
    xdotool mousemove --sync ${SRS2[0]} ${SRS2[1]} click 1 click 1
}
click_srs3() {
    xdotool mousemove --sync ${SRS3[0]} ${SRS3[1]} click 1 click 1
}
click_srs4() {
    xdotool mousemove --sync ${SRS4[0]} ${SRS4[1]} click 1 click 1
}
click_srs5() {
    xdotool mousemove --sync ${SRS5[0]} ${SRS5[1]} click 1 click 1
}
click_srs6() {
    xdotool mousemove --sync ${SRS6[0]} ${SRS6[1]} click 1 click 1
}
click_srs7() {
    xdotool mousemove --sync ${SRS7[0]} ${SRS7[1]} click 1 click 1
}
click_srs8() {
    xdotool mousemove --sync ${SRS8[0]} ${SRS8[1]} click 1 click 1
}
click_srs9() {
    xdotool mousemove --sync ${SRS9[0]} ${SRS9[1]} click 1 click 1
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

click_srs5
sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $VERY_FAST
scroll_pause
scroll_next 10 $VERY_FAST
sleep 1

click_srs7
sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $VERY_FAST
sleep 1
scroll_prev 13 $VERY_FAST
scroll_pause
scroll_prev 13 $VERY_FAST
scroll_pause
scroll_prev 10 $FAST
scroll_pause
scroll_prev 10 $FAST
sleep 1

click_srs1
sleep 1
scroll_next 10 $VERY_FAST
scroll_pause
scroll_next 10 $VERY_FAST
scroll_pause
scroll_next 10 $VERY_FAST
scroll_pause
scroll_next 12 $VERY_FAST
scroll_pause
scroll_next 12 $VERY_FAST

click_srs3
sleep 1
scroll_prev 10 $VERY_FAST
scroll_pause
scroll_prev 10 $VERY_FAST
scroll_pause
scroll_prev 10 $VERY_FAST
sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST

mouse_away