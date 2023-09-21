# -*- coding: utf-8 -*-
"""Anime_recommendation_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d0WhNs8EFMSEN8U4CywFtaiEH3AUfI0J
"""

import pandas as pd
import numpy as np
import ast

df=pd.read_csv("/content/drive/MyDrive/projects/anime.csv")

df.head(1)

df.info()

df=df[['title','mediaType','description','tags','contentWarn']]

df.head(1)

df.isnull().sum()

df.dropna(inplace=True)

df.iloc[0].tags

df.iloc[0].mediaType

df.iloc[0].contentWarn

df['description']=df['description'].apply(lambda x:x.split())

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i)
    return L

df['tags']=df['tags'].apply(convert)
df['contentWarn']=df['contentWarn'].apply(convert)



df.head(1)

df['tags']=df['tags'].apply(lambda x:[i.replace(" ","") for i in x])
df['contentWarn']=df['contentWarn'].apply(lambda x:[i.replace(" ","") for i in x])

df['mediaType']=df['mediaType'].apply(lambda x:x.split())

df.head(1)

df['keys']=df['description']+df['tags']+df['mediaType']+df['contentWarn']

df.head(1)

animes=df[['title','keys']]

animes.head()

animes['keys']=animes['keys'].apply(lambda x:" ".join(x))

animes.head(3)

animes['keys'][0]

animes['keys']=animes['keys'].apply(lambda x: x.lower())

import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps=PorterStemmer()

def stem(text):
    y=[]
    words=word_tokenize(text)
    for i in words:
        y.append(ps.stem(i))
    return " ".join(y)

for i in animes['keys']:
    i=ps.stem(i)

animes['keys']=animes['keys'].apply(stem)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=6000,stop_words='english')

vectors=cv.fit_transform(animes['keys']).toarray()

from sklearn.metrics.pairwise import cosine_similarity

similarity=cosine_similarity(vectors)

similarity[animes[animes['title']=='ERASED'].index[0]][animes[animes['title']=='ERASED'].index[0]]

def recommend(anime):
    try:
        anime_index=animes[animes['title']==anime].index[0]
        distances=similarity[anime_index]
        anime_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1]) [0:5]

        for i in anime_list:
            print(animes.iloc[i[0]].title)

    except IndexError:
             print (f'"{anime}" is not present in our record. :/')

recommend("ERASED")

animes.head()

import pickle

pickle.dump(animes.to_dict(),open('animes_dict.pkl','wb'))

pickle.dump(similarity,open('similar.pkl','wb'))