# -*- coding: utf-8 -*-
"""isolation_forest_anomaly_detection_simple_case1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KXnXLq_HXyPYVZcK_4qUZZYTBAiR1V-T
"""

import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.utils import resample
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split
from google.colab import drive

drive.mount('/content/gdrive')

path = '/content/gdrive/MyDrive/Repository/Datasets/breast_cancer/data.csv'

df = pd.read_csv(path)
df.head()

df.diagnosis.value_counts()

df.diagnosis.unique()

# downsampling
diag_major = df[df['diagnosis']=='B']
diag_minor = df[df['diagnosis']=='M']

min_downsample = resample(diag_minor, replace=True, n_samples=30, random_state=42)
ds_df = pd.concat([diag_major, min_downsample])

ds_df.head()

ds_df.diagnosis.value_counts()

X = ds_df.drop(['diagnosis', 'Unnamed: 32'], axis=1)

y = ds_df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

if_model = IsolationForest(random_state=42)

if_model.fit(X_train, y_train)

y_hat = if_model.predict(X_test)

# replacing -1 with M and 1 with B

y_hat = np.where(y_hat==1, 'B', 'M')

y_hat

confusion_matrix(y_test, y_hat)