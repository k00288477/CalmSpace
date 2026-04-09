import time
import audio_input
import sensehat_input
import led_controller
import db_handler
import firebase_handler

firebase_handler.init_firebase()

while True:
    noise_db = audio_input.get_db()
    readings = sensehat_input.get_readings()
    readings["noise"] = noise_db
    readings["light"] = 0

    led_controller.update_led(readings)

    db_handler.save_readings(readings)

    firebase_handler.push_readings(readings)

    print(f"Noise: {noise_db} dB")
    print(f"Temp: {readings['temperature']}°C")
    print(f"Humidity: {readings['humidity']}%")
    print("---")

    time.sleep(1)
