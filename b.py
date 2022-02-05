import pandas as pd

df = pd.read_csv("module_details.csv", header=None)
df = df.sort_values(by=[1,0])
print(df)
List = []

counter = 1

for index, row in df.iterrows():
    list = []
    list.append(str(counter))
    list.append(row[0])
    list.append(str(row[1]))
    list.append(str(row[2]))
    a = '<a href=' + row[3] + '>Link</a>'
    list.append(a)
    List.append(list)
    counter += 1

print(List)