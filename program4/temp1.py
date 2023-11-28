# Today's problem - Consider some same domain questions and answers of a use case.
# Eg. 
#     Q1) Whata are the courses run by JMI?
#     A1) JMI runs the courses of B.Tech, M.Tech, M.B.A, etc.
#     Q2) Where is JMI located?
#     A2) JMI is located Jamia Nagar, New Delhi.

# Given a new question, find out the closest answer. Generate BOW vectors for the new question and find the most similar answer
# using cosine similarity.


import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Given questions and answers
questions = [
    "What are the courses run by JMI?",
    "Where is JMI located?"
]

answers = [
    "JMI runs the courses of B.Tech, M.Tech, M.B.A, etc.",
    "JMI is located in Jamia Nagar, New Delhi."
]

# Create BOW vectors using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(questions + answers)
bow_vectors = X.toarray()

print(bow_vectors)

# New question
new_question = "Tell me about JMI's courses."

# Convert new question to BOW vector
new_question_vector = vectorizer.transform([new_question]).toarray()

# Calculate cosine similarity between new question and existing questions
similarities = cosine_similarity(new_question_vector, bow_vectors[:len(questions)])[0]

# Find the index of the most similar question
most_similar_index = np.argmax(similarities)

# Get the corresponding answer
closest_answer = answers[most_similar_index]

print("New Question: ",new_question)
print(f"Closest Answer: , {closest_answer}")