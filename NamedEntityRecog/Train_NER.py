from __future__ import unicode_literals, print_function
import pickle
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
def ner_trainig():
    with open (r'C:\Users\Akash\Desktop\be_proj\Data\NER_training_data.pickle', 'rb') as fp:
        TRAIN_DATA = pickle.load(fp)

    LABEL = ['BRANCH']
    nlp = spacy.blank('en')#created a blank model
    ner = nlp.create_pipe('ner')#created a pipeline  ner
    nlp.add_pipe(ner)#added NER to the spcy pipeline
    for l in LABEL:
        ner.add_label(l)#added labels for the component
    optimizer = nlp.begin_training()

    n_iter = 10
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
                random.shuffle(TRAIN_DATA) #shuffled the dataset
                losses = {}
                batches = minibatch(TRAIN_DATA, size=compounding(1.0, 4.0, 1.001))
                for batch in batches:

                    texts, annotations = zip(*batch)
                    nlp.update(texts, annotations, sgd=optimizer,
                            drop=0.35,
                            losses=losses)
                print('Losses', losses)

    #test_text = "how many electronics students are there in IT branch ?"
    #doc = nlp(test_text)
    #print("Entities in '%s'" % test_text)
    #for ent in doc.ents:
    #    print(ent.label_, ent.text)

    nlp.meta["name"] = "NER_mod"  # rename model
    nlp.to_disk(r"D:\projects\col_chatbot - Copy\college_bot\NERdata")

#text = "how many electronics students are there in IT branch ?"
#doc = model(text)
#print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

