from flask import Flask, render_template, request
import cgi, cgitb

app = Flask(__name__)
@app.route('/')
def ufc():
    return render_template('ufc.html')
    if __name__ == '__main__':
        app.run(debug=True)
@app.route('/cgi-bin')
def ufcCard():
	 return render_template(ufc.py)
	 if __name__ == '__main__':
	 	app.run(debug=True)

#form = cgi.FieldStorage()
#ufcCard = form.getvalue('ufcCard')#

#print("Content-type:text/html\r\n\r\n")
#print("<html>")
#print("<head>")
#print("<title>Hello - Second CGI Program</title>")
#print("</head>")
#print("<body>")
#print("<h2>Hello %s</h2>" % (ufcCard))
#print("</body>")
#print("</html>")
