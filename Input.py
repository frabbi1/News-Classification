import pickle

from sklearn.feature_extraction.text import CountVectorizer


class News_Classification:

    def __init__(self):
        pass

    def get_result(self, text):
        ctg_list = ["Sports", "Science and Technology", "National", "International", "Entertainment", "Business"]
        inp = text
        loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
        X_new_counts = loaded_vec.transform([inp])

        loaded_tfidf = pickle.load(open("tfidf.pkl", "rb"))
        loaded_model = pickle.load(open("model.pkl", "rb"))

        X_new_tfidf = loaded_tfidf.transform(X_new_counts)
        predicted = loaded_model.predict(X_new_tfidf)

        return (ctg_list[int(predicted[0]) - 1])




# nc = News_Classification()
# a = nc.get_result("Iran discovers new oil field that could boost reserves by a third, says President Rouhani The announcement comes as Iran is reeling from American sanctions after the US pulled out of its nuclear deal with world powers.")
# print(a)
# print()
# Classifier.classifier.predict()

# Sakib al hasn takes 10 wickets in 5 overs
