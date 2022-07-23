#THIS IS THE FILE WHERE YOU CREATE A EXECUTABLE FILE OF MAIN LOGIC (PART 1 FILE) WHICH WILL USE FURTHER WHILE CREATING AN USER-INTERFACE.
#IN THAT SIMPLY WE HAVE TO IMPORT THE FILE.
import pickle

with open("sm.model", "rb") as f:
	model = pickle.load(f)

#prediction
no_courses = float(input("Enter the no of courses : "))
ti_std = float(input("Enter the time you study in a day (in hr) : "))
marks = model.predict([[no_courses, ti_std]])
print("\n================================Marks obtained=============================\n")
print("If you studied ",no_courses, "courses for the ", ti_std, "hr per day then you will score ", marks, "marks.")
