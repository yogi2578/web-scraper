from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import pandas as pd
dataset=pd.read_csv('data.txt',delimiter='\t')
npm=dataset.as_matrix() #numpy array
x=npm[:,0]    #sentence to classify
y=npm[:,2]   # output token_pattern=r'\b\w+\b',
# z=np.array((x,y)).transpose()
z=zip(x,y)
train=z[0:120]
test=z[120:176]
cl = NaiveBayesClassifier(train)
cl.accuracy(test)