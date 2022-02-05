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
            <th style="background-color:#808000" align="center">Link</th>
        </tr>
        {0}
    </table>
</body>
</HTML>"""

items = [['1', 'Measurement', '2', 'Aarya, Raunak', '<a href=https://docs.google.com/document/d/10UtvxtnTahkMEtaWQ_9nx8UH59OJx1tT4KxNeJv5GmY/edit#heading=h.enexohuphl1j>Link</a>'], 
    ['2', 'Addition and Subtraction', '1', 'Raunak, Mohit', '<a href=https://docs.google.com/document/d/1OOiFWetpGMXIExZqT6TCajRONpbPpZZ2khyjA8PXIXc/edit?usp=sharing>Link</a>'],
    ['3', 'Addition and Subtraction', '1', 'Raunak, Mohit', '<a href=https://docs.google.com/document/d/1OOiFWetpGMXIExZqT6TCajRONpbPpZZ2khyjA8PXIXc/edit?usp=sharing>Link</a>']
    ]
th = "<th>{0}</th>"
tr = "<tr>{0}</tr>"
td = "<td>{0}</td>"
subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]
x= (html.format("".join(subitems))) # or write, whichever
#print(x)

file = open("index.html", "w+")
file.write(x)
file.close()