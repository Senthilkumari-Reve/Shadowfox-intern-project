#1.BMI Category Calculator
#Ask the user for:Height(in meters),Weight(in kilograms)
#BMI = weight/(height**2)

#Then print the correct BMI category:

    #BMI ≥ 30 = Obesity

    #BMI 25 to <30 = Overweight

    #BMI 18.5 to <25 = Normal

    #BMI < 18.5 = Underweight

# Get user input
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine category
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

#2.Identify the Country of a City
#Ask user to enter a city
#check which country the city belongs to from these lists
#Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
#UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
#India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# City data
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# User input
city = input("Enter a city name: ")

# Check which country
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in our list")

#3.Compare Two Cities for Country Match
#Ask the user to enter two city names and checks if both cities belong to the same country
#display the result
# City data
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# User inputs
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check which country each city belongs to
def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

# Compare and print result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in our list")
