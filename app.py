import pickle
from college_bot import slotdata
from college_bot import small_talk
import joblib
import logging
logging.basicConfig(filename="test.log", format="%(asctime)s:%(levelname)s:%(message)s" , level=logging.DEBUG)
import time 
import re
import json
import random
with open('college_bot/db_dict.pickle', 'rb') as handle:
    db_dict = pickle.load(handle)

def get_intent_and_entity(query):

    intent = slotdata.get_intent(query)
    intent = str(intent)
    intent = re.sub(r'[^a-zA-Z0-9]', "", intent)
    entity = slotdata.get_NER(query)
    return intent,entity

def small_talk_intent(query):
    r = small_talk.small_talk_replies(query)
    return r
    
def FAQ_intent(intent,entity):
    
    reply = repr(db_dict[entity][intent])
    print(type(reply))
    reply = reply.replace("{"," ")
    reply = reply.replace("}"," ")

    return reply

def dialog_management(query):
    
    with open("D:\projects\col_chatbot\intentlistdata", 'r') as outfile:
         x = outfile.read()
    intent_list = json.loads(x)

    with open("D:\projects\col_chatbot\entitylistdata", 'r') as outfile:
        x = outfile.read()
    entity_list = json.loads(x)

    if len(intent_list) == 5:
        intent_list = []
    if len(entity_list) == 5:
        entity_list = []

    logging.debug("**********************************************************************************************************************")
    logging.debug("User_query: {}" .format(query))

    query = query.lower()
    mod = joblib.load('college_bot/small_talk_classification.joblib')
    result = mod.predict([query])
    print(result)     
    logging.debug("ques_classification: {} " .format(result))
    
    #try:
    if result == ['small_talk']:#small talk
        try:
            r = small_talk_intent(query)
            logging.debug("BOT: {}" .format(small_talk.small_talk_replies(query)))
            return r
        except:
            x = "can you please rephrase"
            return x
        
    if result ==['question']:#normal talk
            intent, entity = get_intent_and_entity(query)

            print("intent {}" .format(intent))
            print("entity {}" .format(entity))

            if intent == "" and entity == "":
                q = ["I cannot understand you",
                        "can you be a bit more clear ?",
                        "please rephrase the question",
                        "could you say that again ?",
                        "I am sorry , I cannot understand you",
                        ]
                return random.choice(q)

            if entity != "": #we have a new entity
                entity_list.append(entity) #add the entity to the list
            else:#if we donot have a new entity
                try:
                    entity = entity_list[-1]
                    entity_list.append(entity) #repeat the last entity in the list 

                except IndexError:
                    #if the list was already empty,we need the user to specify it the first time
                    q = ["please specifiy the department you want information about ",
                        "you have not specified a department","please give department" ,
                        "for what branch do you want this value ? ",
                        "For which branch ?" , "Branch ?"] 
                    return random.choice(q)
                    logging.debug("BOT: please specifiy the department you want information about ")

            if intent != "":
                intent_list.append(intent)
            else:
                try:
                    intent = intent_list[-1]
                    intent_list.append(intent)
                except IndexError:
                    q = ["please specify what exatly you need to know","you need to specify your question again",
                    "I am sorry but i dont understand you","could you say that again ?"]
                    return random.choice(q)
                    logging.debug("BOT: please specify what exatly you need to know")

            logging.debug("BOT: {}" .format(db_dict[entity][intent]))

            print("intent_list: {}".format(intent_list)) 
            print("entity_list: {}".format(entity_list))

            with open("entitylistdata", 'w') as outfile:
                json.dump(entity_list, outfile)
            with open("intentlistdata","w") as outfile:
                json.dump(intent_list,outfile)
    
            print(db_dict[entity][intent])
            
            logging.debug("intent_list: {} " .format(intent_list))
            logging.debug("entity_list: {}" .format(entity_list))
            #return db_dict[entity][intent]
            x = FAQ_intent(intent,entity)
            return x

    # except:

    #     print("eroor")
    #     q = ["I cannot understand you",
    #                         "can you be a bit more clear ?",
    #                         "please rephrase the question",
    #                         "could you say that again ?",
    #                         "I am sorry , I cannot understand you",
    #                         ]
    #     logging.debug("BOT: please rephrase the question")
    #     return random.choice(q)
    

