from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size = .25)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(x_train,y_train)
print("Accuracy: ",clf.score(x_train,y_train))
print("Accuracy: ",clf.score(x_test,y_test))
print("Predicted Data")
print(clf.predict(x_test))
prediction = clf.predict(x_test)
print("Test data: ")
print(y_test)
diff = prediction-y_test
print("Result is: ")
print(diff)
print("Total no of samples misclassified: ",sum(abs(diff)))
'''
Output:
Accuracy= 1.0
Predicted Data: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
Test data: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
Result is [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Total no of samples misclassified = 0
'''