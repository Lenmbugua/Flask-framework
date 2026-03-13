from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html', message="The result is passed", score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', message="The person has failed", score=score)

@app.route('/results/<int:score>')
def results(score):
    if score < 50:
        return redirect(url_for('fail', score=score))
    else:
        return redirect(url_for('success', score=score))

if __name__ == '__main__':
    app.run(debug=True)
