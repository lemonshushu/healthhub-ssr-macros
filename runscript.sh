#!/bin/bash


RESUME_BTN=(1000 222)
PAUSE_BTN=(2743,209)
CONSOLE_TAB=(2170, 160)

xdotool search --name "Welcome HPACS :: Filmbox" windowactivate
xdotool mousemove --sync ${RESUME_BTN[0]} ${RESUME_BTN[1]} click 1 # Click resume button

# Scenarios to choose from
# /home/lemonshushu/macros/ct_mr_fastscroll1.sh
# /home/lemonshushu/macros/ct_normal1.sh
/home/lemonshushu/macros/mr_normal1.sh
# /home/lemonshushu/macros/us_fastscroll1.sh
# /home/lemonshushu/macros/us_normal1.sh

# xdotool mousemove --sync ${PAUSE_BTN[0]} ${PAUSE_BTN[1]} click 1 click 1 # Click pause button
xdotool mousemove --sync ${CONSOLE_TAB[0]} ${CONSOLE_TAB[1]} click 1 # Click console tab