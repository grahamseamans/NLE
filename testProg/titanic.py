import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

titanic = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

print("\nfirst 5 maybe?\n", titanic.head())

titanic_features = titanic.copy()
titanic_labels = titanic_features.pop('survived')

inputs = {}

for name, column in titanic_features.items():
	dtype = column.dtype
	if dtype == object:
		dtype = tf.string
	else:
		dtype = tf.float32

	inputs[name] = tf.keras.Input(shape=(1,), name=name, dtype=dtype)

print("\nInputs:\n", inputs)

numeric_inputs = {name:input for name, input in inputs.items()
				  if input.dtype==tf.float32}

x = layers.Concatenate()(list(numeric_inputs.values()))
print("\nNormalization is where get the libcuda.so.1 error.\n")
norm = layers.Normalization()
norm.adapt(np.array(titanic[numeric_inputs.keys()]))
all_numeric_inputs = norm(x)

print("\nHappened right there, right?\nStill seems to work tho.\n")

print("Numeric inputs:\n", all_numeric_inputs)