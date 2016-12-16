import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import sys
from nltk.stem.porter import PorterStemmer


reload(sys)
sys.setdefaultencoding('utf8')

def preprocess_text(text):
    porter_stemmer = PorterStemmer()
    stop = set(stopwords.words('english'))
    cleanup = " ".join(filter(lambda word: word.lower() not in stop, text.split()))
    cleanup = cleanup.encode('ascii','ignore');
    text = text.encode('ascii', 'ignore');
    stemmed = [porter_stemmer.stem(word) for word in text.lower().split()]
    UNCOMMENT THIS LINE TO TRY STOP WORDS
    # stemmed = [porter_stemmer.stem(word) for word in cleanup.lower().split()]
    stem_clean = " ".join(stemmed)
    return stem_clean

knn = KNeighborsClassifier(n_neighbors=1)
dataset=pd.read_csv('data.txt',delimiter='\t')
npm=dataset.as_matrix() #numpy array
x=npm[:,0]    #sentence to classify
q=[]#np.empty(176,dtype="string")
i=0
for line in x:
    q.append(preprocess_text(line))
    i+=1
r= np.asarray(q)
y=npm[:,2]   # output token_pattern=r'\b\w+\b',
# vectorizer=CountVectorizer(ngram_range=(2,2), min_df = 0.01, max_df = 0.99)
tvectorizer=TfidfVectorizer(ngram_range=(2,2), min_df = 0.01, max_df = 0.99)
bigram = tvectorizer.fit_transform(r)
trainx=bigram[0:120,:]
trainy=y[0:120]
testx=bigram[120:176,:]
testy=y[120:176]
knn.fit(trainx,trainy)
print knn.score(testx,testy)
# pred = knn.predict(testx)
# print np.mean(testy == pred)
# p=knn.predict(unigram)
# scores= cross_val_score(knn, unigram, y, cv=5)
# print scores.mean()