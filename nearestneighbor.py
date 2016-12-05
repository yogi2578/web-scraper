import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors=1)
dataset=pd.read_csv('data.txt',delimiter='\t')
npm=dataset.as_matrix() #numpy array
x=npm[:,0]    #sentence to classify
y=npm[:,2]   # output token_pattern=r'\b\w+\b',
vectorizer=CountVectorizer(ngram_range=(3,3), min_df = 0.01, max_df = 0.99)
unigram = vectorizer.fit_transform(x)
trainx=unigram[0:120,:]
trainy=y[0:120]
testx=unigram[120:176,:]
testy=y[120:176]
knn.fit(trainx,trainy)
pred = knn.predict(testx)

# print np.mean(testy == pred)
# p=knn.predict(unigram)
# scores= cross_val_score(knn, unigram, y, cv=5)
# print scores.mean()