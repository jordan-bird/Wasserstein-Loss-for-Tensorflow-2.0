# Wasserstein Loss for Tensorflow 2.0

I couldn't find an implementation of Wasserstein Loss for TF2.0 so this one will hopefully help someone looking for the same thing. 

Uses the tf.keras.losses.Loss base class and implements mean(y_true * y_pred) via the Keras backend
