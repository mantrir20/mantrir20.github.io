import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd


html = """<HTML>
<head>
<style>

.header {{
  padding: 5px;
  text-align: center;
  background: #1abc9c;
  color: white;
  font-size: 15px;
}}

.button {{
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}}

table {{
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}

th {{
  border: 1px solid #dddddd;
  font-size: 20px;
  text-align: center;
  padding: 8px;
}}

td {{
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}}



</style>
</head>
<body>
    <div class="header">
        <h1>MATH CDTA TEAM</h1>    
    </div>

    <button type="button" class="button" onclick="location.href='game.html'">Banker-Bonker</button>
    <hr>
    <h3>Vector Mathematics Module Details</h3>
    <table>
        <tr>
            <th style="background-color:#808000" align="center"></th>
            <th style="background-color:#808000" align="center">Name of module</th>
            <th style="background-color:#808000" align="center">Level</th>
            <th style="background-color:#808000" align="center">Authors</th>
            <th style="background-color:#808000" align="center">Google Link</th>
            <th style="background-color:#808000" align="center">PDF</th>
        </tr>
        {0}
    </table>
</body>
</HTML>"""

gdd.download_file_from_google_drive(file_id='14QE434Iv-B_HQXRcWcN87HbuJPOTbVEj', dest_path='./module_details.csv')

df = pd.read_csv("module_details.csv", header=None)
df = df.sort_values(by=[1,0])
print(df)
items = []

counter = 1

for index, row in df.iterrows():
    list = []
    list.append(str(counter))
    list.append(row[0])
    list.append(str(row[1]))
    list.append(str(row[2]))
    a = '<a href=' + row[3] + '>Link</a>'
    list.append(a)
    b = '<a href=' + row[4] + '>Link</a>'
    list.append(b)
    items.append(list)
    counter += 1

th = "<th>{0}</th>"
tr = "<tr>{0}</tr>"
td = "<td>{0}</td>"
subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]
x= (html.format("".join(subitems))) # or write, whichever
#print(x)

file = open("index.html", "w+")
file.write(x)
file.close()