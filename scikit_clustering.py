# # # ===========\++++++
import tensorflow as tf
from tensorflow.keras import layers, models, datasets,losses
import matplotlib as plt
from tensorflow.keras.preprocessing import image
import numpy as np
tf.k

#Loading MNIST dataset
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

#Normalize pixel values

x_train = x_train/ 255
x_test = x_test / 255

#Build a model

model = models.Sequential([
    layers.Flatten(input_shape =(28,28)),
    layers.Dense(128, activation ='relu'),
    layers.Dropout(0.2),
    layers.Dense(10)

])

#Compile a model

model.compile(

    optimizer = 'adam',
    loss= tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ['accuracy']
)

#train a model

model.fit(x_train, y_train, epochs = 5)
model.save("Digit_classifier.h5")
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("Test Accuracy is: ", test_acc)
print("Model has been train successfully")





















































# import tensorflow as tf
# from tensorflow.keras import layers, models, datasets
# import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing import image
# import numpy as np
#
# # Load MNIST dataset
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# print(x_test)
# # Normalize pixel values to be between 0 and 1
# x_train, x_test = x_train / 255.0, x_test / 255.0
#
#
# # Build a simple convolutional neural network model
# model = models.Sequential([
#     layers.Flatten(input_shape=(28, 28)),
#     layers.Dense(128, activation='relu'),
#     layers.Dropout(0.2),
#     layers.Dense(10)
# ])
#
# # Compile the model
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])
#
# # # Train the model
# model.fit(x_train, y_train, epochs=5)
# model.save("digit_classifier.h5")
# # Evaluate the model on the test set
# test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
# print(f'\nTest accuracy: {test_acc}')
# #
# model = tf.keras.models.load_model('digit_classifier.h5')
# # Load and preprocess the test image
# img_path = 'digit.jpg'  # Replace with the path to your test image
# img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
# img_array = image.img_to_array(img)
# img_array = np.expand_dims(img_array, axis=0)
# img_array /= 255.0  # Normalize pixel values
# #
# # Make predictions
# predictions = model.predict(img_array)
#
# # Get the predicted class
# predicted_class = np.argmax(predictions)
#
# # Display the original image
# img = image.load_img(img_path)
# plt.imshow(img, cmap="gray")  # Adjust colormap for grayscale image
# plt.title(f"Predicted Class: {predicted_class}")
# plt.show()

# import os
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
#
# # Define paths to your image datasets
# vehicle_data_dir = "Data/vehicles"
# non_vehicle_data_dir = "Data/non-vehicles"
#
#
# # # Set target image size
# img_width, img_height = 224, 224
#
# # Define subdirectories for training, validation, and test sets
# vehicle_train_dir = os.path.join(vehicle_data_dir, "train")
# vehicle_val_dir = os.path.join(vehicle_data_dir, "val")
# vehicle_test_dir = os.path.join(vehicle_data_dir, "test")
# non_vehicle_train_dir = os.path.join(non_vehicle_data_dir, "train")
# non_vehicle_val_dir = os.path.join(non_vehicle_data_dir, "val")
# non_vehicle_test_dir = os.path.join(non_vehicle_data_dir, "test")
#
# # Create ImageDataGenerator objects for each class
# vehicle_datagen = ImageDataGenerator(rescale=1./255)
# non_vehicle_datagen = ImageDataGenerator(rescale=1./255)
#
# # Create training and validation generators for each class
# vehicle_train_generator = vehicle_datagen.flow_from_directory(
#     vehicle_train_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"  # Binary classification: vehicle or non-vehicle
# )
# vehicle_val_generator = vehicle_datagen.flow_from_directory(
#     vehicle_val_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
# non_vehicle_train_generator = non_vehicle_datagen.flow_from_directory(
#     non_vehicle_train_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
# non_vehicle_val_generator = non_vehicle_datagen.flow_from_directory(
#     non_vehicle_val_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
#
# # Create test generators (optional, if you have separate test sets)
# vehicle_test_generator = vehicle_datagen.flow_from_directory(
#     vehicle_test_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
# non_vehicle_test_generator = non_vehicle_datagen.flow_from_directory(
#     non_vehicle_test_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
#

