import webbrowser
import time 

total_break = 3
break_count = 0
while(break_count <  total_break):
    time.sleep(10)
    webbrowser.open("http://play.baidu.com/?__m=mboxCtrl.playSong&__a=274841326&__o=/||dayhotIcon#")
    break_count += 1