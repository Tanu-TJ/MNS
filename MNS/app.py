from flask import Flask, render_template

app = Flask(__name__)

# Main route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the result redirections
@app.route('/result/<answer1>/<answer2>')
def result(answer1, answer2):
    if answer1 == 'yes' and answer2 == 'yes':
        return render_template('result_1.html')  # Show Result 1
    elif answer1 == 'yes' and answer2 == 'no':
        return render_template('result_3.html')  # Show Result 2
    elif answer1 == 'no' and answer2 == 'yes':
        return render_template('result_4.html')  # Show Result 3
    elif answer1 == 'no' and answer2 == 'no':
        return render_template('result_2.html')  # Show Result 4

if __name__ == '__main__':
    app.run(debug=True)
