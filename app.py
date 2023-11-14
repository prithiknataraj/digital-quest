from flask import Flask, render_template, redirect, url_for, request
import json

app= Flask(__name__)

# Initializing global variables.
Start= 0

# Fetching the data from the json.
with open('questions.json', 'r') as file:
        questions = json.load(file)

@app.route('/')
def index():
    # global start
    global Start

    return render_template('index.html', start= Start)

@app.route('/start', methods=['POST', 'GET'])
def start():
    global Start, questions

    Start+= 1

    return render_template('index.html', start= Start, questions= questions, status= 'correct')

# question 1
@app.route("/input1", methods=['POST', 'GET'])
def answer1():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer1')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 2
@app.route("/input2", methods=['POST', 'GET'])
def answer2():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer2')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 3
@app.route("/input3", methods=['POST', 'GET'])
def answer3():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer3')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 4
@app.route("/input4", methods=['POST', 'GET'])
def answer4():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer4')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 5
@app.route("/input5", methods=['POST', 'GET'])
def answer5():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer5')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 6
@app.route("/input6", methods=['POST', 'GET'])
def answer6():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer6')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 7
@app.route("/input7", methods=['POST', 'GET'])
def answer7():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer7')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 8
@app.route("/input8", methods=['POST', 'GET'])
def answer8():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer8')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 9
@app.route("/input9", methods=['POST', 'GET'])
def answer9():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer9')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

# question 10
@app.route("/input10", methods=['POST', 'GET'])
def answer10():
    global Start, questions

    # Getting the user entered value from html.
    user_input = request.form.get('answer10')
    print(user_input)

    # Comparing the user input with the answer.
    if user_input.lower() in questions[Start- 1]:
        Start+= 1
        return render_template('index.html', start= Start, questions= questions, status= 'correct')
         
    return render_template('index.html', start= Start, questions= questions, status= 'wrong')

if __name__== '__main__':
        app.run(debug= True)
