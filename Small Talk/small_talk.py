import pandas as pd
import gensim 
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize , word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection, svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib
from itertools import chain 
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier


def ques_classification():

    df = pd.read_csv("D:\projects\col_chatbot - Copy\college_bot\Training Data\small_talk - Sheet.csv",encoding = "utf-8")
    question = df["QUESTIONS"]
    intent = df["INTENT"]
    X = question
    y = intent


    #Encoder = LabelEncoder()
    #y = Encoder.fit_transform(y)
    #y_test = Encoder.fit_transform(y_test)
    #Tfidf_vect = TfidfVectorizer(stop_words='english')
    #X_Tfidf = Tfidf_vect.fit_transform(X)
    #Test_X_Tfidf = Tfidf_vect.transform(X_test)

    params_grid = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], "probability" : [True],
                        'C': [1, 10, 100, 1000]},
                        {'kernel': ['linear'], 'C': [1, 10, 100, 1000] ,"probability":[True] }]

    #SVM = GridSearchCV(SVC(), params_grid, cv=5)
    #SVM.fit(X_Tfidf,y)
    #predictions_SVM = SVM.predict(Test_X_Tfidf)
    #joblib.dump(SVM, 'small_talk_classification.joblib') 
    #joblib.dump(Tfidf_vect , 'tfidf_small.joblib')
    #print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, y_test)*100)

    # X = question
    # y = intent
    # my_tags = list(set(intent))
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)
    

    sgd = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    #('tfidf',TfidfVectorizer()),
                    #("svc", svm.SVC(decision_function_shape='ovo')),
                    #('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=10, max_iter= 10, tol=None)),
                    ('clf',GridSearchCV(SVC(), params_grid, cv=5))
                ])
    sgd.fit(X,y)


    joblib.dump(sgd, 'small_talk_classification.joblib') 

    #dump(Tfidf_vect , 'college_bot/tfidf_small.joblib')
#ques_classification()
def small_talk():

    data = pd.read_csv("D:\projects\col_chatbot - Copy\college_bot\Training Data\chatbot_training_data.csv" ,encoding = "utf-8")
    ans = data["small_talk_answer"].dropna() 
    ques = data["small_talk_questions"].dropna()
    ques = list(ques)
    for data in ques:
        data = re.sub(r'\W+', ' ', data)
    user_que = str("thank you ")
    user_que = re.sub(r'\W+', ' ', user_que)

    def trainin_model(ques):
        sentences = []
        for sen in ques:
            l1 = []
            for words in sen.split():
                l1.append(words)
            sentences.append(l1)
        model = Word2Vec(sentences, min_count=1 ,size=10)#training the model
        model.save('college_bot/smalltalk_model.bin')
#small_talk()
def small_talk_replies(user_que):

    def avg_sentence_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0
        for word in words:
            nwords = nwords+1
            featureVec = np.add(featureVec, model[word])
        if nwords>0:
            featureVec = np.divide(featureVec, nwords)
        return featureVec

    data = pd.read_csv("D:\projects\col_chatbot - Copy\college_bot\Training Data\chatbot_training_data.csv" ,encoding = "utf-8")
    ques = data["small_talk_questions"].dropna()
    ans = data["small_talk_answer"].dropna() 
    sentence_1_avg_vector = avg_sentence_vector(user_que.split(), model=Word2Vec.load('college_bot/smalltalk_model.bin'), num_features=10)
    sentence_1_avg_vector = sentence_1_avg_vector.reshape(1,-1)
    l1 = []
    for sen in ques:
        sentence_2_avg_vector = avg_sentence_vector(sen.split(), model=Word2Vec.load('college_bot/smalltalk_model.bin'), num_features=10)
        sentence_2_avg_vector = sentence_2_avg_vector.reshape(1,-1)
        sen1_sen2_similarity =  cosine_similarity(sentence_1_avg_vector,sentence_2_avg_vector)
        sen1_sen2_similarity = list(sen1_sen2_similarity[0])
        l1.append(sen1_sen2_similarity)
    l1 = list(chain.from_iterable(l1))
    max_val = max(l1)
    #print(max(l1) , "max value")
    #print(l1.index(max(l1)))
    print(ans[l1.index(max(l1))], "ans")
    #print(ques[l1.index(max(l1))], "ques")
    return ans[l1.index(max(l1))]
#small_talk_replies("hello")
