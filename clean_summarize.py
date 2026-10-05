readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]
clean_readings = []
alert_readings = []

for reading in readings:
    if reading is None:
        continue
    elif reading < 0 or reading > 50:
        continue
    else: 
        clean_readings.append(reading)

print(f"Clean readings: {clean_readings}")
average = average = sum(clean_readings)/len(clean_readings)
print("Average:", round(average, 1))

for reading in clean_readings:
    if reading > 30:
        alert_readings.append(reading)

print(f"Alerts: {alert_readings}")