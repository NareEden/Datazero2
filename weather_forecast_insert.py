# Weather forecast data insert
  def processWEATHER_FORECAST(self, weatherForecastMessage):
	  # insert from weatherForecastMessage message
	  timestampMessage = weatherForecastMessage.timeStamp
	  for weatherForecast in weatherForecastMessage.weatherForecast:
		  timestamp_weather=weatherForecast.forecastTimeStamp        # BIG int
		  weather_forecast_info=weatherForecast.forecastInfos  # obj 
		  speed = weather_forecast_info.windSpeed
		  radiation = weather_forecast_info.solarRadiation 
		  temperature = weather_forecast_info.temperature
		  data_to_insert = (timestamp_weather, speed, radiation,temperature)
		  #self.cursor.execute("""INSERT INTO WeatherForecast (timeForecast, speed, radiation,temperature) VALUES (?, ?, ?, ?)", data_to_insert
		  sql_query = '''
			INSERT INTO datazero2.WeatherForecast (timeForecast, speed, radiation, temperature)
			VALUES (?, ?, ?, ?)
			ON DUPLICATE KEY UPDATE
            speed = VALUES(speed),
            radiation = VALUES(radiation),
            temperature = VALUES(temperature)
            '''
		  self.cursor.execute(sql_query, data_to_insert)
		  self.conn.commit()
		  print("processWEATHER_FORECAST")
