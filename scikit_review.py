# # # ===========\++++++ predict = model.predict(vectorized_comment)
from sklearn.decomposition import PCA
import pandas as pd

# Load the iris dataset as an example
df = pd.read_excel("stress.xlsx")
X = df.drop("stress_level", axis=1)
y = df["stress_level"]

# Apply PCA to reduce the number of features to 2
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X)
print(X_reduced)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from scipy.sparse import hstack
import joblib
# df = pd.read_csv("pakwheels.csv")
# features_mode = df["Features"].mode()[0]
# df["Features"] = df["Features"].fillna(features_mode)
#
# vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
# combined_text_features = df["Name"] + " " + df["Features"] + " " + df["Location"] + " " + df["Registered City"] + " " + df["Color"] + " " + df["Assembly"]
#
# vectorized_text_features = vectorizer.fit_transform(combined_text_features)
# combined_numeric_features = df.drop(["Name","Features","Registered City","Color","Assembly","Location","Price"], axis=1)
#
# print(vectorized_text_features.shape)
# print(combined_numeric_features.shape)
# # print(combined_numeric_features.values)
# # print(vectorized_text_features)
# combined_features = hstack([vectorized_text_features,combined_numeric_features])
# X = combined_features
# y = df["Price"]
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
# model = DecisionTreeRegressor()
# model.fit(X_train, y_train)
# joblib.dump(model,"pak_wheels_price_prediction.joblib")
# print("model has been trained")
# loaded_model=joblib.load("pak_wheels_price_prediction.joblib")
# prediction = loaded_model.predict(X_test)
#
# mse = mean_squared_error(y_test,prediction)
# r2 = r2_score(y_test,prediction)
# print(mse)
# print(r2)
# input_text_features = ["Suzuki Bolan VX 2010 Air Bags, Air Conditioning,Power Locks, Power Mirrors Karachi Pakistan Karachi White Local"]
# input_numeric_features = [2010,11111,1,800,2,1]
# vectorized_input_text_features = vectorizer.transform(input_text_features)
# combined_input_features = hstack([vectorized_input_text_features,input_numeric_features])
# predict_price = loaded_model.predict(combined_input_features)
# print(predict_price)



# def predict_price(m,v,i):
#     input_text_features = i["Name"] + " " + i["Features"] + " " + i["Location"] + " " + i["Registered City"] + " " + i["Color"] + " " + i["Assembly"]
#     input_text_vectorized = v.transform(input_text_features)
#     input_numeric_features = i.drop(["Name","Features","Registered City","Color","Assembly","Location","Price"])
#     return input_text_features





# print(predict_price)
# custom_input = {
#     "Name":"Mitsubishi Mirage 1.0 G 2012",
#     "Model":1998,
#     "Location":"Karachi Pakistan",
#     "Milage":11111,
#     "Registered City":"Karachi",
#     "Engine Type":1,
#     "Engine Capacity": 1300,
#     "Transmission":2,
#     "Color":"White",
#     "Assembly": "Local",
#     "Body Type":1,
#     "Features":" Air Bags, Air Conditioning,Power Locks, Power Mirrors, Power Steering"
# }
# predicted_price = predict_price(model,vectorizer,custom_input)
# print(predicted_price)








# print(df["Features"])
# print(df.info())
# print(df["Model Year"].median())
# print(df["Name"].mode().loc[)






































#
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.linear_model import Ridge
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import ElasticNet
# from sklearn.preprocessing import LabelEncoder
# from sklearn.svm import SVR
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from scipy.sparse import hstack
#
#
#
# df = pd.read_csv("pakwheels.csv")
#
# df['Features'] = df['Features'].fillna(df['Features'].mode()[0])
# df['Name'] = df['Name'].fillna(df['Name'].mode()[0])
# df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
# df['Registered City'] = df['Registered City'].fillna(df['Registered City'].mode()[0])
# df['Color'] = df['Color'].fillna(df['Color'].mode()[0])
# df['Assembly'] = df['Assembly'].fillna(df['Assembly'].mode()[0])
#
# vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
# text_features = vectorizer.fit_transform(df['Name'] + ' ' + df['Features'] + ' ' +df['Location'] + ' ' + df['Registered City'] + ' ' + df['Color'] + ' ' + df['Assembly'])
#
# numeric_features = df.drop(["Name","Features","Location","Registered City","Color","Assembly","Price"], axis=1)
# numeric_features = numeric_features.values
# combined_features = hstack([text_features, numeric_features])
# X = combined_features
# y = df['Price']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Initialize the linear regression model
# # model = LinearRegression()
# # model = Ridge(alpha=1.0)
# # model = Lasso(alpha=1.0)
# # model = ElasticNet(alpha=1.0, l1_ratio=0.5)
# # model = SVR(kernel='linear', C=1.0)
# # model = DecisionTreeRegressor()
# model = RandomForestRegressor(n_estimators=100)
# # model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
# # model = KNeighborsRegressor(n_neighbors=5)
#
# # Fit the model to the training data
# model.fit(X_train, y_train)
#
# # Make predictions on the test set
# predictions = model.predict(X_test)
# #
# # Evaluate the model
# mse = mean_squared_error(y_test, predictions)
# r2 = r2_score(y_test, predictions)
# print(df.describe().loc['max'])
# print(f"Mean Squared Error: {mse}")
# print(f"R-squared: {r2}")

