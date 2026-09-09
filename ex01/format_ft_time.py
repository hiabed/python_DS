import datetime as dt_module
#importing the module directly is safer and won't cause conflicts with local variables or functions.
def format_ft_time():
    # Get the current time
    now = dt_module.datetime.now()
    random_datetime = dt_module.datetime(2023, 3, 1)
    print( f"Seconds since {random_datetime.strftime('%B %-d, %Y')}: {(now - random_datetime).total_seconds():,.4f} or {(now - random_datetime).total_seconds():.2e} in scientific notation")
    print(now.strftime("%b %d %Y"))

    # return now

if __name__ == "__main__":
    format_ft_time()