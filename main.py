import get_historical as historical
import moving_average as ma 
import time

if __name__ == "__main__":
    timer = 0
    historical.run()
    ma.ma_calc()
    while True:
        if timer < 900: #15 min
            time.sleep(1)
            timer += 1
        else:
            timer = 0
            historical.run()
            ma.ma_calc()
