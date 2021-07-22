import pyowm 

owm = pyowm.OWM(
    'jfskjhfjsaaaaa2321902sdfsdf'

)

city = 'Bhaktapur'
loc = owm.weather_at_place(city)
weather = loc.get_weather()

for key,val in temp.items():
    print(f"{key} -> {val}")

humidity = weather.get_humidity()
winds = weather.get_wind()
rain = weather.get_rain()
snow = weather.get_snow()

print(f"humidity = {humidity}")
print(f"winds = {winds}")
print(f"rain = {rain}")
print(f"snow = {snow}")

sunrise = weather.get_sunrise_time(timeformat = 'iso')
sunset= weather.get_sunset_time(timeformat = 'iso')

print(f"Sunrise = {sunrise}")
print(f"sunset = {sunset}")


loc = loc.three_hours_forcast(city)
clouds = str(loc.will_have_clouds())
rain = str(loc.will_have_rain())

print("will have rain ",rain)
print("will have cloud ",clouds)


