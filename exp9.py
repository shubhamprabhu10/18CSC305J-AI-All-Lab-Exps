#!/usr/bin/env python
# coding: utf-8

# In[34]:


a=input()
documents=[a]
while(a!='exit'):
    a=input()
    documents.append(a)

lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
print(lower_case_documents)


# In[35]:


sans_punctuation_documents = []
import string

for i in lower_case_documents:
    sans_punctuation_documents.append(''.join(c for c in i if c not in string.punctuation))
    
print(sans_punctuation_documents)


# In[36]:


preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
print(preprocessed_documents)


# In[37]:


frequency_list = []
import pprint
from collections import Counter

for i in preprocessed_documents:
    frequency_list.append(Counter(i))
    
pprint.pprint(frequency_list)


# In[38]:


import pandas as pd


# In[39]:


from sklearn.feature_extraction.text import CountVectorizer


# In[40]:


from sklearn.feature_extraction.text import CountVectorizer
# Create a Vectorizer Object
vectorizer = CountVectorizer()

print(vectorizer.fit(documents))


# In[41]:


# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)

# Encode the Document
vector = vectorizer.transform(documents)

# Summarizing the Encoded Texts
print("Encoded Document is:")
print(vector.toarray())


# In[ ]:




