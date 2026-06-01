sensor_input = input("Enter 6 sensor values: ")

# Converting input string to list of integers
sensor_values = list(map(int, sensor_input))

# Using filter to count active sensors
active = list(filter(lambda x: x==1, sensor_values))
print(len(active), "sensors detected the line")
