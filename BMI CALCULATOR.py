weight = float(input("enter your weight in kilograms(kg):"))
height_cm=float(input("enter your height in centimeters(cm):"))
height_m=height_cm/100
bmi = weight / (height_m ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
    print("Your BMI is:", round(bmi, 2)) 
print("Category:", category)