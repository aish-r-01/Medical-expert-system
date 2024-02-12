import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split, cross_val_score
from collections import Counter

def bayes_result(symptoms_user):

    data = pd.read_csv('Training.csv')
    data['prognosis'].unique()
    data.drop('Unnamed: 133', axis = 1, inplace = True)
    X = data.drop('prognosis', axis = 1)
    y = data['prognosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    naive_bayes = MultinomialNB()
    naive_bayes.fit(X_train, y_train)
    y_pred = naive_bayes.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    #print(f"Accuracy: {accuracy:.2f}")
    #print(classification_report(y_test, y_pred))

    first_row = X_test.iloc[0].to_frame().T
    class_probabilities_test = naive_bayes.predict_proba(first_row)
    class_probabilities_test[0]

    maximum = class_probabilities_test[0].max()
    classes = naive_bayes.classes_
    d = dict(zip(classes, class_probabilities_test[0]))
    cross_val_scores = cross_val_score(naive_bayes, X, y, cv=20)

    #user_symptom
    cols = X_test.columns.to_list()
    user_values = []
    for i in cols:
        if i in symptoms_user:
            user_values.append(1)
        else:
            user_values.append(0)

    df = pd.DataFrame()
    j = 0
    for i in cols:
        df[i] = [user_values[j]]
        j = j + 1

    predicted = naive_bayes.predict(df)
    predicted_diseases = naive_bayes.predict_proba(df)
    classes = naive_bayes.classes_
    dictionary = dict(zip(classes, predicted_diseases[0]))
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    #k = Counter(sorted_dict)
    return sorted_dict

#print(bayes_result(['itching']))
#print(bayes_result(['fever','headache']))

