# Today's problem - Consider some same domain questions and answers of a use case.
# Eg. 
#     Q1) Whata are the courses run by JMI?
#     A1) JMI runs the courses of B.Tech, M.Tech, M.B.A, etc.
#     Q2) Where is JMI located?
#     A2) JMI is located Jamia Nagar, New Delhi.

# Given a new question, find out the closest answer. Generate BOW vectors for the new question and find the most similar answer
# using cosine similarity.

# Solution:
#     1. Create a corpus of questions and answers.
#     2. Create a BOW vector for each question and answer.
#     3. Create a BOW vector for the new question.
#     4. Find the most similar answer using cosine similarity.

# Importing the libraries
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Importing the dataset
dataset = pd.read_csv('qa.csv')
dataset = dataset.dropna()
dataset = dataset.reset_index(drop=True)

# Cleaning the texts
corpus = []
for i in range(0, len(dataset)):
    question = re.sub('[^a-zA-Z]', ' ', dataset['question'][i])
    question = question.lower()
    question = question.split()
    ps = PorterStemmer()
    question = [ps.stem(word) for word in question if not word in set(stopwords.words('english'))]
    question = ' '.join(question)
    answer = re.sub('[^a-zA-Z]', ' ', dataset['answer'][i])
    answer = answer.lower()
    answer = answer.split()
    ps = PorterStemmer()
    answer = [ps.stem(word) for word in answer if not word in set(stopwords.words('english'))]
    answer = ' '.join(answer)
    corpus.append(question + ' ' + answer)

# Creating the BOW model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()

# Creating the BOW model for new question
new_question = 'Where is JMI located?'

new_question = re.sub('[^a-zA-Z]', ' ', new_question)
new_question = new_question.lower()
new_question = new_question.split()
ps = PorterStemmer()
new_question = [ps.stem(word) for word in new_question if not word in set(stopwords.words('english'))]
new_question = ' '.join(new_question)

new_corpus = []
new_corpus.append(new_question)
new_X = cv.transform(new_corpus).toarray()

# Finding the most similar answer
from sklearn.metrics.pairwise import cosine_similarity
cosine_similarities = cosine_similarity(new_X, X)
most_similar_answer = np.argmax(cosine_similarities)

print('The most similar answer is: ' + dataset['answer'][most_similar_answer])

# The most similar answer is: JMI is located in Jamia Nagar, New Delhi.

