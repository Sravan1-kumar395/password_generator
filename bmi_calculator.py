
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    
    bmi = calculate_bmi(weight, height)
    
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {bmi_category(bmi)}")

if __name__ == "__main__":
    main()
