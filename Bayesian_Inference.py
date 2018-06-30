import pandas as pd
import string 
import pprint
from collections import Counter

df = pd.read_table('C:\\Users\\steve\\Documents\\GitHub\\Udacity\\SMSSpamCollection', 
                   sep='\t', header=None, names=['label','sms_collection'])

#print (df.head())

df['label']=df.label.map({'ham':0, 'spam':1})
print (df.shape)


documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []

for i in range(len(documents)):
    lower_case_documents.append(documents[i].lower())
print(lower_case_documents)

sans_punctuation_documents = []

for i in range(len(lower_case_documents)):
    temp = lower_case_documents[i].strip(string.punctuation)
    temp = temp.replace(',','')
    sans_punctuation_documents.append(temp)
    
print(sans_punctuation_documents)

preprocessed_documents = []
for i in range(len(sans_punctuation_documents)):
    preprocessed_documents.append(sans_punctuation_documents[i].split(' '))
print(preprocessed_documents)

frequency_list = []

for i in range(len(preprocessed_documents)):
    frequency_list = Counter(preprocessed_documents[i])
    pprint.pprint(frequency_list)
    
#pprint.pprint(frequency_list)


