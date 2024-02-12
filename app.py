from flask import Flask , render_template , request,jsonify
from string_match import remove_punctuation,generate_N_grams1,generate_N_grams2,symptoms_mapped,known_symptoms
from naive_bayes_2 import bayes_result
from main import questions,answe_assign,MedicalExpert
import json
import re
app = Flask(__name__)
@app.route('/')
def index ():
    return render_template('index.html')
@app.route('/inter_page')
def inter_page():
    return render_template('inter_page.html')

@app.route('/chat_page')
def chat_page():
    return render_template('chat_page.html')

@app.route('/questionnarie')
def questionnarie():
    return render_template('questionnarie.html',questions=enumerate(questions, start=1))

@app.route('/submit', methods=['POST'])
def submit():
    answers = [request.form[f'q{i+1}'] for i in range(10)]
    answe_assign(answers)
    engine=MedicalExpert()
    engine.reset()
    engine.run()
    from main import result
    print(result)
    return render_template('result_diagnosis.html',data=result)
    


@app.route('/get_response',methods=["GET","POST"])
def get_response() :
    user_message=request.form['user_message']
    description1 = remove_punctuation(user_message)
    extracted_symptoms = generate_N_grams1(description1)   
    two_word_extract=generate_N_grams2(description1)
    ext_1=symptoms_mapped(extracted_symptoms)
    ext_2=symptoms_mapped(two_word_extract)
    final_symptoms=ext_1
    for i in ext_1:
        for j in ext_2:
            if re.search(i,j):
                ext_2.remove(j)
    final_symptoms.extend(ext_2)
    if len(final_symptoms) == 0 :
        respond= 'Sorry invalid information !!'
    else :
        result=bayes_result(final_symptoms)
        top=0
        respond=' '
        for i in result:
          if top<3:
            respond+=i+' Probability: '+str(result[i])+'\n'
            top+=1
          else :
              break
    bot_response = respond
    print(bot_response)
    return jsonify({'bot_response': bot_response})
if __name__ == '__main__':
    app.run(debug=True)
    
