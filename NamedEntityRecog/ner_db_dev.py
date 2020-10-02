import pandas as pd
import os
os.chdir(r"C:\Users\Akash\Desktop\be_proj_py")
import spacy 
from functools import reduce
import random 
import argparse
import sys
import json
import pickle
nlp = spacy.load("en_core_web_sm") 

data_file = pd.read_csv("chatbot_training_data.csv")
ner_data_1 = list(data_file['NER DATA'].dropna())

branch = ['comps' , "IT" , "EXTC" , "Mech", "computer", "cs", "etrx" , "mechanical"]
updated_branch = []
for data in ner_data_1:
    updated_branch.append(data)
    for name in branch:
        new_sentence = data.replace("electronics" , name)
        updated_branch.append(new_sentence)
        
random.shuffle(updated_branch)    
updated_ner = pd.DataFrame(updated_branch)
#print(len(updated_ner))
if os.path.isdir("Data") :
    updated_ner.to_csv('Data/NER raw data.csv' , index = False, header=['Updated_NER'])
else:
    os.mkdir("Data")
    updated_ner.to_csv('Data/NER raw data.csv' , index = False, header=['Updated_NER'])
count = 0
Sentence = []
Name = []
PoS = []
Tag = []

for data in updated_branch:
    count = count +1 
    sen = "sentence " + str(count)
    list_name = []
    sen_no = []
    list_pos = []
    list_tag = []
    sen_no.append(sen)
    doc = nlp(data)
    for token in doc:
        list_pos.append(token.pos_)
        token = str(token)
        if token == "comps" or token =="IT" or token == "EXTC" or token == "Mech" or token == "computer" or token == "cs" or token == "etrx" or token =="mechanical":
            list_tag.append("BRANCH")
        else: list_tag.append("O")
        sen_no.append("None")
        list_name.append(token)
    list_name.append(".")
    list_pos.append(".")
    list_tag.append("O")
    Tag.append(list_tag)
    Name.append(list_name)
    PoS.append(list_pos)
    Sentence.append(sen_no)
PoS = reduce(lambda z, y :z + y, PoS) 
Name = reduce(lambda z, y :z + y, Name) 
Sentence = reduce(lambda z, y :z + y, Sentence) 
Tag = reduce(lambda z, y :z + y, Tag) 
sen_no = pd.DataFrame(Sentence)
list_tag = pd.DataFrame(Tag)
list_name = pd.DataFrame(Name)
list_pos = pd.DataFrame(PoS)

data = {"Sentence" : Sentence , "Name": Name , "PoS" : PoS , "Tag" : Tag}
df = pd.DataFrame(data)
df.to_csv('Data/NER strucutred data.csv' , index = False , header = "PoS" )




def tsv_to_json_format(input_path,output_path,unknown_label):
    try:
        f=open(input_path,'r',encoding = "utf-8") # input file
        fp=open(output_path, 'w') # output file
        data_dict={}
        annotations =[]
        label_dict={}
        s=''
        start=0
        for line in f:
            if line[0:len(line)-1]!='.\tO':#cheak if a line is empty
                word,entity=line.split('\t')
                s+=word+" "
                entity=entity[:len(entity)-1]
                if entity!=unknown_label:
                    if len(entity) != 1:
                        d={}
                        d['text']=word
                        d['start']=start
                        d['end']=start+len(word)-1  
                        try:
                            label_dict[entity].append(d)
                        except:
                            label_dict[entity]=[]
                            label_dict[entity].append(d) 
                start+=len(word)+1
              
            else:
                data_dict['content']=s
                s=''
                label_list=[]
                for ents in list(label_dict.keys()):
                    for i in range(len(label_dict[ents])):
                        if(label_dict[ents][i]['text']!=''):
                            l=[ents,label_dict[ents][i]]
                            for j in range(i+1,len(label_dict[ents])): 
                                if(label_dict[ents][i]['text']==label_dict[ents][j]['text']):  
                                    di={}
                                    di['start']=label_dict[ents][j]['start']
                                    di['end']=label_dict[ents][j]['end']
                                    di['text']=label_dict[ents][i]['text']
                                    l.append(di)
                                    label_dict[ents][j]['text']=''
                            label_list.append(l)                          
               
                for entities in label_list:
                    label={}
                    label['label']=[entities[0]]
                    label['points']=entities[1:]
                    annotations.append(label)
                data_dict['annotation']=annotations
                annotations=[]
                json.dump(data_dict, fp)
                fp.write('\n')
                data_dict={}
                start=0
                label_dict={}
    except Exception as e:
        #logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None

tsv_to_json_format(r"C:\Users\Akash\Desktop\be_proj_py\Data\NER strucutred data - NER strucutred data.tsv",r'C:\Users\Akash\Desktop\be_proj_py\Data\NER_training_data.json','abc')


def main(input_file=r"C:\Users\Akash\Desktop\be_proj_py\Data\NER_training_data.json", output_file=r"C:\Users\Akash\Desktop\be_proj_py\Data\NER_training_data.pickle"):
    try:
        training_data = []
        lines=[]
        with open(input_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            for annotation in data['annotation']:
                point = annotation['points'][0]
                labels = annotation['label']
                if not isinstance(labels, list):
                    labels = [labels]

                for label in labels:
                    entities.append((point['start'], point['end'] + 1 ,label))


            training_data.append((text, {"entities" : entities}))

        print(training_data)

        with open(output_file, 'wb') as fp:
            pickle.dump(training_data, fp)

    except Exception as e:
        #logging.exception("Unable to process " + input_file + "\n" + "error = " + str(e))
        return None
#if __name__ == '__main__':
 #   plac.call(main)
main()   