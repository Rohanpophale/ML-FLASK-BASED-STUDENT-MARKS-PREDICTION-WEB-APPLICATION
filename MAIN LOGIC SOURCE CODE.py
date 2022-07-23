#import the lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt
import pickle

#load the data
print("\n=============================Importing the data============================\n")
data = pd.read_csv("Student_Marks.csv")
print(data.head(10))

#understanding the data
print("\n===========================Understanding the data==========================\n")
print(data.isnull().sum())

#featurs and target
featurs = data[["number_courses", "time_study"]]
target = data["Marks"]
print("\n===================================Featurs=================================\n")
print(featurs.head(10))
print("\n===================================Target==================================\n")
print(target.head(10))

#train and test
x_train, x_test, y_train, y_test = train_test_split(featurs,target,random_state = 110)

#model
model1 = LinearRegression()
model1.fit(featurs, target)

#score
train_score = model1.score(x_train, y_train)
test_score = model1.score(x_test, y_test)

print("\n==========================Scores LinearRegression==========================\n")
print("TRAIN_SCORE : ", train_score, "\t","TEST_SCORE : ", test_score)

"""
#prediction
no_courses = float(input("Enter the no of courses : "))
ti_std = float(input("Enter the time you study in a day (in hr) : "))
marks = model1.predict([[no_courses, ti_std]])
print("\n================================Marks obtained=============================\n")
print("If you studied ",no_courses, "courses for the ", ti_std, "hr per day then you will score ", marks, "marks.")
"""
#save the model
with open("sm.model", "wb") as f:
	pickle.dump(model1, f)
print("model successfully saved...")









