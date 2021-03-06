# -*- coding: utf-8 -*-
"""preprocess.ipynb

"""
import numpy as np
def remove_pattern(input_txt, pattern):
    import re
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt

def preprocessdata(df):

  #removing text which has length more than 280 char(max char limit of tweet)
  df['pre_clean_len'] = [len(t) for t in df.text]
  df[df.pre_clean_len <= 280]
  
 
  b= (df.pre_clean_len <=280) #boolean output column for hour value lying between 0 to 6 
  df=df.iloc[np.where(b)] 

  #removing hyperlinks in train data
  df['text'] = df['text'].str.replace('http\S+|www.\S+', '', case=False)
  
  #removing hyperlinks in test data
  df['text'] = df['text'].str.replace('http\S+|www.\S+', '', case=False)
  
  #removing @username in train data
  df['text'] = np.vectorize(remove_pattern)(df['text'], "@[\w]*")
  
  #1.1 Convert text to lowercase 
  df['text']=df['text'].str.lower()
  
  #Remove numbers in train data
  df.text = df.text.str.replace('\d+', '')
  
  #1.3 Remove punctuation in train data
  import string
  (str(df['text']).translate(str.maketrans("","",string.punctuation)))
  
  # remove special characters, numbers, punctuations in train data
  df['text'] = df['text'].str.replace("[%!@$^#&*?.;:+_-]", " ")
  
  #1.5 Remove stop words 
  import nltk                                
  nltk.download('stopwords')
  from nltk.corpus import stopwords
  stop = stopwords.words("english")
  
  #stop words removal from train data
  df['text']= df['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
  
  #removing short words from train, dev and test data
  df['text'] = df['text'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
  
  #Remove leading and ending whitespaces from train
  df['text'] = df['text'].str.strip() 
  
  
  #Step 2 Lemmatization in train, dev and test data            
  import nltk
  nltk.download('wordnet')
  from nltk.stem.wordnet import WordNetLemmatizer
  lmtzr = WordNetLemmatizer()
  
  lem_data = df['text'].apply(lambda x: ' '.join([lmtzr.lemmatize(word,'v') for word in x.split() ]))

  #Step 3 Tokenization in train, dev and test             
  tok_data = lem_data.apply(lambda x: x.split())
  
  return lem_data, tok_data
