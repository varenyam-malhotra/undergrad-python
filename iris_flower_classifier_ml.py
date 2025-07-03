# Varenyam Malhotra
# Iris Flower Classifier
# Machine Learning Project
# Uses visualization, k-means clustering, classifcation, random forest and its feature importance
# Trains and tests the logistic regression model 
# Recall that the Iris dataset that we are using is a built-in toy dataset within scikit-learn

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)
target_names = iris.target_names
print(X.head)
print(y.head)

# Visualize the dataset (pairplot)

# sns.pairplot(pd.concat([X, y.rename("target")], axis=1), hue="target", palette="Set2")
# plt.suptitle("Pairplot of Iris Features", y=1.02)
# plt.show()


# K-Means Clustering (Unsupervised Learning)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)
X["kmeans_cluster"] = clusters

plt.figure(figsize=(8, 5))
sns.scatterplot(data=X, x="petal length (cm)", y="petal width (cm)", hue="kmeans_cluster", palette="Set1")
plt.title("K-Means Clusters")
plt.show()

# Prepare data for classification (remove cluster column)
X_features = X[iris.feature_names]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42)

# Logistic Regression Model
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train, y_train)
logreg_preds = logreg.predict(X_test)

print("Logistic Regression Results:")
print("Accuracy:", accuracy_score(y_test, logreg_preds))
print(confusion_matrix(y_test, logreg_preds))
print(classification_report(y_test, logreg_preds, target_names=target_names))

# Random Forest Model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

print("🔹 Random Forest Results:")
print("Accuracy:", accuracy_score(y_test, rf_preds))
print(confusion_matrix(y_test, rf_preds))
print(classification_report(y_test, rf_preds, target_names=target_names))

# Feature Importance from Random Forest
importances = rf.feature_importances_
feat_df = pd.DataFrame({"feature": iris.feature_names, "importance": importances}).sort_values("importance", ascending=False)

plt.figure(figsize=(6, 4))
sns.barplot(data=feat_df, x="importance", y="feature", palette="viridis")
plt.title("Feature Importance (Random Forest)")
plt.tight_layout()
plt.show()
