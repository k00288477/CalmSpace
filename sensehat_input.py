from sense_hat import SenseHat

sense = SenseHat()

def get_readings():
    return {
	#Readings adjusted using to offset the ehat produced by the Raspbery Pi
        "temperature": round(sense.get_temperature() -25 , 1),
        "humidity": round(sense.get_humidity() +40 , 1)
    }
