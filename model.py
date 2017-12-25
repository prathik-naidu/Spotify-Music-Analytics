import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, classification_report, confusion_matrix,
                             roc_auc_score, roc_curve, matthews_corrcoef)
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

def separate_features(complete_data):
	X = complete_data[['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 
								'instrumentalness', 'time_signature', 'danceability', 
								'key', 'duration_ms', 'loudness', 'valence', 'mode', 
								'length', 'popularity', 'explicit']]

	y = complete_data[['target']]

	return X, y

def kNN_model(X_train, X_test, y_train, y_test):
	knn = KNeighborsClassifier()
	knn.fit(X_train, y_train)
	y_pred_knn = knn.predict(X_test)
	y_pred_prob_knn = knn.predict_proba(X_test)[:,1]
	knn_roc = roc_auc_score(y_test, y_pred_prob_knn)


def logreg_model(X_train, X_test, y_train, y_test):
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	y_pred_logreg = logreg.predict(X_test)
	y_pred_prob_logreg = logreg.predict_proba(X_test)[:,1]
	logreg_roc = roc_auc_score(y_test, y_pred_prob_logreg)

def rf_model(X_train, X_test, y_train, y_test):
	rf = RandomForestClassifier()
	rf.fit(X_train, y_train)
	y_pred_rf = rf.predict(X_test)
	y_pred_prob_rf = rf.predict_proba(X_test)[:,1]
	rf_roc = roc_auc_score(y_test, y_pred_prob_rf)

def mlp_model(X_train, X_test, y_train, y_test):
	mlp = MLPClassifier()
	mlp.fit(X_train, y_train)
	y_pred_mlp = mlp.predict(X_test)
	y_pred_prob_mlp = mlp.predict_proba(X_test)[:,1]
	mlp_roc = roc_auc_score(y_test, y_pred_prob_mlp)

