import pandas as pd
import numpy as np

# make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers

abalone_train = pd.read_csv(
	"https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv",
	names=["Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Age"]
)

# f = open("demo.csv", "w")
# f.write(abalone_train.head(5))
# f.close()
np.savetxt(r'demo.txt', abalone_train.head(20), fmt='%.4f')

print("The size:", np.shape(abalone_train))
print("Data types:\n", abalone_train.dtypes)
# print("First 5:\n", abalone_train[:5,:])

abalone_features = abalone_train.copy()
abalone_labels = abalone_features.pop('Age')

abalone_features = np.array(abalone_features)
print("First 5 set of features:\n", abalone_features[:5, :])

normalize = layers.Normalization()
normalize.adapt(abalone_features)

print("\nThis is after I normalized... I think after error?...\n")
abalone_model = tf.keras.Sequential([
	normalize,
	layers.Dense(64),
	layers.Dense(1)
])

abalone_model.compile(loss = tf.losses.MeanSquaredError(), 
					  optimizer = tf.optimizers.Adam())

abalone_model.fit(abalone_features, abalone_labels, epochs=10)
