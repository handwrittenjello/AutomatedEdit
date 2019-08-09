from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('UFC.html')



@app.route('/ufc', methods=['POST'])
def foo():
    bar = request.form['ufcCard']
    return 'Hello %s have fun learning python <br/> <a href="/">Back Home</a>' % (bar), print(bar)

if __name__ == '__main__':
    app.run()