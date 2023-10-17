from flask import Flask, render_template, request, jsonify, flash
import random
app = Flask(__name__)
app.secret_key = b'very_secret_string'

@app.route('/')
def home():  # put application's code here
    return render_template('home.html', username="Partially Developed");

@app.route('/math-game', methods=['GET', 'POST'])
def math_game():
    if request.method == 'POST':
        #handle this case
        if "answer" in request.form and "correct_answer" in request.form:
            if request.form["answer"] == request.form["correct_answer"]:
                ## the answer is correct
                flash("correct")
            else:
                ##the answer is incorrect
                flash(f"incorrect! The Correct Answer was {request.form['correct_answer']}")
        return jsonify(request.form)
        pass

    num1 = random.randint(0,100);
    num2 = random.randint(0,100);
    correct_answer = num1+num2;

    return render_template('math.html', num1=num1, num2=num2, correct_answer=correct_answer)



# @app.route('/about')
# def about():
#     return "About Page";
#
# @app.route('/user/<username>')
# def user_profile(username):
#     return f"Welcome {username}"

if __name__ == '__main__':
    app.run()

