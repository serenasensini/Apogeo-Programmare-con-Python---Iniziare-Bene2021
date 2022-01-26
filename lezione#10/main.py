# # NLTK
#
# # pip install nltk
#
# from nltk.tokenize import word_tokenize
# import nltk.sentiment.util
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
# nltk.download('vader_lexicon')
# nltk.download('punkt')
# nltk.download('stopwords')
#
# # ENGLISH - VADER
#
# print("####################")
# print("SENTIMENT ANALYSIS")
# print("####################")
#
# frasi = ["It was a great experience",
#          "Bad acting, bad music and especially bad taste",
#          "This is the best movie created so far",
#          "It's a waste of time",
#          "Well directed, well produced",
#          "I love the photography and the script is amazing",
#          "Truly disappointed from this product",
#          "All the characters are beautifully executed"
#          "Unfortunately I didn't like it at all",
#          "Horrid acting and mediocre script, I'm unhappy"]
#
# type(frasi)
#
# print("####################")
# print("Risultato del SentimentIntensityAnalyzer:")
# print("####################")
# sid = SentimentIntensityAnalyzer()
# for sentence in frasi:
#     print(sentence)
#     ss = sid.polarity_scores(sentence)
#     for k in ss:
#         print('{0}: {1}, '.format(k, ss[k]), end='')
#     print()
#
# # ENGLISH - Naïve Bayes
#
# print("####################")
# print("SENTIMENT ANALYSIS CON NAIVE BAYES (NLTK) IN INGLESE")
# print("####################")
#
# train = [("It was a great experience", "positive"),
#          ("Bad acting, bad music and especially bad taste", "negative"),
#          ("This is the best movie created so far", "positive"),
#          ("It's a waste of time", "negative"),
#          ("Well directed, well produced, I like it", "positive"),
#          ("I love the photography and the script is amazing", "positive"),
#          ("Truly disappointed from this product", "negative"),
#          ("All the characters are beautifully executed", "positive"),
#          ("Unfortunately I didn't like it at all", "negative"),
#          ("Horrid acting and mediocre script, I'm unhappy", "negative")]
#
# type(train)
#
# dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
# print(dictionary)
# # la riga precedente è uguale a questa che segue...
# # dictionary2 = {}
# # bag_of_words = set()
# # for tupla in train:
# #     for word in word_tokenize(tupla[0]):
# #         word = word.lower()
# #         bag_of_words.add(word)
# # print(bag_of_words)
#
# t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
# print("####################")
# print("Insieme di test:")
# print(t)
# print("####################")
# classifier = nltk.NaiveBayesClassifier.train(t)
#
# test_data = "This book is simply terrible, I am horrified"
# test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
# print("####################")
# print("Risultato del test #1:")
# print("####################")
# print(classifier.classify(test_data_features))
#
# test_data2 = "Wonderful movie, is really incredible"
# test_data_features2 = {word.lower(): (word in word_tokenize(test_data2.lower())) for word in dictionary}
# print("####################")
# print("Risultato del test #2:")
# print("####################")
# print(classifier.classify(test_data_features2))
#
# test_data3 = "It was a huge disaster, I've seen a lot of movies that are much better than this one"
# test_data_features3 = {word.lower(): (word in word_tokenize(test_data2.lower())) for word in dictionary}
# print("####################")
# print("Risultato del test #3:")
# print("####################")
# print(classifier.classify(test_data_features3))
#
# # ITALIANO - Naïve Bayes
#
# print("####################")
# print("SENTIMENT ANALYSIS CON NAIVE BAYES (NLTK) IN ITALIANO")
# print("####################")
#
# train2 = [("E' stata una bella esperienza", "positive"),
#           ("Male recitato, male interpretato, pessimo", "negative"),
#           ("Il miglior film che ho mai visto, incredibile", "positive"),
#           ("Una perdita di tempo", "negative"),
#           ("Ben diretto, ben recitato, mi è piaciuto, bellissimo", "positive"),
#           ("Mi è piaciuta la fotografia e gli attori sono fantastici", "positive"),
#           ("Davvero deluso di questo film", "negative"),
#           ("Tutti i personaggi sono belli e ben interpretati", "positive"),
#           ("Purtroppo faceva schifo", "negative"),
#           ("Orribile e mediocre, sono orripilato", "negative")]
#
# dictionary = set(word.lower() for passage in train2 for word in word_tokenize(passage[0]))
#
# t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train2]
#
# classifier = nltk.NaiveBayesClassifier.train(t)
#
# test_data = "Questo libro era terribile, sono orripilato"
# test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
# print("####################")
# print("Risultato del test #1 con Naive Bayes:")
# print("####################")
# print(classifier.classify(test_data_features))
#
# test_data2 = "Bellissimo, è stato incredibile"
# test_data_features2 = {word.lower(): (word in word_tokenize(test_data2.lower())) for word in dictionary}
# print("####################")
# print("Risultato del test #2 con Naive Bayes:")
# print("####################")
# print(classifier.classify(test_data_features2))
#
# # scikit-learn
#
# print("####################")
# print("SENTIMENT ANALYSIS CON SCIKIT-LEARN IN INGLESE")
# print("####################")
#
# import pandas as pd
# import re
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report
# from sklearn.feature_extraction.text import CountVectorizer
#
#
# # carico i dati presenti nel dataset Excel all'interno di "df"
# df = pd.read_excel('reviews_en.xlsx', names=["text", "label"])
# # stampo  le prime 5 righe
# print("####################")
# print("Stampo le prime 5 righe del dataset")
# print("####################")
# print(df.head())
#
# # descrivo le info dei valori presenti nella colonna "label"
# print("####################")
# print("Descrizione della colonna 'label'")
# print("####################")
# print(df.groupby('label').describe())
#
# # creo un'associazione tra positivo e negativo associandoli a 1 e 0
# cl = {'positive': 1, 'negative': 0}
#
# # sostituisco questi valori con quelli numerici dell'associazione
# df['label'] = df['label'].map(cl)
# print("####################")
# print("Dataset dopo la sostituzione:")
# print("####################")
# print(df)
#
# # pre-processing dei dati
# corpus = []
# for i in range(0, 1998):
#     # per ogni frase, mi tengo solo le stringhe senza punteggiatura
#     text = re.sub('[^a-zA-Z]', ' ', df['text'][i])
#     # riduco tutte le frasi in minuscolo
#     text = text.lower()
#     text = text.split()
#     # uso lo stemmer di Porter per ridurre alla radice tutte le parole presenti nelle frasi
#     ps = PorterStemmer()
#     # per ogni parola presente nella frase, se questa non è presente nell'elenco
#     # di stopwords, la riduco alla radice
#     text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
#     text = ' '.join(text)
#     # aggiungo le frasi al corpus
#     corpus.append(text)
#
# print(corpus)
#
# cv = CountVectorizer(max_features=2000)
# print("rr")
# x = cv.fit_transform(corpus).toarray()
# print("fddfdf")
# cl = df['label'].values
#
# print("prova")
# x_train, x_test, y_train, y_test = train_test_split(x, cl, test_size=0.3, random_state=12345)
#
# # Regressione Logistica
# lr = LogisticRegression()
# lr.fit(x_train, y_train)
# lr_pred = lr.predict(x_test)
# print("####################")
# print("Matrice di classificazione:")
# print("####################")
# print(classification_report(y_test, lr_pred))
#
# y = ["It was a great experience"]
# y = cv.transform(y)
# print("####################")
# print("Risultato della predizione:")
# print("####################")
# print(lr.predict(y))

