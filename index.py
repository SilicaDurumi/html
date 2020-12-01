#!/usr/bin/python3
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value

print('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
 <h1><a href="index.py?id=Test">Test</a></h1>
 <br>
 <h4><a href = "index.py?id=PYTHON">1.Python</a></h4>
 <h4><a href = "index.py?id=CSS">2.css</a></h4>
 <h4><a href = "index.py?id=HTML">3.htmL</a></h4>
 <h4><a href = "index.py?id=JAVASCRIPT">4.JavaScript</a></h4>
 <h2>{title}</h2>
<a href = "/hello.py">1+1=?</a>
</body>
</html>
'''.format(title=pageId))




