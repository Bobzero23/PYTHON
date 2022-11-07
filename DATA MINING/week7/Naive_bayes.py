#imports
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB


iris = load_iris()

X = iris.data
y = iris.target

#creating the train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

#train our model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

print("Gaussian Naive Bayes model accuracy(in %):",
metrics.accuracy_score(y_test, y_pred)*100)
bizimcicek = np.array([1.2, 1.7, 1.8, 2.1]).reshape(-1,4)
bizimtahmin = gnb.predict(bizimcicek)
print(bizimtahmin)