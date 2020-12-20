# Twitter-Sentiment-Analysis-using-RNN
In this project I did binary classification of tweets for sentiment analysis in order to determine the mood or opinions shared by the users on twitter. As we all are aware, sentiment analysis has got wide applications in the analysis of survey response, product review or movie review. With this, industry can get to know what really people think about their products and can take data driven decisions to improve. 

Problem Definition- Binary classification of tweets based on their sentiments/ moods using various machine learning algorithms.
Important steps involved-
1. Data preprocessing- length < 280 characters, lower case, removal of unnecessary part such as hyperlinks, stop words, inflection in words
2. Data split- training, test and validation to optimize hyperparameters
3. Vectorization- using word2vec embedding along with Tokenization and lemmatization
4. Classification- using various ML algorithms such as SVM,logistic regression, baseline NN, RNN where RNN outperforms other ML algorithms and give up to 84% test        accuracy
Tools used: Keras, Tensorflow, Google Colab
Data: Sentiment140 by Stanford


