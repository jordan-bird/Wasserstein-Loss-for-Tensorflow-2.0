from tensorflow.keras import backend

class wasserstein_loss(Loss):
	def call(self, y_true, y_pred):
		return backend.mean(y_true * y_pred)