import os
import csv
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, RegexpTokenizer
from sklearn.feature_extraction.text import TfidfTransformer


class KeywordExtractor:
    corpus = []


    def __init__(self, dir_path):
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.ps = PorterStemmer()
        self.lm = WordNetLemmatizer()
        self.path = dir_path
        self.all_words_per_class = set()

    def start_listing(self):
        print(self.path)
        for r, d, files in os.walk(self.path):
            i = 0
            for file in files:
                if file.endswith(".txt"):
                    i += 1
                    f_path = os.path.join(self.path, file)
                    f = open(f_path, "r", encoding="utf-8")
                    content = f.read().lower()
                    tokenized_list = self.tokenize(content)
                    filtered_list = self.remove_stop_words(tokenized_list)
                    lemma_list = self.lemmatize(filtered_list)
                    final_list = self.stem(lemma_list)

                    content = self.make_document(final_list)
                    KeywordExtractor.corpus.append(content)

                    uw = self.make_count_list(final_list, i)
                    self.all_words_per_class = self.all_words_per_class.union(uw)

                    # print(final_list)
                    # print(len(tokenized_list))
                    # print(len(filtered_list))
                    # print(len(final_list))

        #print(len(self.all_words_per_class))
        return self.get_all_words()

    def tokenize(self, content):
        # f = open(file, "r", encoding="utf-8")
        # content = f.read().lower()
        word_tokens = self.tokenizer.tokenize(content)

        return word_tokens

    def remove_stop_words(self, tokenized_list):
        filtered_list = []

        for w in tokenized_list:
            if w not in self.stop_words:
                filtered_list.append(w)
        return filtered_list

    def stem(self, filtered_list):
        stemmed_list = []
        for word in filtered_list:
            w = self.ps.stem(word)
            w = WordNetLemmatizer().lemmatize(w)
            stemmed_list.append(w)

        return stemmed_list

    def lemmatize(self, filtered_list):
        lemma_list = []
        for word in filtered_list:
            w = self.lm.lemmatize(word)
            lemma_list.append(w)

        return lemma_list

    def make_count_list(self, final_list, i):
        csv_data = [['word', 'frequency']]
        unique_words = set(final_list)
        # for word in unique_words:
        #     csv_data.append([word, final_list.count(word)])
        #     # print('Frequency of ', word, 'is :', final_list.count(word))
        # print(i)
        # with open(f'{self.path}{i}.csv', 'w') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerows(csv_data)
        # csv_file.close()

        return unique_words

    def get_all_words(self):
        return self.all_words_per_class

    def make_document(self, final_list):
        sentence = ""
        for word in final_list:
            sentence = sentence + word + " "

        return sentence


class Vectorizer:

    def __init__(self, words):
        self.vect = CountVectorizer()
        self.vect.fit(words)

    def vectorize(self, corpus):

        #print(self.vect.get_feature_names())
        x = self.vect.transform(corpus)
        pickle.dump(self.vect.vocabulary_, open("count_vector.pkl", "wb"))
        #print(self.vect.vocabulary_)

        #print(x.toarray())
        # with open("all_words.txt", "a+", encoding='utf-8') as word_file:
        #     for l in x.toarray():
        #         listToStr = ','.join(map(str, l))
        #         word_file.write(listToStr)
        #         word_file.write("\n")

        return x

    def tfidf(self, x):
        tfidf_transformer = TfidfTransformer()
        X_tfidf = tfidf_transformer.fit_transform(x)
        pickle.dump(tfidf_transformer, open("tfidf.pkl", "wb"))
        list_f = self.vect.get_feature_names()
        list_f.append("news_category")
        print(list_f)
        with open("tfidf.csv", "a+", encoding='utf-8') as word_file:
            count = len(list_f)
            for w in list_f:

                if(count == 1):
                    word_file.write('\"' + w + '\"')
                    word_file.write("\n")
                else:
                    word_file.write('\"' + w + '\"' + ",")

                count -= 1
            nc = 1
            news = ''
            for l in X_tfidf.toarray():
                if nc <= 113:
                    news = '1'
                elif nc <= 197:
                    news = '2'
                elif nc <= 290:
                    news = '3'
                elif nc <= 396:
                    news = '4'
                elif nc <= 541:
                    news = '5'
                else:
                    news = '6'

                listToStr = ','.join(map(str, l))
                word_file.write(listToStr)
                word_file.write("," + news + "\n")
                nc += 1
        word_file.close()


