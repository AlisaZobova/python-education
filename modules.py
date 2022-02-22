"""Important python modules, exercise 15"""
import time
from datetime import datetime
import os
import sys

# time
t_sec = time.time()
print(time.ctime(t_sec))
time_tuple = (2022, 2, 11, 12, 0, 0, 5, 42, 0)
time_obj = time.struct_time(time_tuple)
print(time_obj)
print(f"Year: {time_obj.tm_year}, month: {time_obj.tm_mon}, day: {time_obj.tm_mday}\n")

# datetime
today_datetime = datetime.now()
print(f"Today is {today_datetime}")
print(f"Now {datetime.time(today_datetime)}")
print(f"Hours: {today_datetime.hour}, minutes {today_datetime.minute}, "
      f"second {today_datetime.second}\n")

# os
print(f"Current process id is {os.getpid()}")
print(f"Current working directory is {os.getcwd()}")
print(f"List of files and directories in a folder:\n {os.listdir(path='.')}\n")

# sys
print(f"Size of time_tuple: {sys.getsizeof(time_tuple)}")
print(f"Interval between threads: {sys.getswitchinterval()}")
