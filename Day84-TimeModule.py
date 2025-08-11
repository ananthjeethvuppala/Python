# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.
# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized)
# The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.


import time
print('Start: ',time.time())
# time.sleep(5)
print('End: ',time.time())
print(time.localtime())
formatted_time=time.strftime('%d-%m-%y %H:%M:%S')
print(formatted_time)