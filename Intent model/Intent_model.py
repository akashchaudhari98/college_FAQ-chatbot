import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from nltk import word_tokenize
import nltk
#nltk.download('punkt')
import re
import joblib

def train_intent():
     
    df = pd.read_csv("Training Data/intent_training_data.csv")
    df.head
    question = df["QUESTIONS"]
    intent = df["INTENT"]


    def preprocess(data):

        data = data.lower()
        # stop_words =['hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
        # word_tokens = word_tokenize(data) 
        # data = [w for w in word_tokens if not w in stop_words] 
        # for w in word_tokens: 
        #     if w not in stop_words: 
        #         data.append(w) 
        # data = " ".join(data)
        data = re.sub(r'[^a-zA-Z0-9]', " ", data)
        return data

    question = question.apply(preprocess)
    X = question
    y = intent
    my_tags = list(set(intent))
    #print(my_tags)
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)

    sgd = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    #('tfidf',TfidfVectorizer()),
                    #("svc", svm.SVC(decision_function_shape='ovo')),
                    ('clf', SGDClassifier(loss='log', penalty='l2',alpha=1e-3, random_state=10, max_iter=10, tol=None)),
                ])
    sgd.fit(X, y)


    #y_pred = sgd.predict(X_test)
    
    #t = sgd.predict_proba(["of electronics department"])
    #print(t) 
    #print(sgd.predict(["what is the eligblity crieteria for addmisson in somaiya "]))   
    #print('accuracy %s' % accuracy_score(y_pred, y_test))
    joblib.dump(sgd, 'intent_model_1.joblib') 
    #print(classification_report(y_test, y_pred,target_names=my_tags))


#train_intent()

'''
calender = 0
faculty =1 
infra = 2
placement = 4
result = 5
small_talk = 6
student body = 7
syllabus = 8

'''
