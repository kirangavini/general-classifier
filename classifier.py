from sklearn import tree
from sklearn import svm
import numpy as np
clf = tree.DecisionTreeClassifier()


X = [[123, 25, 41, 13], [132, 48, 15, 13], [153, 25, 38, 19], [156, 66, 29, 15], [136, 59, 64, 10], [168, 32, 63, 14], [112, 65, 27, 15],
     [154, 36, 47, 11], [112, 34, 25, 16], [136, 36, 29, 14], [165, 76, 38, 13]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
clf = clf.fit(X, Y)

clf1 = svm.SVC()
clf1 = clf1.fit(X, Y)

 


prediction = clf.predict([[170, 60, 21, 12]])
prediction1 = clf1.predict([[170, 60, 21, 12]])

print prediction
print prediction1

 
