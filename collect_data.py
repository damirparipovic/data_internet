import sys
import speedtest
import time
import datetime
import pandas as pd

# data = pd.read_csv("speed_data.csv", index_col=0)

curr_conection = speedtest.Speedtest()
down_speed = int(curr_conection.download())

print("bits:", down_speed)
print("bytes:", down_speed / 8)
print("kilobytes:", down_speed / 1000)
print("megabytes:", down_speed / 1000000)

try:
    while True:
        time.sleep(2)
        print("still going")

except KeyboardInterrupt:
    print("Ending program")


# if __name__ == "__main__":
#     main()