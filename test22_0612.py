import pandas as pd

tables = pd.read_html(r'https://tw.money.yahoo.com/currency-converter')
print(tables)
