# Weather Observation data insert
  def processWEATHER_OBSERVATION(self, weatherObservationMessage):
    # insert from weatherObservationMessage message
    timestamp_weather=weatherObservationMessage.timeStamp            # name 'dcPowerObservationMess│in/DZStopDC 0 age' is not defined 
    weather_observation_info=weatherObservationMessage.weatherInfos
    speed = weather_observation_info.windSpeed
    radiation = weather_observation_info.solarRadiation 
    temperature = weather_observation_info.temperature
    data_to_insert = (timestamp_weather, speed, radiation,temperature)
    #self.cursor.execute("INSERT INTO WeatherForecast (timeForecast, speed, radiation,temperature) VALUES (?, ?, ?, ?)", data_to_insert)
    sql_query = '''
      INSERT INTO datazero2.WeatherObservation (timeObservation, speed, radiation, temperature)
			VALUES (?, ?, ?, ?)
			ON DUPLICATE KEY UPDATE
            speed = VALUES(speed),
            radiation = VALUES(radiation),
            temperature = VALUES(temperature)
            '''
    self.cursor.execute(sql_query, data_to_insert)
    self.conn.commit()
    print("processWEATHER_OBSERVATION")
