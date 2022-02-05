import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='14QE434Iv-B_HQXRcWcN87HbuJPOTbVEj', dest_path='./module_details.csv')

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
