import datetime as dt_module
import time

seconds = time.time()
print(
    f"Seconds since January 1, 1970: {seconds:,.4f} "
    f"or {seconds:.2e} in scientific notation"
)
print(dt_module.datetime.now().strftime("%b %d %Y"))