# Database
## Postgres with Psycopg2

print("####################")
print("DATABASE - POSTGRES CON PSYCOPG2:")
print("####################")

import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",
                                database="test",
                                user="postgres",
                                password="password")

        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_users():
    """ query data from the users table """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",
                                database="test",
                                user="postgres",
                                password="password")

        # create a cursor
        cur = conn.cursor()
        cur.execute("SELECT user_id, user_name FROM users ORDER BY user_name")
        print("The number of users: ", cur.rowcount)
        table = cur.fetchall()

        for row in table:
            print(row)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_user(user_name):
    """ insert a new user into the users table """
    conn = None
    user_id = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",
                                database="test",
                                user="postgres",
                                password="password")

        # create a cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO users(user_name) VALUES(%(user_name)s)", {"user_name": "john12"},)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id


def delete_user(part_id):
    """ delete user by user_id """
    conn = None
    rows_deleted = 0
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost",
                                database="test",
                                user="postgres",
                                password="password")

        # create a cursor
        cur = conn.cursor()
        # execute the DELETE statement
        cur.execute("DELETE FROM users WHERE user_id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


if __name__ == '__main__':
    connect()
    get_users()
    insert_user("frank89")
    delete_user(2)

# MySQL con SQLAlchemy

import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://user:pwd@localhost/test", echo=False)
metadata = db.MetaData()

# USO SELECT
persone = db.Table('users', metadata, autoload=True, autoload_with=engine)
# Equivalent to 'SELECT * FROM PERSONE'
query = db.select([persone])
connection = engine.connect()
result = connection.execute(query)
for row in result:
    print(row)

# QUERY
t = db.text("SELECT * FROM persone")
result2 = connection.execute(t)
for row in result2:
    print(row)
