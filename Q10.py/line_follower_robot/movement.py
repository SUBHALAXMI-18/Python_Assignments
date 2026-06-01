# movement.py

def movement(sensor_values):

    if sensor_values == [0,0,0,0,0,0]:
        print("Robot Action: Stop Robot")

    elif sensor_values == [1,1,1,1,1,1]:
        print("Robot Action: Junction Detected")

    elif sensor_values[2] == 1 and sensor_values[3] == 1:
        print("Robot Action: Move Forward")

    elif sensor_values[0] == 1 or sensor_values[1] == 1:
        print("Robot Action: Turn Left")

    elif sensor_values[4] == 1 or sensor_values[5] == 1:
        print("Robot Action: Turn Right")