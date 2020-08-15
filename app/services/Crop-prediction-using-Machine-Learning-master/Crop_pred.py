#importing the required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Reading the csv file
data=pd.read_csv('cpdata.csv')
print(data.head(1))

#Creating dummy variable for target i.e label
label= pd.get_dummies(data.label).iloc[: , 1:]
data= pd.concat([data,label],axis=1)
data.drop('label', axis=1,inplace=True)
print('The data present in one row of the dataset is')
print(data.head(1))
train=data.iloc[:, 0:4].values
test=data.iloc[: ,4:].values

#Dividing the data into training and test set
X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.3)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Importing Decision Tree classifier
from sklearn.tree import DecisionTreeRegressor
clf=DecisionTreeRegressor()

#Fitting the classifier into training set
clf.fit(X_train,y_train)
pred=clf.predict(X_test)

from sklearn.metrics import accuracy_score
# Finding the accuracy of the model
a=accuracy_score(y_test,pred)
print("The accuracy of this model is: ", a*100)

import requests
api_key = "0e21a5ce05552c036b46309af2790168"


def GetUserGeoLocation():
    url = 'http://ipinfo.io/json '
    payload = {}
    files = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    data = response.json()
    list1 = data["city"]
    return list1
url = "http://api.openweathermap.org/data/2.5/weather?q="+GetUserGeoLocation()+"&units=metric&appid=0e21a5ce05552c036b46309af2790168"
res = requests.get(url)
data = res.json()

humidity= data['main']['humidity']
temp = data['main']['temp']
try: rain = data['rain']['3h']
except: rain = 50
ph = input("give soil ph:")
# ah=tp['Air Humidity']
# atemp=tp['Air Temp']
# pH=tp['Soil pH']
# rain=tp['Rainfall']


l=[]
l.append(humidity)
l.append(temp)
l.append(ph)
l.append(rain)
predictcrop=[l]

# Putting the names of crop in a single list
crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
cr='rice'

#Predicting the crop
predictions = clf.predict(predictcrop)
count=0
for i in range(0,30):
    if(predictions[0][i]==1):
        c=crops[i]
        count=count+1
        break;
    i=i+1
if(count==0):
    print('The predicted crop is %s'%cr)
else:
    print('The predicted crop is %s'%c)

