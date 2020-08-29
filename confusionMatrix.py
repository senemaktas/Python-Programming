from sklearn.metrics import confusion_matrix
from keras.models import Sequential
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#basci model------------------------------------------------
model = Sequential()
model.add()
model.add()
model.add()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(X_train, y_train, batch_size=128, epochs=100, verbose=1,validation_data=(X_test,y_test))
score = model.evaluate(X_test, y_test,batch_size=128, verbose=1)

#confusion matrix------------------------------------------
y_pred=model.predict(X_test,batch_size=64)
y_pred=(y_pred > 0.5)
results=confusion_matrix(y_test,y_pred)

plt.clf()
plt.imshow(results, interpolation='nearest', cmap="Wistia")
plt.title('Confusion Matrix - Test Data')
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt. yticks([])
plt. xticks([])

s = [['TN','FP'], ['FN','TP']]
for i in range(2):
    for j in range(2):
        plt.text(j,i, str(s[i][j])+" = "+str(results[i][j]))
plt.show()
