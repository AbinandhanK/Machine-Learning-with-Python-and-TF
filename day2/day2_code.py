from __future__ import absolute_import,division,print_function,unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

dftrain=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
y_train=dftrain.pop('survived')
y_eval=dfeval.pop('survived')
print(dftrain.loc[0], y_train.loc[0])

dftrain.head()

dftrain.describe()

dftrain.shape

y_train.head()

dftrain.age.hist(bins=20)

dftrain.age.value_counts().plot(kind="barh")

dftrain['class'].value_counts().plot(kind="barh")