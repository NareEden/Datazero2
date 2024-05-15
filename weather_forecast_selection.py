# WeatherForecast selection
def select_WEATHER_FORECAST(self, timestamp, start, end):  
	  try:
		  if start is None and end is None:
			  raise ValueError("Please provide at least one of start_time or end_time")
		  if start == -1 and end == -1:
			  self.cursor.execute("SELECT * FROM datazero2.WeatherForecast ")
		  elif start == -1:
			  self.cursor.execute("SELECT * FROM datazero2.WeatherForecast WHERE timeForecast < %s ORDER BY timeForecast ASC", (end,))
		  elif end == -1:
			  self.cursor.execute("SELECT * FROM datazero2.WeatherForecast WHERE timeForecast > %s ORDER BY timeForecast ASC", (start,))
		  else: 
			  self.cursor.execute("SELECT * FROM datazero2.WeatherForecast WHERE timeForecast > %s AND timeForecast < %s ORDER BY timeForecast ASC", (start, end))
			  
			
		  rows = self.cursor.fetchall() 
		  return rows
	
		
	  except mariadb.Error as e:
		  print(f"Error selecting data: {e}")
