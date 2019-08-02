import cgi, cgitb

form = cgi.FieldStorage(
	fp=self.rfile,
    headers=self.headers,
    environ={'REQUEST_METHOD':'POST'})

ufcCard = form.getvalue('ufcCard')

print(ufcCard)