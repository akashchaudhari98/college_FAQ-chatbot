#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import joblib
import re
import numpy as np

def get_NER(text):
    from college_bot import predictor
    model_NER = spacy.load(r"C:\Users\Akash\Desktop\be_proj_py")
    doc = model_NER(text)
    ans = ""
    for ent in doc.ents:
        ans = ent.text
        ans = predictor.predict(ans)
        ans = "".join(ans)
    try:
        return ans

    except:
       return ans == "empty"
   

#get_NER("who is the electronics head of the department")

def get_intent(data):

    print(data)
    names = ["Faculty","infrastructure","syllabus","admissions","placements","programes","student"]
    scores = np.zeros(7)
    print(scores)
    Faculty       = ["HOD","faculty","teachers","instructors","assistant","head","members"]
    infrastructure= ["infrastructure","classroom","architechture","labs","campus","courts","computers"]
    syllabus   =    ["content","elective","curriculum","outcomes","subjects","courses"    ]
    admissions =    ["SET","entrance","admissions","eligible","eligiblity","score","secure"]
    placements =    ["placements","companies","company","job","package"                   ]
    programes  =    ["branches","department","electronics","comps","computer science","information"]
    student_body =  ["body","orion","robocon","life","student","bodies","council","students","activities","extra"]

    for words in data.split():
        if words in Faculty:    
            scores[0] = scores[0] +1
        if words in infrastructure:
            scores[1] = scores[1] +1
        if words in syllabus:
            scores[2] = scores[2] +1
        if words in admissions:
            scores[3] = scores[3] +1
        if words in placements:
            scores[4] = scores[4] +1
        if words in programes:
            scores[5] = scores[5] +1
        if words in student_body:
            scores[6] = scores[6] +1 
    print(scores)

    if np.max(scores) == 0:
        intent = ""
        return intent
    data = data.lower()
    data = re.sub(r'[^a-zA-Z0-9]', " ", data)
    #mod = joblib.load('intent_model_1.joblib')
    mod = joblib.load('college_bot/intent_model_1.joblib')

    intent = mod.predict([data])
    intent ="".join(intent)
    print(intent)
    if intent == "Faculty":
        scores[0] = scores[0] +3
    if intent == "infrastructure":
        scores[1] = scores[1] +3
    if intent == "syllabus" :
        scores[2] = scores[2] +3 
    if intent == "admissions":
        scores[3] = scores[3] +3
    if intent == "placements": 
        scores[4] = scores[4] +3
    if intent == "programes": 
        scores[5] = scores[5] +3
    if intent == "student body":
        scores[6] = scores[6] +3 
    names_index = np.argmax(scores)

    print("final scores {}" .format(scores))
    intent = [names[names_index]]
    print("final intent {}".format(intent))
    #print(mod.predict_proba([data]))
    print("=========================================================================================================")
    return intent

# l = ["give me faculty members in etrx","how many labs are present in etrx","what are the courses for comps department",
#      "when is the somaiya entrance test","companies hiring in etrx department","course outcomes for etrx department",
#      "extra activities for comps department"]

# for data in l:
#get_intent("how many computers are their in etrx department")