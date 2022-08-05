import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
msg=pd.read_csv('https://raw.githubusercontent.com/KMITDS/CS601PC/main/naivetext.csv',names=['message','label']) 
print("The dimensaions : ",msg.shape)
msg['labelnum'] = msg.label.map({'pos':1,'neg':0})
x = msg.message
y = msg.labelnum
xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state=42)
print("Total no if training data: ",ytrain.shape)
print("Total no of test data: ",ytest.shape)
cv = CountVectorizer()
xtrain_dtm = cv.fit_transform(xtrain)
xtest_dtm = cv.transform(xtest)
df = pd.DataFrame(xtrain_dtm.toarray(),columns=cv.get_feature_names_out())
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)
print('Accuracy of the classifier is',metrics.accuracy_score(ytest,predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(ytest,predicted))
print('\nThe value of Precision', metrics.precision_score(ytest,predicted))
print('The value of Recall', metrics.recall_score(ytest,predicted))
'''
The dimensions of the dataset (18, 2)
The total number of Training Data : (13,)
The total number of Test Data : (5,)
Accuracy of the classifier is 0.6
Confusion matrix
[[2 0]
[2 1]]
The value of Precision 1.0 The value of Recall 0.3333333333333333
'''
