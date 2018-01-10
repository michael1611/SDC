from data import *
from model import *
X, y = getData()
print(X.shape, y.shape)
model = getModel()
nb_epochs = 1
history = model.fit(X, y, epochs=nb_epochs, validation_split=0.25)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")
