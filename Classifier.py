import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn.metrics import classification_report, \
    confusion_matrix  # Import scikit-learn metrics module for accuracy calculation




dataset = pd.read_csv("tfidf.csv")
dataset.shape
X = dataset.drop('news_category', axis=1)
y = dataset['news_category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

classifier = DecisionTreeClassifier()
classifier = classifier.fit(X, y)
pickle.dump(classifier, open("model.pkl", "wb"))

y_pred = classifier.predict(X_test)
print(y_pred)
print(classification_report(y_test, y_pred))
