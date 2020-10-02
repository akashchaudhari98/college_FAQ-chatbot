# college_FAQ-chatbot

Chatbot working 

The chatbot has multiple working parts- 1) intent classfication 
                                        2) entity classfication 
                                        3) small talk 
                                        4) dialog managment 

## Work flow - 
1) user enters a query 
2) query gets classified as question or small talk 
3) if small talk , then the small talk module is called the approprite reply is returned and the bot awaits the next user text
4) if question , then the query is passes to the slotdata.py file to get intent and entity values 
4) if both intent and entity are not found by the model then the query is probably wrong and the bot replies accordingly " i cannot understand " 
5) if intent and entity are both found, the bot pings the database for the intent ( "Faculty","infrastructure","syllabus","admissions",
            "placements","programes","student body") and entity( etrx,comps,extc,it,mech ) and replies with the approprite data
6) the bot also rememebers the previous intent and entity values ( using python tuples) of the user  for upto 5 conversation turns , after which the session ends and the 
            intent and entity tuples are reset 
7) if incase the user specifies the entity ( branch ) but not the intent , then the bot refers to the intent tuple and retirves the intent value 
            for the last conversation turn 
8) similary incase the user specifies the intent but not the entity then the bot retirves the previous entity and uses it as the current entity and
            updates the entity tuple accordingly 
9) incase the intent and entity tuple are empty and the user does not specify either one , the bot asks for the respective value 


## Intent classfication
the intent classfication dataset is hand made and has 131 questions with their corresponding intents 
we have 7 intents in total ["Faculty","infrastructure","syllabus","admissions",
                             "placements","programes","student body" ]
The intent classfication is a multi class classfication problem , meaning the we have to classify text into more than one intent 
The algorithm used to do this classfication is stocastic gradient descent optimisation with a log loss function  ( read about it on sklearn)
the problem faced here is of negative class , that is saying the text does not belong to any of the classes 
this is solved by employing a scoring method , in which we have created a list of keywords for every single intent, whenever the query is passes to the intent model 
all the words in the query are compared with all the keywords in every intent list , for every match that perticlular intent is given a score of +1 , then the query is
passed to the trained model , the output intent value by the trained model is given a score of +2 after this which ever intent has the highest score is returned as the
final intent


## NER classfication
NER stands for named entity recognision and is used to identify branch the user is talking about .
we have used spacys NER model to train this dataset which was also hand written 


## Small talk 
first step is to identify if the query is actually small talk and to do this a binary classification model was trained , the algorithm used in the model is SVM 
we use TFIDF for text representation and then apply SVM on that text , once we have identifed that the query is small talk , we convert all the small talk questions in 
the dataset into word vectors using word2vec, we convert the query as well into a word vector , we then go on to compare the query word vector with every single small 
talk question word vecor , using consine similary we find out the most similar question and return the answer corresponding to that perticlular question as the reply 
to user query and then await user responce


## Database
It is a dctionary database, and is structured as follows - 
ETRX :{
    "etrx":{
        "intent 1": " Data for the intent",
        "intent 2": "Data for the intent",
        .
        .
        .
        "intent 7": "data"

    }
}
same thing is done for all the branches 
this database is saved as a pickle object and is opened everytime the chatbot server is turned on 


Front end 
We use a framework called bot.ui which is developed in simple HTML and CSS , to communicate with the backend, the front end makes a "GET" request, we developed an 
API to make this request using Django rest framework. 
