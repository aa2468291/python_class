import pandas as pd

datas = [[100, 20, 30], [30, 50, 60], [50, 96, 20]]
inds = ['姆咪', '呱呱', '貓貓']
cols = ['國文', '英文', '數學']

df = pd.DataFrame(datas, inds, cols)
print(df)
