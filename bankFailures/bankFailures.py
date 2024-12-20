import pandas as pd

tables = pd.read_html("fdic_failed_bank_list.html")

len(tables)

failures = tables[0]

failures.head()

close_timestamps = pd.to_datetime(failures["Closing Date"])

close_timestamps.dt.year.value_counts()