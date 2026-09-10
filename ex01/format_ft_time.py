import datetime as dt_module
import time
# Get Epoch time in seconds since January 1, 1970
seconds = time.time()
# Format the output using f-strings
print( f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(dt_module.datetime.now().strftime("%b %d %Y"))
