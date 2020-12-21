# Twitter-Sentiment-Analysis-using-RNN
Problem Definition- Following set of algorithms achieves binary classification of tweets for sentiment analysis in order to determine the mood or opinions shared by the users on twitter. 

Applications- Sentiment analysis has got wide applications in the analysis of survey response, product review or movie review. The usecase of this could be for industries to find out what really people think about their products and can take data driven decisions to improve their businesses. 

Following are the important steps of data pipeline to do the sentiment classificationinvolved-
1. Data Acquisition- I used Sentiment140 dataset provided by Stanford which is also available on Kaggle. 
The data is a CSV with emoticons removed. Data file format has 6 fields:
0 - the polarity of the tweet (0 = negative, 1 = positive)
1 - the id of the tweet (2087)
2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
3 - the query (lyx). If there is no query, then this value is NO_QUERY.
4 - the user that tweeted (robotickilldozr)
5 - the text of the tweet (Lyx is cool)

2. Data preprocessing- Next important step after acquiring dataset was to clean the data and make it suitable for classification purpose. In this step the tweet sentences were formatted uniformly to make their length < 280 characters which is within the character limit of twitter by removing unnecessary part of the sentencs such as stop words, hyperlinks, removing inflection in a word, normalizing it to lower or upper case case to maintain the uniformity.
3. Data split- After preprocessing, the entire dataset was splitted into training, test and validation which is used to optimize the hyperparameters of our models
3. Vectorization- Since the words can't be fed as it is to any ML model, word2vec embedding was used along with Tokenization and lemmatization to create a meaningful mathematical representation of words in a text corpus
4. Classification- At the end, the vectorized tweets were given as an input to various ML algorithms such as SVM,logistic regression, baseline NN and RNN for classification, where RNN outperformed other ML algorithms and gave up to 84% test accuracy

Tools used: Keras, Tensorflow, Google Colab



