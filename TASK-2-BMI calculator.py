def bmi_calculate(weight, height):
    bmi = weight / (height**2)
    return bmi

def bmi_index(bmi):
    if bmi < 18.5:
        return "underweight"
    
    elif 18.5 <= bmi <24.9:
        return "normal weight"
    
    elif 25 <= bmi < 29.9:
        return "overweight"
    
    else:
        return "Extra Overweight"
    
def main():
    print("Welcome to BMI Calculator")

    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height in meters:"))

    bmi = bmi_calculate(weight , height)


    your_weight = bmi_index(bmi)

    print(f"Your BMI is:{bmi}")
    print(f"your weight:{your_weight}")

if __name__ == "__main__":
    main()    