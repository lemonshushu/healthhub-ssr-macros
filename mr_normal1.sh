#!/bin/bash
# xdotool script (MR)
# Execution time : 60.19 secs

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
SRS10=(969 556)
SRS11=(1073 556)
SRS12=(1178 556)
SRS13=(1282 556)
SRS14=(1386 556)
SRS15=(1490 556)
SRS16=(1594 556)
SRS17=(1659 556)
SRS18=(1732 556)
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
click_srs10() {
    xdotool mousemove --sync ${SRS10[0]} ${SRS10[1]} click 1 click 1
}
click_srs11() {
    xdotool mousemove --sync ${SRS11[0]} ${SRS11[1]} click 1 click 1
}
click_srs12() {
    xdotool mousemove --sync ${SRS12[0]} ${SRS12[1]} click 1 click 1
}
click_srs13() {
    xdotool mousemove --sync ${SRS13[0]} ${SRS13[1]} click 1 click 1
}
click_srs14() {
    xdotool mousemove --sync ${SRS14[0]} ${SRS14[1]} click 1 click 1
}
click_srs15() {
    xdotool mousemove --sync ${SRS15[0]} ${SRS15[1]} click 1 click 1
}
click_srs16() {
    xdotool mousemove --sync ${SRS16[0]} ${SRS16[1]} click 1 click 1
}
click_srs17() {
    xdotool mousemove --sync ${SRS17[0]} ${SRS17[1]} click 1 click 1
}
click_srs18() {
    xdotool mousemove --sync ${SRS18[0]} ${SRS18[1]} click 1 click 1
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
sleep 2

click_srs15
sleep 1
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 3

click_srs18
sleep 2
scroll_next 3 $VERY_SLOW
sleep 3
scroll_prev 5 $SLOW
scroll_pause
scroll_prev 10 $SLOW
scroll_pause
scroll_prev 10 $MED
sleep 2

click_srs5
sleep 2
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 1
scroll_prev 7 $SLOW
sleep 3
scroll_next 5 $VERY_SLOW
sleep 4

click_srs12
sleep 1
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

click_srs3
sleep 1
scroll_next 7 $MED
sleep 2
scroll_next 10 $MED
scroll_pause
scroll_next 10 $FAST
scroll_pause
scroll_next 10 $FAST
sleep 5
scroll_prev 5 $VERY_SLOW
sleep 3
scroll_prev 10 $MED
scroll_pause
scroll_prev 10 $MED

# click_srs7
# sleep 2
# scroll_prev 3 $VERY_SLOW
# sleep 2
# scroll_prev 5 $SLOW
# sleep 2
# scroll_prev 10 $FAST
# scroll_pause
# scroll_prev 10 $FAST
# scroll_pause
# scroll_prev 5 $MED
# sleep 3

click_srs1
sleep 1
scroll_next 10 $VERY_FAST

mouse_away