import get_historical as historical
import moving_average as ma 
import time

if __name__ == "__main__":
    time = 0
    historical.run()
    while True:
        if time < 900: #15 min
            time.sleep(1)
            time += 1
        else:
            time = 0
            historical.run()
