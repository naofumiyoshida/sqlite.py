#!/usr/bin/python3

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import cgi
import requests
import re
import sqlite3

print("Content-Type: text/html")    # HTML is following
print("")                             # blank line, end of headers

form = cgi.FieldStorage()
text = form.getvalue('text','')

#if (text==""):
print("<form action=\"sqlite.py\">")
print("<input type=text name=\"text\">")
print("<input type=submit>")
print("</form>")

conn = sqlite3.connect("word.db")
sql="select * from wordtable where vocabulary LIKE '%" + text + "%'"
cursor=conn.execute(sql)
print("<pre>")
print(sql)
print("</pre>")
for row in cursor.fetchall():
    print("vocabulary:" + str(row[0] + "  meaning:" + row[1]))
    print("<br>")
cursor.close
conn.close
