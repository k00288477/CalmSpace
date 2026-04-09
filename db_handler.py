import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="calmspace",
        password="password",
        database="calmspace"
    )

def save_readings(readings):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO readings (temperature, humidity, noise)
            VALUES (%s, %s, %s)
        """, (
            readings["temperature"],
            readings["humidity"],
            readings["noise"]
        ))
        conn.commit()
        cursor.close()
        conn.close()
        print("Readings saved to database")
    except Exception as e:
        print(f"Database error: {e}")
