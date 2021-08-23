import pandas as pd

io=r'D:\python_xiangmu\other_projects\lianxi.xls'


data=pd.read_excel(io,sheet_name=0,names = ['rank','player','club','goal'])

data.head()
print(data)