#
# # Create training and validation generators
# train_datagen = ImageDataGenerator(rescale=1./255)  # Normalize images
# train_generator = train_datagen.flow_from_directory(
#     vehicle_data_dir,
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"  # Binary classification: vehicle or non-vehicle
# )
# val_datagen = ImageDataGenerator(rescale=1./255)  # Normalize images
# val_generator = val_datagen.flow_from_directory(
#     vehicle_data_dir + "/val",
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )
#
# # Create test generator (optional, if you have a separate test set)
# test_datagen = ImageDataGenerator(rescale=1./255)
# test_generator = test_datagen.flow_from_directory(
#     non_vehicle_data_dir + "/test",
#     target_size=(img_width, img_height),
#     batch_size=32,
#     class_mode="binary"
# )

# Define the base model (e.g., VGG16, ResNet50)
# base_model = tf.keras.applications.VGG16(weights="imagenet", include_top=False)
#
# # Freeze base model layers (optional)
# base_model.trainable = False
#
# # Add additional layers for classification
# x = base_model.output
# x = tf.keras.layers.Flatten()(x)
# x = tf.keras.layers.Dense(units=128, activation="relu")(x)
# output = tf.keras.layers.Dense(units=1, activation="sigmoid")(x)
#
# model = tf.keras.Model(inputs=base_model.input, outputs=output)
#
# # Compile the model
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# # Print the model summary
# model.summary()
#
#
# # Train the model on training data
# history = model.fit(
#     train_generator,
#     epochs=10,
#     validation_data=val_generator
# )
#
# # Save the model (optional)
# model.save("vehicle_classifier.h5")
# print("Model Saved Successfully")






# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt
# df = pd.read_csv("segmentation data.csv")
#
# df.drop('ID',axis=1, inplace=True)
# df_clustering = df.drop('ID',axis=1)
#
#
# scaler = StandardScaler()
# df_scaled = scaler.fit_transform(df_clustering)
# number_of_clusters = 3
# model = KMeans(n_clusters=number_of_clusters,random_state=42)
# df["Cluster"] = model.fit_predict(df_scaled)
# print(df)
#
# plt.scatter(df['Sex'],df['Education'], c=df['Cluster'], cmap = 'viridis')
# plt.xlabel('Sex')
# plt.ylabel('Education')
# plt.title('K-Means Clustering')
# plt.show()

# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import pandas as pd
#
#
# data_frame=pd.read_csv("student_interests_group.csv")
# data_frame=data_frame.fillna(0)
# scaler=StandardScaler()
# data_frame_scaled=scaler.fit_transform(data_frame)
# number_of_clusters=2
# model=KMeans(n_clusters=number_of_clusters,random_state=42)
# predicted_clusters=model.fit_predict(data_frame_scaled)
# data_frame["clusters"]=predicted_clusters
# data_frame.to_excel("data_frame2.xlsx")
#
# condition_one=data_frame["clusters"]==0
# filtered_rows_cluster_one=data_frame[condition_one]
# # print(filtered_rows_cluster_one)
#
# condition_two=data_frame["clusters"]==1
# filtered_rows_cluster_two=data_frame[condition_two]
# #print(filtered_rows_cluster_two)
#
# column_with_ones=filtered_rows_cluster_one.columns[filtered_rows_cluster_one.eq(2).any()].tolist()
# # print(len(column_with_ones))
# # print(filtered_rows_cluster_two)
# excel_data_frame=filtered_rows_cluster_two.to_excel("filtered.xlsx")
# column_with_two=filtered_rows_cluster_two.columns[filtered_rows_cluster_two.eq(2).any()].tolist()
# print(column_with_two)

# filtered_rows_cluster_one=filtered_rows_cluster_one.drop(["clusters"],axis=1)
# sum_one=filtered_rows_cluster_one.sum()
# max_one=sum_one.idxmax()
# # print(max_one)
#
# filtered_rows_cluster_two=filtered_rows_cluster_two.drop(["clusters"],axis=1)
# sum_two=filtered_rows_cluster_two.sum()
# max_two=sum_two.idxmax()
# print(max_two)










































# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt
# df  =  pd.read_csv("segmentation data.csv")
# df_clustering = df.drop('ID', axis=1)
# scaler = StandardScaler()
# df_scaled = scaler.fit_transform(df_clustering)
# n_clusters = 3
# kmeans = KMeans(n_clusters=n_clusters, random_state=42)
# df['Cluster'] = kmeans.fit_predict(df_scaled)
# print(df)
# # Plot clusters (for 2D data, e.g., Age vs. Income)
# plt.scatter(df['Age'], df['Income'], c=df['Cluster'], cmap='viridis')
# plt.xlabel('Age')
# plt.ylabel('Income')
# plt.title('K-Means Clustering')
# plt.show()
