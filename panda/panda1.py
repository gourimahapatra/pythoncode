import pandas as pd
s = pd.Series([1,3,5,np.nan,6,8])

print(s)

dates = pd.date_range("20230103", period=6)
print(dates)