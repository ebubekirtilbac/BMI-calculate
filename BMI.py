print ("""########################################################################
EBUBEKİR TİLBAÇ - BMI CALCULATE
#################################################################################
""")
def calculate_body_mass_index(weight, height):
    
    #Calculates the Body Mass Index (BMI) using weight in kilograms and height in meters.
    #BMI is calculated by dividing weight in kilograms by the square of height in meters.
    
    bmi = weight / (height ** 2)
    return bmi

def get_user_input(message):
    
    #Prompts the user for input and returns the entered value.
    #If the user does not provide a valid numeric input or enters a value that is zero or less, it displays an error message and asks for input again.
    
    while True:
        try:
            user_input = float(input(message))
            if user_input <= 0:
                raise ValueError()
            return user_input
        except ValueError:
            print("Invalid input. Please enter a positive number.")

weight = get_user_input("Enter your weight in kilograms: ")
height = get_user_input("Enter your height in meters: ")

bmi = calculate_body_mass_index(weight, height)

print("Body Mass Index (BMI):", bmi)