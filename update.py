#!/usr/bin/python3
print("Content-Type: text/html; charset=UTF-8")
print()
import cgi,os,view

form = cgi.FieldStorage()

if 'id' in form:
  pageId = form["id"].value
  description = open('data/'+pageId,'r').read()
else:
  pageId = 'Welcome'
  description = 'Hello, Welcome'

print('''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SilicaWeb</title>
</head>
 <body>
  <h1><a href="index.py">Test</a></h1>
  <ol>
    {listStr}
  </ol>
  
    <form action = "process_update.py" method ="post">
     <input type = "hidden" name = "pageId" value="{form_default_title}">
     <p><input type = "text" name="title" placeholder = "title" value ="{form_default_title}"></p>
     <p><textarea rows="4" name="description" placeholder = "description">{form_default_description}</textarea></p>
     <p><input type = "submit"></p>
    </form>

  <a href = "/hello.py">1+1=?</a>
 </body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title = pageId, form_default_description = description))






























