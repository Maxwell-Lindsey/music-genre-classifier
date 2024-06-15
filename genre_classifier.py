# load data
# split the data into train and test sets
# build the network architecture
# compile network
# train network
# source: https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf

import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt

DATASET_PATH = './data.json'
GLOBAL_HISTORY = None

def add(a, b):
    return a + b

def load_data(dataset_path):
    with open(dataset_path, "r") as fp:
        data = json.load(fp)
    
    # convert lists into numpy arrays
    inputs = np.array(data['mfcc'])
    targets = np.array(data['labels'])

    return (inputs, targets)

def plot_history(history):
    fig,axs = plt.subplots(2)
    
    #create the acurracy subplot
    axs[0].plot(history.history["accuracy"], label = "train accuracy")
    axs[0].plot(history.history["val_accuracy"], label = "test accuracy")
    axs[0].set_ylabel("accuracy")
    axs[0].legend(loc="lower right")
    axs[0].set_title("Accuracy eval")
    

    #create the error subplot
    axs[1].plot(history.history["loss"], label = "train error")
    axs[1].plot(history.history["val_loss"], label = "test error")
    axs[1].set_ylabel("Error")
    axs[1].set_xlabel("Epoch")
    axs[1].legend(loc="upper right")
    axs[1].set_title("Error eval")


    plt.savefig("error_accuracy.png")
    #plt.show()


def prepare_dataset(test_size, validation_size):
 
    # load data
    X, y = load_data(DATASET_PATH)    
 
    #create train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)
 
 
    #create train/validation splits
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size = validation_size)
    #20% of data used for validation
 
    # Tensorflow expects a 3D array for each sample (130, 13, 1)
    # 3rd dimension is the channel
    # X_train = X_train[..., np.newaxis] # now it's a 4D array -> (num_samples, 130, 13, 1)
    # X_validation = X_validation[..., np.newaxis]
    # X_test = X_test[...,np.newaxis]
    # code above is not required for RNN

    return X_train, X_validation, X_test, y_train, y_validation, y_test
 
def build_model(input_shape):
    # create model
    model = keras.Sequential()
    # 1st convolution layer
    # numKernels, size of grid, activation function we want to use
    model.add(keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides = (2, 2), padding = 'same'))
    model.add(keras.layers.BatchNormalization()) # helps speed up training, model converges faster
 
    # 2nd convolution layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = input_shape))
    model.add(keras.layers.MaxPool2D((3, 3), strides = (2, 2), padding = 'same'))
    model.add(keras.layers.BatchNormalization())
 
    # 3rd convolution layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation = 'relu', input_shape = input_shape))
    model.add(keras.layers.MaxPool2D((2, 2), strides = (2, 2), padding = 'same'))
    model.add(keras.layers.BatchNormalization())
 
    # flatten the output (of convolution layers)
    # feed this output into a dense layer
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation = 'relu'))
    model.add(keras.layers.Dropout(0.3)) # to prevent overfitting
   
    # output layer
    # we want as many neurons as we have genres
    model.add(keras.layers.Dense(10, activation = 'softmax'))
   
    return model

def build_model_RNN(input_shape):

    #build network topology
    model = keras.Sequential()

    # 2 LSTM layers
    model.add(keras.layers.LSTM(64, input_shape = input_shape, return_sequences = True))
    model.add(keras.layers.LSTM(64))

    # dense layer
    model.add(keras.layers.Dense(64, activation = 'relu'))
    model.add(keras.layers.Dropout(0.3)) # to help with overfitting

    # output layer
    model.add(keras.layers.Dense(10, activation = 'softmax'))

    return model
 
# def predict(model, X, y):
   
   
#     #  X = X[np.newaxis, ...]
#     X = X[..., np.newaxis]
 
#     #prediction  = [ [0.1, 0.2, ...] ]
#     prediction = model.predict(X)

#     #extract index with max value
#     predicted_index = np.argmax(prediction, axis = 1) # [index b/w 0 and 9]
#     print("Expected index: {}, Predicted index: {}".format(y, predicted_index))
    

# Use for run-time inputs
def actual_predict(model, X):
    labels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
    # X = np.reshape(X, (216, 13, 1))
    # X = X[np.newaxis, ...]
    # X = X[np.newaxis, ...]
    prediction = model.predict(X)
    predicted_index = np.argmax(prediction, axis = 1)
    return labels[predicted_index[0]]

if __name__ == '__main__':

    # Create train, validation, and test sets
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_dataset(0.25, 0.2)
 
    # build the CNN net
    # input shape -> (130, 13, 1)
    # input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])
    # model =  build_model(input_shape)

    # build the RNN net
    input_shape = (X_train.shape[1], X_train.shape[2])
    model = build_model_RNN(input_shape)
 
    #compile the network
    optimizer = keras.optimizers.Adam(learning_rate = 0.0001)
    model.compile(optimizer = optimizer,
                    loss = "sparse_categorical_crossentropy",
                    metrics = ['accuracy'])
 
    #train the CNN
    history = model.fit(X_train, y_train, validation_data = (X_validation, y_validation), batch_size = 32, epochs = 500)
 
    #evalute the CNN on the train set
    test_error, test_accuracy = model.evaluate(X_test, y_test, verbose = 1)
    print("Accuracy on test set is: {}".format(test_accuracy))
    print("reached line 158")
    plot_history(history)
 
    # make prediction on a sample
    # X = input data
    # y = label
    print("reached line 164")
    X = X_test[3]
    print(X_test.shape)
    print(X.shape)
    # y = y_test[100]
    #predict(model, X, y)
    # print(actual_predict(model, X))

    # serialize model to JSON
    # model_json = model.to_json()
    # with open("model.json", "w") as json_file:
        # json_file.write(model_json)
    # serialize weights to HDF5
    model.save(save_format='h5', filepath='model.h5')
    # model.save_weights("model.h5")
    print("Saved model to disk")

#     inputs, targets = load_data(DATASET_PATH)

#     # 30% of data for test set
#     # 70% for train set
#     inputs_train, inputs_test, targets_train, targets_test = train_test_split(inputs, targets, test_size=0.3)

#     model = keras.Sequential([
#         keras.layers.Flatten(input_shape=(inputs.shape[1], inputs.shape[2])),
#         keras.layers.Dense(5096, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(2048, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(1024, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(256, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(128, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.25),
#         keras.layers.Dense(32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
#         keras.layers.Dropout(0.2),
#         keras.layers.Dense(10, activation='softmax'),
#     ])

#     optimizer = keras.optimizers.Adam(learning_rate=0.0001)
#     model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#     model.summary()

#     history = model.fit(inputs_train, targets_train, validation_data=(inputs_test, targets_test), batch_size=32, epochs=20)

    
    

#     prediction = model.predict(input_matrix)
#     print(prediction)
#     print("prediction is above")

#     #plot the accuracy and error vs epoch
#     

# def test_accuracy_change(history):
#     training_accuracy = history.history["accuracy"]
#     assert training_accuracy[0] < training_accuracy[-1]
#     print(training_accuracy)

#     val_accuracy = history.history["val_accuracy"]
#     assert val_accuracy[0] < val_accuracy[-1]
#     print(val_accuracy)


# test_accuracy_change(GLOBAL_HISTORY)
# print("All test cases passed - the model improved accuracy")