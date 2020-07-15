from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    lower = any(map(str.islower, username))
    upper = any(map(str.isupper, username))
    if username:
        number = username[-1].isdigit()
    else:
        number = False
    valid = all([lower, upper, number])
    return render_template('report.html', username=username, valid=valid,
                            lower=lower, upper=upper, number=number)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
