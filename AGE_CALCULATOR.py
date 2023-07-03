from tkinter import *
root=Tk()
root.configure(background="Sky Blue")
root.title("Age Calculator")
root.geometry("900x1000")

#Functions
def clearAll():
	year1.delete(0,END)
	month1.delete(0,END)
	day1.delete(0,END)
	currentday1.delete(0,END)
	currentmonth1.delete(0,END)
	currentyear1.delete(0,END)
	years1.delete(0,END)
	months1.delete(0,END)
	days1.delete(0,END)

def checkError(): 

	if(year1.get()== "" or month1.get() == ""
		or day1.get() == "" or currentday1.get() == ""
		or currentmonth1.get() == "" or currentyear1.get() == "") :

		messagebox.showerror("Input Error")
		clearAll()

		return - 1 

def calculateAge(): 
	
	value = checkError()

	if value == -1 : 
		return 

	else: 
		birth_day = int(day1.get())
		birth_month = int(month1.get())
		birth_year = int(year1.get())

		given_day= int(currentday1.get())
		given_month= int(currentmonth1.get())
		given_year = int(currentyear1.get())
		month = [31, 28, 31, 30, 21, 30, 31, 31, 30, 31, 30, 31]

		if (birth_day > given_day): 
			given_month = given_month - 1
			given_day = given_day + month[birth_month-1]

		if (birth_month > given_month):
			given_year= given_year -1 
			given_month = given_month + 12 

		calculated_day=given_day - birth_day;
		calculated_month = given_month - birth_month;
		calculated_year = given_year - birth_year;

		years1.insert(10, str(calculated_day))
		month1.insert(10, str(calculated_month))
		day1.insert(10, str(calculated_day))


#Labels 
agecalc=Label(root, text="AGE CALCULATOR", font=("courier", "65"), bg='white', fg="black").grid(row=0, column=1)
random=Label(root).grid(row=2, column=1)
random1=Label(root).grid(row=3, column=1)
random2=Label(root).grid(row=4, column=1)

#Date of Birth with Entry Boxes and Labels
date=Label(root, text= "DATE OF BIRTH", font=("courier", "25"), bg="white", fg="black").grid(row=5, column=0)
random3=Label(root).grid(row=6, column=1)
name=Label(root, text="Name: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=7, column=0)
name1=Entry(root, font=("courier", "15"), bg='white')
name1.grid(row=7, column=1)
year=Label(root, text="Year: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=8, column=0)
year1=Entry(root, font=("courier", "15"), bg='white')
year1.grid(row=8, column=1)
month=Label(root, text="Month: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=9, column=0)
month1=Entry(root, font=("courier", "15"), bg='white')
month1.grid(row=9, column=1)
day=Label(root, text="Day: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=10, column=0)
day1=Entry(root, font=("courier", "15"), bg='white')
day1.grid(row=10, column=1)
random4=Label(root).grid(row=11, column=1)
random5=Label(root).grid(row=12, column=1)

#GIVEN DATE WITH ENTRY BOXES AND LABELS
currentdate=Label(root,text= "CURRENT DATE", font=("courier", "25"), bg="white", fg="black").grid(row=13, column=0)
random6=Label(root).grid(row=14, column=1)
currentday=Label(root, text="Current Day: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=15, column=0)
currentday1=Entry(root, font=("courier", "15"), bg='white')
currentday1.grid(row=15, column=1)
currentmonth=Label(root, text="Current Month: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=16, column=0)
currentmonth1=Entry(root, font=("courier", "15"), bg='white')
currentmonth1.grid(row=16, column=1)
currentyear=Label(root, text="Current Year: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=17, column=0)
currentyear1=Entry(root, font=("courier", "15"), bg='white')
currentyear1.grid(row=17, column=1)
random7=Label(root).grid(row=18, column=1)
random8=Label(root).grid(row=20, column=1)

#Age in years, months, days
age=Label(root, text="AGE!", font=("courier", "25"), bg="white", fg="black").grid(row=21, column=0)
random9=Label(root).grid(row=22, column=1)
years=Label(root, text="Years: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=23, column=0)
years1=Entry(root, font=("courier", "15"), bg='white')
years1.grid(row=23, column=1)
months=Label(root, text="Month: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=24, column=0)
months1=Entry(root, font=("courier", "15"), bg='white')
months1.grid(row=24, column=1)
days=Label(root, text="Days: ", font=("courier", "15"), bg='white', fg="black", anchor="w").grid(row=25, column=0)
days1=Entry(root, font=("courier", "15"), bg='white')
days1.grid(row=25, column=1)
random9=Label(root).grid(row=26, column=1)

#Buttons 
btn=Button(text="Calculate Age", command=calculateAge).grid(row=19,column=1)
btn1=Button(text="Clear All", command=clearAll).grid(row=27, column=1)


root.mainloop()