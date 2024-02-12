from experta import *
import ast

result=''
def answe_assign(answer_list):
     global answers
     answers=answer_list

class MedicalExpert(KnowledgeEngine):
    username = "", 
    
    @DefFacts()
    def needed_data(self):
        self.chest_pain=answers[0]
        self.cough=answers[1]
        self.fainting=answers[2]
        self.fatigue=answers[3]
        self.headache=answers[4]
        self.back_pain=answers[5]
        self.sunken_eyes=answers[6]
        self.fever=answers[7]
        self.sore_throat=answers[8]
        self.restlessness=answers[9]
        yield Fact(findDisease = 'true')
        

    @Rule(Fact(findDisease='true'), NOT (Fact(chestPain = W())),salience = 995)
    def hasChestPain(self):
        
        self.chest_pain = self.chest_pain.lower()
        self.declare(Fact(chestPain = self.chest_pain.strip().lower()))

   
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        self.cough = self.cough.lower()
        self.declare(Fact(cough = self.cough.strip().lower()))

    
   
    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
       
        self.fainting = self.fainting.lower()
        self.declare(Fact(fainting = self.fainting.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        
        self.headache = self.headache.lower()
        self.declare(Fact(headache = self.headache.strip().lower()))
    
   
    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        
        self.back_pain = self.back_pain.lower()
        self.declare(Fact(back_pain = self.back_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(sunken_eyes = W())),salience = 950)
    def hasSunkenEyes(self):
        
        self.sunken_eyes = self.sunken_eyes.lower()
        self.declare(Fact(sunken_eyes = self.sunken_eyes.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fever = W())),salience = 945)
    def hasfever(self):
        
        self.fever=self.fever.lower()
        self.declare(Fact(fever = self.fever.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sore_throat = W())),salience = 940)
    def hassorethroat(self):
        
        self.sore_throat = self.sore_throat.lower()
        self.declare(Fact(sore_throat = self.sore_throat.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(restlessness = W())),salience = 935)
    def hasrestlessness(self):
        
        self.restlessness = self.restlessness.lower()
        self.declare(Fact(restlessness = self.restlessness.strip().lower()))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_1(self):
        self.declare(Fact(disease = 'Alzheimers'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_2(self):
        self.declare(Fact(disease = 'Asthma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_3(self):
        self.declare(Fact(disease = 'Diabetes'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_4(self):
        self.declare(Fact(disease = 'Epilepsy'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_5(self):
        self.declare(Fact(disease = 'Glaucoma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_6(self):
        self.declare(Fact(disease = 'Heart Disease'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_7(self):
        self.declare(Fact(disease = 'Heat Stroke'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_8(self):
        self.declare(Fact(disease = 'Hyperthyroidism'))
    
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_9(self):
        self.declare(Fact(disease = 'Hypothermia'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_10(self):
        self.declare(Fact(disease = 'Jaundice'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_11(self):
        self.declare(Fact(disease = 'Sinusitis'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_12(self):
        self.declare(Fact(disease = 'Tuberculosis'))


    @Rule(Fact(findDisease='true'),NOT (Fact(disease = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = 1)
    def getDisease(self, disease):
        global result
        
        if(disease == 'unknown'):
            mapDisease = []
            result=''
            mapDisease.append('back_pain')
            mapDisease.append('chest_pain')
            mapDisease.append('cough')
            mapDisease.append('fainting')
            mapDisease.append('fatigue')
            mapDisease.append('fever')
            mapDisease.append('headache')
            mapDisease.append('sore_throat')
            mapDisease.append('restlessness')
            mapDisease.append('sunken_eyes') 
            result+='\n\nWe checked the following symptoms'+str(mapDisease)
            mapDisease_val=[self.back_pain,self.chest_pain,self.cough,self.fainting,self.fatigue
            ,self.fever,self.headache,self.sore_throat,self.restlessness,self.sunken_eyes]
            result+='\n\nSymptoms in patients are :'+ str(mapDisease_val)
            
            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()
            
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'yes':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            result+='\n\nYes symptoms noticed are : '+str(yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_symptoms:
                        count+=1
                #print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                result+="No diseases found.You are healthy!"
                return result
            else:
                
                result+="\n\nWe are unable to tell you the exact disease with confidence.But we believe that you suffer from"+str(pred_dis)
                result+='\n\nSome info about the disease:'+str(pred_dis)
                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r")
                result+=f.read()
                result+='\n\n'
                result+='\n\nNo need to worry. We even have some preventive measures for you!\n'
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r")
                result+=f.read()
                return result
        else:
            
            result=''
            result+='The most probable illness you are suffering from is:'+str(disease)
            result+='\n\n'
            result+='Some info about the disease:\n'
            f = open("disease/disease_descriptions/" + disease + ".txt", "r")
            result+=f.read()
            result+='\n'
            result+='\n\nNo need to worry. We even have some preventive measures for you!\n'
            f = open("disease/disease_treatments/" + disease + ".txt", "r")
            result+=f.read()
            
            return result
        
    
    # @Rule(Fact(findDisease = 'true'),
    # Fact(name=MATCH.name))
    # def greet(self, name):
    #     print("Hi!",name, "How is the weather?")
'''if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    #print('Printing engine facts after 1 run',engine.facts)'''

questions=['Do you have chest pain?','Do you have cough?','Do you faint occasionally?','Do you experience fatigue occasionally?','Do you experience headaches?',
           'Do you experience back pains?' ,'Do you experience sunken eyes?','Do you experience fever?','Do you experience sore throat?','Do you experience restlessness?']

'''engine=MedicalExpert()
engine.reset()
engine.run()
print(result)'''
           

   