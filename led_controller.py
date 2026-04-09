from sense_hat import SenseHat

sense = SenseHat()

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

THRESHOLDS = {
    "noise": 50, #35
    "temperature": (17.2, 26),
    "humidity": (40, 60),
    "light": 300
}

def count_out_of_range(readings):
    count = 0

    if readings["noise"] > THRESHOLDS["noise"]:
        count += 1

    temp = readings["temperature"]
    if temp < THRESHOLDS["temperature"][0] or temp > THRESHOLDS["temperature"][1]:
        count += 1

    humidity = readings["humidity"]
    if humidity < THRESHOLDS["humidity"][0] or humidity > THRESHOLDS["humidity"][1]:
        count += 1

    if readings["light"] > THRESHOLDS["light"]:
        count += 1

    return count

def update_led(readings):
    out_of_range = count_out_of_range(readings)

    if out_of_range == 0:
        colour = GREEN
    elif out_of_range == 1:
        colour = YELLOW
    else:
        colour = RED

    sense.clear(colour)
