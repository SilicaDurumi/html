#!/usr/bin/python3
print("Content-Type: text/html; charset=UTF-8")
print()
import cgi, os, view, html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()

if 'id' in form:
  title = pageId = form["id"].value
  title = sanitizer.sanitize(title)
  description = open('data/'+pageId, 'r').read()
  description = sanitizer.sanitize(description)
  someImage = '<img src =" https://images.unsplash.com/photo-1530210124550-912dc1381cb8?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80"/ alt = "WA! SANS!" width ="50%" height="50%">'

  update_action = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action ='''
    <form action = "process_delete.py" method = "post">
      <input type ="hidden" name ="pageId" value="{}">
      <input type ="submit" value = "delete">
    </form>
  '''.format(pageId)

else:
  title = pageId = 'Shark Says?'
  description = 'a'
  update_action = ''
  delete_action = ''
  someImage = '<img src = "https://images.unsplash.com/photo-1531959870249-9f9b729efcf4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1326&q=80" alt = "a" width = "50%" height = "50%">'

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
    <a href="create.py">create</a>
    {update_action}
    {delete_action}

  <h2>{title}</h2>
  <p>{desc}</p>
  {someImage}
  <br>
  <a href = "/hello.py">1+1=?</a>
  <br>


 </body>
</html>
'''.format(
    title=title, 
    desc=description, 
    listStr=view.getList(), 
    update_action=update_action, 
    someImage=someImage,
    delete_action=delete_action))






























