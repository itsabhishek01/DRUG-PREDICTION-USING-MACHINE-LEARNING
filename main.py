import pandas as pd

df=pd.read_csv('drug200.csv')
#checking if there is any missing value

#print(df.isnull().sum())

x=df.iloc[0:201,0:5]#independent
y=df["Drug"]#dependent

from sklearn.preprocessing import LabelEncoder
la=LabelEncoder()
y=la.fit_transform(y)

ls=LabelEncoder()
x["Sex"]=ls.fit_transform(x["Sex"])

lb=LabelEncoder()
x["BP"]=lb.fit_transform(x["BP"])

lc=LabelEncoder()
x["Cholesterol"]=lc.fit_transform(x["Cholesterol"])

#scaling our independent data
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

#train test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#classifiction
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)

#checking accuracy
from sklearn.metrics import accuracy_score
print("Accuracy Score is:")
print(accuracy_score(y_test, y_pred))

#saving models
from joblib import dump
dump(la,"Drug.joblib")
dump(ls,"Sex.joblib")
dump(lb,"BP.joblib")
dump(lc,"Cholesterol.joblib")
dump(sc,"scaling.joblib")
dump(lr,"regressor.joblib")