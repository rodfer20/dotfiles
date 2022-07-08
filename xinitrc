export AWT_TOOLKIT=MToolkit
export _JAVA_AWT_WM_NONREPARENTING=1

unclutter &
feh --bg-fill ~/.bg/arch-linux-1366x768.jpg &
while xsetroot -name " [`cat /sys/class/power_supply/BAT0/capacity`% `cat /sys/class/power_supply/BAT0/status`] `date` "
do
    sleep 1
done &
exec dwm
