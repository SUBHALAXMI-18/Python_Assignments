angles = [30, -15, 45, 200, 60, 90]

# Using filter to validate angles
def valid_angle(x):
    if x >= 0 and x <= 180:
        return True
    else:
        return False
valid = list(filter(valid_angle, angles))
print(valid)

# Using map to convert valid angles to servo commands
def servo(x):
    return x*10
servo_angles = list(map(servo, valid))
print(servo_angles)