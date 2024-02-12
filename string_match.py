from nltk import ngrams
import string
string.punctuation
import nltk
from nltk.corpus import stopwords
import re


def remove_punctuation(text):
  if(type(text)==float):
    return text
  ans = ""  
  for i in text:     
    if i not in string.punctuation:
      ans+=i    
  return ans



def generate_N_grams1(text, ngram = 1):
  #removing stop words
  words=[word for word in text.split(" ") if word not in set(stopwords.words('english'))]  
  temp=zip(*[words[i:] for i in range(0,ngram)])
  ans=[' '.join(ngram) for ngram in temp]
  return ans

def generate_N_grams2(text, ngram = 2):
  #removing stop words
  words=[word for word in text.split(" ") if word not in set(stopwords.words('english'))]  
  temp=zip(*[words[i:] for i in range(0,ngram)])
  ans=[' '.join(ngram) for ngram in temp]
  return ans

'''extracted_symptoms = generate_N_grams(description1)
ext2=generate_N_grams(desc2)
ext3=generate_N_grams(desc3)
extracted_symptoms=generate_N_grams(description)'''


# List of known symptoms in the dataset
known_symptoms = ['itching',
 'skin_rash',
 'nodal_skin_eruptions',
 'continuous_sneezing',
 'shivering',
 'chills',
 'joint_pain',
 'stomach_pain',
 'acidity',
 'ulcers_on_tongue',
 'muscle_wasting',
 'vomiting',
 'burning_micturition',
 'spotting_ urination',
 'fatigue',
 'weight_gain',
 'anxiety',
 'cold_hands_and_feets',
 'mood_swings',
 'weight_loss',
 'restlessness',
 'lethargy',
 'patches_in_throat',
 'irregular_sugar_level',
 'cough',
 'high_fever',
 'sunken_eyes',
 'breathlessness',
 'sweating',
 'dehydration',
 'indigestion',
 'headache',
 'yellowish_skin',
 'dark_urine',
 'nausea',
 'loss_of_appetite',
 'pain_behind_the_eyes',
 'back_pain',
 'constipation',
 'abdominal_pain',
 'diarrhoea',
 'mild_fever',
 'yellow_urine',
 'yellowing_of_eyes',
 'acute_liver_failure',
 'fluid_overload',
 'swelling_of_stomach',
 'swelled_lymph_nodes',
 'malaise',
 'blurred_and_distorted_vision',
 'phlegm',
 'throat_irritation',
 'redness_of_eyes',
 'sinus_pressure',
 'runny_nose',
 'congestion',
 'chest_pain',
 'weakness_in_limbs',
 'fast_heart_rate',
 'pain_during_bowel_movements',
 'pain_in_anal_region',
 'bloody_stool',
 'irritation_in_anus',
 'neck_pain',
 'dizziness',
 'cramps',
 'bruising',
 'obesity',
 'swollen_legs',
 'swollen_blood_vessels',
 'puffy_face_and_eyes',
 'enlarged_thyroid',
 'brittle_nails',
 'swollen_extremeties',
 'excessive_hunger',
 'extra_marital_contacts',
 'drying_and_tingling_lips',
 'slurred_speech',
 'knee_pain',
 'hip_joint_pain',
 'muscle_weakness',
 'stiff_neck',
 'swelling_joints',
 'movement_stiffness',
 'spinning_movements',
 'loss_of_balance',
 'unsteadiness',
 'weakness_of_one_body_side',
 'loss_of_smell',
 'bladder_discomfort',
 'foul_smell_of urine',
 'continuous_feel_of_urine',
 'passage_of_gases',
 'internal_itching',
 'toxic_look_(typhos)',
 'depression',
 'irritability',
 'muscle_pain',
 'altered_sensorium',
 'red_spots_over_body',
 'belly_pain',
 'abnormal_menstruation',
 'dischromic _patches',
 'watering_from_eyes',
 'increased_appetite',
 'polyuria',
 'family_history',
 'mucoid_sputum',
 'rusty_sputum',
 'lack_of_concentration',
 'visual_disturbances',
 'receiving_blood_transfusion',
 'receiving_unsterile_injections',
 'coma',
 'stomach_bleeding',
 'distention_of_abdomen',
 'history_of_alcohol_consumption',
 'fluid_overload.1',
 'blood_in_sputum',
 'prominent_veins_on_calf',
 'palpitations',
 'painful_walking',
 'pus_filled_pimples',
 'blackheads',
 'scurring',
 'skin_peeling',
 'silver_like_dusting',
 'small_dents_in_nails',
 'inflammatory_nails',
 'blister',
 'red_sore_around_nose',
 'yellow_crust_ooze']

#applying jaccard similarity
def jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    similarity = intersection / union if union != 0 else 0
    return similarity


def symptoms_mapped(extracted_symptoms):
    symptom_mapping = []
    for i in extracted_symptoms:
        for j in known_symptoms:
            string1 = i
            string2 = j
            similarity_score = jaccard_similarity(string1, string2)
            if similarity_score > 0.7:
                symptom_mapping.append(i)
    return symptom_mapping


'''description1='i have abdominal pain and headache'
print(description1)
description1 = remove_punctuation(description1)
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

print('detected: ',final_symptoms)'''




       
