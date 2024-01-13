# arr = [16,17,4,3,5,2]
# largest_value = -1
#
# for i in range(len(arr) - 1, -1, -1):
#     temp = arr[i]
#     arr[i] = largest_value
#     largest_value = max(largest_value, temp)
# print(arr)
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import preprocess_kgptalkie as ps
import re
def get_clean(x):
    x = str(x).lower().replace('\\', '').replace('_', ' ')
    # x = ps.cont_exp(x)
    # x = ps.remove_emails(x)
    # x = ps.remove_urls(x)
    # x = ps.remove_html_tags(x)
    # x = ps.remove_rt(x)
    # x = ps.remove_accented_chars(x)
    # x = ps.remove_special_chars(x)
    # x = re.sub("(.)\\1{2,}", "\\1", x)
    return x
df = pd.read_excel("rr.xlsx")
df.dropna(inplace=True)
# df = df[df['Review'].apply(lambda x: not (pd.isnull(x) or x.strip().isdigit()))]


# Separate features and target variable
df["Review"] = df["Review"].apply(lambda x: get_clean(x))
X = df["Review"]
# X = get_clean(X)
y = df["impact"]
# print(df.isnull().sum())
# print(df[df["impact"].isnull()])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a text vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

# Fit and transform the training data
X_train_vectorized = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_vectorized = vectorizer.transform(X_test)
print("X_Train shape is : ",X_train.shape)
print("X_Train_Vectorized shape is : ",X_train_vectorized.shape)
# Train a Decision Tree classifier
model = DecisionTreeClassifier()
model.fit(X_train_vectorized, y_train)
# joblib.dump(model,'reviews_classification.joblib')

# Make predictions on the test set
predictions = model.predict(X_test_vectorized)
#
# # Evaluate the model
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
#
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)



# from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score, confusion_matrix
# from sklearn.preprocessing import LabelEncoder
# from sklearn.feature_extraction.text import CountVectorizer
# import pandas as pd
#
# # Read a smaller subset of the data
# df = pd.read_excel("health.xlsx", nrows=1000)
#
# # Rest of the code remains the same
# X_text = df.drop("Medication", axis=1)
# y = df["Medication"]
#
# X_combined = X_text.apply(lambda row: ' '.join(map(str, row)), axis=1)
# vectorizer = CountVectorizer(stop_words='english')
# X_vectorized = vectorizer.fit_transform(X_combined)
#
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
#
# X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded, test_size=0.2, random_state=42)
#
# # Use Logistic Regression for quicker testing
# # model = LogisticRegression(random_state=42)
# model = MultinomialNB()
# model.fit(X_train, y_train)
#
# prediction = model.predict(X_test)
#
# accuracy = accuracy_score(y_test, prediction)
# conf_matrix = confusion_matrix(y_test, prediction)
#
# print("Accuracy:", accuracy)
# print("Confusion Matrix:")
# print(conf_matrix)







# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, confusion_matrix
# import joblib
# from sklearn.preprocessing import LabelEncoder
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import pandas as pd
# df = pd.read_excel("health.xlsx")
# X = df.drop("Medication", axis=1)
# y = df["Medication"]
# X_text = X.apply(lambda row: ' '.join(map(str, row)), axis=1)
# vectorizer = CountVectorizer(stop_words='english')
# X_vectorized  = vectorizer.fit_transform(X_text)
# label_encoder = LabelEncoder()
# y_encoded = label_encoder.fit_transform(y)
#
# X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded, test_size=0.2, random_state=42)
#
#
# model = MultinomialNB()
# model.fit(X_train,y_train)
# prediction = model.predict(X_test)
# accuracy = accuracy_score(y_test,prediction)
#
# conf_matrix = confusion_matrix(y_test,prediction)
# print(accuracy)
# print(conf_matrix)
#
# pd.set_option('display.max_columns', None)
# df = pd.read_excel("stress.xlsx")


# X = df.drop("stress_level", axis=1)
# y = df["stress_level"]
#
# X_train, X_test,  y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
#
# model = RandomForestClassifier()
# model.fit(X_train, y_train)
# joblib.dump(model,'stress_classifier_model.joblib')
# print("Our model is trained and saved in our PC")

# loaded_model = joblib.load("stress_classifier_model.joblib")
# prediction = loaded_model.predict(X_test)
# accuracy = accuracy_score(y_test,prediction)
# print(accuracy)

# prediction = loaded_model.predict([[21,0,1,27,5,3,0,5,5,0,0,0,0,5,0,5,0,5,0,5]])
# print(prediction)
# column_ranges = df.describe().loc[["min","max"]]
# print(column_ranges)
# print(df.loc[[])