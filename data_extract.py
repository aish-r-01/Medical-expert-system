import pandas as pd
df=pd.read_csv('Training.csv')
df.drop(df.columns[[133]], axis=1, inplace=True)

Symptoms=df.columns
#print(Symptoms)

Diseases=df.prognosis.unique()
#print(Diseases)

disease_count=df['prognosis'].value_counts()


disease_prob={}
for i in Diseases:
     disease_prob[i]=disease_count[i]/(120*len(disease_count))
#print(disease_prob)

'''symptoms_prob_list=[]
for i in Diseases:
    each_dis_symptom=[]
    for j in Symptoms:
          
        count=0
        for z in df[df['prognosis']==i][j] :
            if z:
                count+=1
        each_dis_symptom.append(count/120)
        each_dis_symptom.append(1-(count/120))
        
    symptoms_prob_list.append(each_dis_symptom)

symptoms_prob={}
for i in range(len(Diseases)):
     symptoms_prob[Diseases[i]]=symptoms_prob_list[i]'''

def conditional_probablities(symptom, disease):
  p1=len(df[(df[symptom]==1) & (df['prognosis']==disease)])/len(df[df['prognosis']== disease])
  p2=len(df[(df[symptom]==0) & (df['prognosis']==disease)])/len(df[df['prognosis']== disease])
  p3=len(df[(df[symptom]==1) & (df['prognosis']==disease)])/len(df[df['prognosis']!= disease])
  p4=len(df[(df[symptom]==0) & (df['prognosis']==disease)])/len(df[df['prognosis']!= disease])
  return p1,p2,p3,p4

disease_cpd={}
for i in Diseases :
    each_disease_sym=[]
    for j in Symptoms:
        each_disease_sym.append(conditional_probablities(j,i))
    disease_cpd[i]=each_disease_sym
print(disease_cpd)
    