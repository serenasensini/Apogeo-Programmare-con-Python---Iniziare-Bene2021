# NLTK

# pip install nltk
# nltk.download('vader_lexicon')
# nltk.download('punkt')


from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
import nltk.sentiment.util
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# ENGLISH - VADER

frasi = ["It was a great experience",
         "Bad acting, bad music and especially bad taste",
         "This is the best movie created so far",
         "It's a waste of time",
         "Well directed, well produced",
         "I love the photography and the script is amazing",
         "Truly disappointed from this product",
         "All the characters are beautifully executed"
         "Unfortunately I didn't like it at all",
         "Horrid acting and mediocre script, I'm unhappy"]


type(frasi)

sid = SentimentIntensityAnalyzer()
for sentence in frasi:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()

# ENGLISH - Naïve Bayes

train = [("It was a great experience", "positive"),
         ("Bad acting, bad music and especially bad taste", "negative"),
         ("This is the best movie created so far", "positive"),
         ("It's a waste of time", "negative"),
         ("Well directed, well produced, I like it", "positive"),
         ("I love the photography and the script is amazing", "positive"),
         ("Truly disappointed from this product", "negative"),
         ("All the characters are beautifully executed", "positive"),
         ("Unfortunately I didn't like it at all", "negative"),
         ("Horrid acting and mediocre script, I'm unhappy", "negative")]

type(train)

dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))

t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]

classifier = nltk.NaiveBayesClassifier.train(t)

test_data = "This book is simply terrible, I am horrified"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}

print(classifier.classify(test_data_features))

test_data2 = "Wonderful movie, is really incredible"
test_data_features2 = {word.lower(): (word in word_tokenize(test_data2.lower())) for word in dictionary}

print(classifier.classify(test_data_features2))


# ITALIANO - Naïve Bayes

train2 = [("E' stata una bella esperienza", "positive"),
         ("Male recitato, male interpretato, pessimo", "negative"),
         ("Il miglior film che ho mai visto, incredibile", "positive"),
         ("Una perdita di tempo", "negative"),
         ("Ben diretto, ben recitato, mi è piaciuto, bellissimo", "positive"),
         ("Mi è piaciuta la fotografia e gli attori sono fantastici", "positive"),
         ("Davvero deluso di questo film", "negative"),
         ("Tutti i personaggi sono belli e ben interpretati", "positive"),
         ("Purtroppo faceva schifo", "negative"),
         ("Orribile e mediocre, sono orripilato", "negative")]

dictionary = set(word.lower() for passage in train2 for word in word_tokenize(passage[0]))

t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train2]

classifier = nltk.NaiveBayesClassifier.train(t)

test_data = "Questo libro era terribile, sono orripilato"
test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}

print(classifier.classify(test_data_features))

test_data2 = "Bellissimo, è stato incredibile"
test_data_features2 = {word.lower(): (word in word_tokenize(test_data2.lower())) for word in dictionary}

print(classifier.classify(test_data_features2))

# scikit-learn

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_excel('reviews_en.xlsx', names=["text", "label"], encoding='utf8')
print(df.head())

print(df.groupby('label').describe())

cl = {'positive': 1, 'negative': 0}
df['label'] = df['label'].map(cl)

corpus = []
for i in range(0, 1998):
    text = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    corpus.append(text)

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features = 2000)
x = cv.fit_transform(corpus).toarray()
cl = df['label'].values

x_train, x_test, y_train, y_test = train_test_split(x, cl, test_size = 0.3, random_state = 12345)

# Regressione Logistica
lr = LogisticRegression()
lr.fit(x_train, y_train)
lr_pred = lr.predict(x_test)
print(classification_report(y_test, lr_pred))

y = ["It was a great experience"]
y = cv.transform(y)
print(lr.predict(y))
