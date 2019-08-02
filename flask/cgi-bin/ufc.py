#!/usr/bin/python3

import cgi, cgitb
import subprocess

form = cgi.FieldStorage(
	fp=self.rfile,
    headers=self.headers,
    environ={'REQUEST_METHOD':'POST'})

ufcCard = form.getvalue('ufcCard')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s</h2>" % (ufcCard)
print "</body>"
print "</html>"