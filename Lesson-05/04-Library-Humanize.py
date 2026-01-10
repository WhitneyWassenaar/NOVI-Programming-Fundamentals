# You must install the library in the terminal: pip install humanize
# You must use a venv (virtual environment)


import humanize
import datetime as dt

file_space = humanize.naturalsize(1_000_000)

print(file_space)

seconds_ago = humanize.naturaltime(dt.timedelta(seconds=7))

print(seconds_ago)