#function that takes two arguments 145 and 'o' used  by 'format' function to return formatted string    
number = 145
formatted_number = format(number, 'o')  # 'o' means octal
print("Formatted number in octal:", formatted_number)

#2.calculate the area of a circular pond and water volume
radius = 84
pi = 3.14

# Step 1: Calculate area of the pond
area = pi * (radius ** 2)

# Step 2: Calculate total water in liters
water_per_sqm = 1.4
total_water = int(area * water_per_sqm)  # Convert to integer to remove decimals

print("Area of the pond:", area)
print("Total amount of water (liters):", total_water)

#3.Calculate Speed in Meters per Second
distance_m = 490
time_min = 7
time_sec = time_min * 60  # Convert minutes to seconds

# Calculate speed
speed_mps = int(distance_m / time_sec)  # Truncate to integer

print("Speed (m/s):", speed_mps)