# Now, you can use the model to predict house prices for new data
# new_data = {'SquareFeet': [2500], 'Bedrooms': [3], 'Bathrooms': [2], 'Neighborhood_Rural': [0], 'YearBuilt': [2005]}
# new_df = pd.DataFrame(new_data)
#
# # Make predictions on the new data
# new_predictions = model.predict(new_df)
#
# print("Predicted Price for New Data:", new_predictions)

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("salary.csv")
# X = df[["YearsExperience"]]
# y = df["Salary"]
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# model = LinearRegression()
# model.fit(X_train,y_train)
# prediction = model.predict(X_test)
#
# mse = mean_squared_error(y_test,prediction)
# r2 = r2_score(y_test,prediction)
#
# print(mse)
# print(r2)

# plt.scatter(X_test, y_test, color = 'black', label='Actual Data')
# plt.plot(X_test,prediction,color = 'blue', linewidth=3, label = 'Regression Line')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.legend()
# plt.show()


# experience_input = float(input("Enter year of experience: "))
# input_reshaped = [[experience_input]]
# predicted_salary = model.predict(input_reshaped)
#
# print(predicted_salary)






















































# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt
#
# # Load your dataset
# # Assuming your dataset is in a file named 'salary_data.csv'
# df = pd.read_csv('salary.csv')
#
# # Select relevant features and target variable
# X = df[['YearsExperience']]
# y = df['Salary']
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Linear Regression Model
# model = LinearRegression()
#
# # Train the model
# model.fit(X_train, y_train)
#
# # Make predictions on the test set
# y_pred = model.predict(X_test)
#
# # Evaluate the model
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
#
# print("Mean Squared Error:", mse)
# print("R-squared:", r2)
#
# experience_input = float(input("Enter the years of experience: "))
#
# # Reshape the input to match the model's expectations
# experience_input_reshaped = [[experience_input]]
#
# # Make the prediction
# predicted_salary = model.predict(experience_input_reshaped)
#
# # Print the predicted salary
# print(f"Predicted Salary for {experience_input} years of experience: {predicted_salary}")

# # Plot the regression line
# plt.scatter(X_test, y_test, color='black', label='Actual Data')
# plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression Line')
# plt.xlabel('Year of Experience')
# plt.ylabel('Salary')
# plt.legend()
# plt.show()






# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.feature_extraction.text import TfidfVectorizer
# import joblib
# import pandas as pd
#
# import preprocess_kgptalkie as ps
# import re
# def get_clean(x):
#     x = str(x).lower().replace('\\', '').replace('_', ' ')
#     x = ps.cont_exp(x)
#     x = ps.remove_emails(x)
#     x = ps.remove_urls(x)
#     x = ps.remove_html_tags(x)
#     x = ps.remove_rt(x)
#     x = ps.remove_accented_chars(x)
#     x = ps.remove_special_chars(x)
#     x = re.sub("(.)\\1{2,}", "\\1", x)
#     return x
#
# # df.dropna(inplace=True)
# # df = df[df['Review'].apply(lambda x: not (pd.isnull(x) or x.strip().isdigit()))]
#
#
# # Separate features and target variable
#
#
# data_frame=pd.read_csv("Diseases_Symptoms.csv")
# data_frame=data_frame.dropna()
# X=data_frame["Symptoms"] + " " + data_frame["Treatments"]
# X = X.apply(lambda X: get_clean(X))
# Y=data_frame["Name"]
# X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
# vectorizer=TfidfVectorizer(stop_words="english",max_features=5000)
# vectorizer_X_train=vectorizer.fit_transform(X_train)
# vectorizer_X_test=vectorizer.transform(X_test)
# model=LogisticRegression(max_iter=5000)
# model.fit(vectorizer_X_train,Y_train)
# joblib.dump(model,"disease_symptoms_treatment.joblib")
# print("model has been trained")
# loaded_model=joblib.load("disease_symptoms_treatment.joblib")
# prediction=loaded_model.predict(vectorizer_X_test)
# accuracy_score=accuracy_score(Y_test,prediction)
# print(accuracy_score)




# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
#
# # Assume 'data' is your DataFrame containing the features and target 'Price'
# # Example:
# data = pd.read_csv("hpd.csv")
#
# # Split the data into features and target
# X = data[['SquareFeet', 'Bedrooms', 'Bathrooms', 'Neighborhood', 'YearBuilt']]
# y = data['Price']
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Identify numerical and categorical columns
# numeric_features = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt']
# categorical_features = ['Neighborhood']
#
# # Create transformers for numerical and categorical columns
# numeric_transformer = Pipeline(steps=[
#     ('imputer', 'passthrough')  # You may want to add an imputer for missing values
# ])
#
# categorical_transformer = Pipeline(steps=[
#     ('onehot', OneHotEncoder(handle_unknown='ignore'))
# ])
#
# # Create column transformer
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', numeric_transformer, numeric_features),
#         ('cat', categorical_transformer, categorical_features)
#     ])
#
# # Create a pipeline with the preprocessor and the regression model
# model = Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('regressor', LinearRegression())
# ])
#
# # Fit the model
# model.fit(X_train, y_train)
#
# # Make predictions
# y_pred = model.predict(X_test)
#
# # Evaluate the model
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
#
# print(f'Mean Squared Error: {mse}')
# print(f'R-squared: {r2}')




# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd
#
# # Assuming you have a DataFrame 'df' with the mentioned features and the target 'Segmentation'
# # For example:
# df = pd.read_csv("segment.csv")
#
# # Drop 'ID' as it is not a useful feature for classification
# df.drop('ID', axis=1, inplace=True)
#
# # Convert categorical features to numeric using Label Encoding
# label_encoder = LabelEncoder()
# df['Gender'] = label_encoder.fit_transform(df['Gender'])
# df['Ever_Married'] = label_encoder.fit_transform(df['Ever_Married'])
# df['Graduated'] = label_encoder.fit_transform(df['Graduated'])
# df['Profession'] = label_encoder.fit_transform(df['Profession'])
# df['Spending_Score'] = label_encoder.fit_transform(df['Spending_Score'])
# df['Var_1'] = label_encoder.fit_transform(df['Var_1'])
# df['Segmentation'] = label_encoder.fit_transform(df['Segmentation'])
#
# # Separate features (X) and target variable (y)
# X = df.drop('Segmentation', axis=1)
# y = df['Segmentation']
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Create a decision tree classifier
# model = DecisionTreeClassifier(random_state=42)
#
# # Fit the model on the training data
# model.fit(X_train, y_train)
#
# # Make predictions on the test set
# predictions = model.predict(X_test)
#
# # Evaluate the model
# accuracy = accuracy_score(y_test, predictions)
# classification_report_result = classification_report(y_test, predictions)
#
# print("Accuracy:", accuracy)
# print("Classification Report:")
# print(classification_report_result)

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# import pandas as pd
#
# df = pd.read_csv("animals.csv")
# df.dropna(inplace=True)
# X = df["AnimalName"] + " " + df["symptoms1"] + " " +  df["symptoms2"] + " " + df["symptoms3"] + " " + df["symptoms4"] + " " + df["symptoms5"]
# y = df["Dangerous"]
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
# vectorizer = TfidfVectorizer(stop_words="english",max_features=5000)
# X_train_vectorized = vectorizer.fit_transform(X_train)
# X_test_vectorized = vectorizer.transform(X_test)
# print(X_train_vectorized.shape)
# print(X_test_vectorized.shape)
# model = DecisionTreeClassifier()
# model.fit(X_train_vectorized,y_train)
# predict =  model.predict(X_test_vectorized)
# accuracy =  accuracy_score(y_test,predict)
# print(accuracy)

































# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# import pandas as pd
#
# df = pd.read_csv("animals.csv")
# df.dropna(inplace=True)
#
# X = df["AnimalName"] + " " + df["symptoms1"] + " " + df["symptoms2"] + " " +df["symptoms3"] + " " + df["symptoms4"] + " " + df["symptoms5"]
# # X = df.drop("Dangerous", axis=1)
# y = df["Dangerous"]
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# vectorizer = TfidfVectorizer(stop_words="english",max_features=5000)
# X_train_vectorized = vectorizer.fit_transform(X_train)
# X_test_vectorized = vectorizer.transform(X_test)
# print(X_train_vectorized.shape)
# print(X_test_vectorized.shape)
# model = DecisionTreeClassifier()
# model.fit(X_train_vectorized,y_train)
# data = ["cat fever painfull Coughing Lethargy Sneezing Depression"]
# vectorized_data  = vectorizer.transform(data)
# predict  = model.predict(vectorized_data)
# print(predict)
# predict =  model.predict(X_test_vectorized)
# accuracy =  accuracy_score(y_test,predict)
# print(accuracy)

#
# comment = ["Worst food ever, not recommended at all"]
# vectorized_comment = vectorizer.transform(comment)
# predict = model.predict(vectorized_comment)
# print(predict)

# df = pd.read_excel("rr.xlsx")
# df.dropna(inplace=True)
# X = df["Review"]
# y = df["impact"]
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
# vectorizer = TfidfVectorizer(stop_words="english",max_features=5000)
# X_train_vectorized = vectorizer.fit_transform(X_train)
# X_test_vectorized = vectorizer.transform(X_test)
# model = DecisionTreeClassifier()
# model.fit(X_train_vectorized,y_train)
#
# comment = ["Worst food ever, not recommended at all"]
# vectorized_comment = vectorizer.transform(comment)
# predict = model.predict(vectorized_comment)
# print(predict)

# prediction = model.predict(X_test_vectorized)
# accuracy = accuracy_score(y_test,prediction)
# print(accuracy)
