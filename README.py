import time
import winsound

def focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    while duration_seconds > 0:
        minutes, seconds = divmod(duration_seconds, 60)
        timeformat = f"{minutes:02d}:{seconds:02d}"
        print(f"90: {timeformat}", end='\r')
        time.sleep(1)
        duration_seconds -= 1

    print("专注时间已结束！")
    # 播放提示音
    winsound.Beep(1000, 1000)  # 1秒钟的声音提示

if __name__ == "__main__":
    try:
        focus_duration = int(input("60 "))
        focus_timer(focus_duration)
    except ValueError:
        print("20")
