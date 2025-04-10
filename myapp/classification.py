import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import django
from dotenv import load_dotenv
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iWiH_Django.settings')
django.setup()


tf.config.set_visible_devices([], 'GPU')
class GenderClassifier:
    def __init__(self):
        self.model = Sequential([
            Dense(16, activation='relu', input_shape=(3,)),  
            Dense(8, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])

    def train(self, data_filename):
        data_path = os.path.join(settings.BASE_DIR, 'myapp', data_filename)
        data = pd.read_csv(data_path)
        X = data[['male_participant', 'male_author', 'male_pronouns']]
        y = data['biased_male']

        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        history = self.model.fit(X_train, y_train,
                                 epochs=20,
                                 batch_size=2,
                                 validation_data=(X_val, y_val),
                                 verbose=1)
        
        self.model.save_weights("gender_classifier.weights.h5")
        
    def predict(self, input_scores):
        input_array = np.array([input_scores])
        
        prediction = self.model.predict(input_array)
        predicted_class = (prediction > 0.5).astype(int)
        return predicted_class

if __name__ == "__main__":
    '''
    classifier = GenderClassifier()
    classifier.train("train.csv") 
    prediction = classifier.predict([0.5, 0.91, 0.01])
    
    print(f"Predicted Class: {prediction}")
    '''