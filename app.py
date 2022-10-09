# pip install flask
# set FLASK_ENV=development
# flask run

# set FLASK_APP=main.py
# python -m flask run

# python -m venv name_of_venv
# name_of_venv\Scripts\activate
# pip freeze > requirements.txt
# pip install -r requirements.txt

# [pip install flask] so that you can apply... [from flask]
from flask import Flask, render_template, request

# [pip install nltk] so that you can apply... [from nltk.tokenize]
from nltk.tokenize import WhitespaceTokenizer

# [pip install sklearn] ...so that you can... [import pickle]
import pickle, os


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')


@app.route("/main/", methods = ['GET', 'POST'])
def mainpage():
    if request.method =="POST":
        entered_password = request.form['password']
    else:
        return 'index.html'


    # Load the algorithm models
    

    vectorizer_model = pickle.load(open("vectorizer.pkl",'rb')) 

    log_reg_model = pickle.load(open("log_reg.pkl",'rb')) 
    Bernoulli_Naive_Bayes_model = pickle.load(open('Bernoulli_Naive_Bayes.pkl','rb')) 
    # Decision_Tree_model = pickle.load(open('Decision_Tree.pkl','rb')) 
    # Random_Forest_model = pickle.load(open('Random_Forest.pkl','rb')) 
    multi_layer_perceptron_model = pickle.load(open('multi_layer_perceptron.pkl','rb')) 

    def word_with_white_spaces(inputs):
        characters = []
        st = " "
        for i in inputs:
            characters.append(i)
        
        return st.join(characters)


    p_a_s_s_w_o_r_d = word_with_white_spaces(entered_password)
    password_list = [p_a_s_s_w_o_r_d]

    
    password_vec = vectorizer_model.transform(password_list)

    log_reg_model_test = log_reg_model.predict(password_vec)
    Bernoulli_Naive_Bayes_model_test = Bernoulli_Naive_Bayes_model.predict(password_vec)
    # Decision_Tree_model_test = Decision_Tree_model.predict(password_vec)
    # Random_Forest_model_test = Random_Forest_model.predict(password_vec)
    multi_layer_perceptron_model_test = multi_layer_perceptron_model.predict(password_vec)

    # return "render_template('main.html')"

    return render_template('main.html',
                            log_reg = log_reg_model_test[0],
                            Bernoulli_Naive = Bernoulli_Naive_Bayes_model_test[0],
                            multi_layer = multi_layer_perceptron_model_test[0]#,
                            # Decision_Tree = Decision_Tree_model_test[0],
                            # Random_Forest = Random_Forest_model_test[0],
                            )

if __name__ == '__main__':
    app.run(debug=True)   