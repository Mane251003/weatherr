def final_message():
    with open('weather_log.txt', 'a') as f:
        f.write('Weather data logged successfully.\n')
        