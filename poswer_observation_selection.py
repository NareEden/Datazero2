# DC power observation selection
  def select_DC_power_Observation(self, timestamp, start_time, end_time):
	  try:
		  if start_time is None and end_time is None:
			  raise ValueError("Please provide at least one of start_time or end_time")
		  if start_time == -1 and end_time == -1:
			  self.cursor.execute("SELECT * FROM datazero2.DCpowerObservation")
		  elif start_time == -1:
			  self.cursor.execute("SELECT * FROM datazero2.DCpowerObservation WHERE timeObservation < %s ORDER BY timeObservation ASC", (end_time,))
		  elif end_time == -1:
			  self.cursor.execute("SELECT * FROM datazero2.DCpowerObservation WHERE timeObservation > %s ORDER BY timeObservation ASC", (start_time,))
		  else: 
			  self.cursor.execute("SELECT * FROM datazero2.DCpowerObservation WHERE timeObservation > %s AND timeObservation < %s ORDER BY timeObservation ASC", (start_time, end_time))

		  rows =  self.cursor.fetchall()
		  return rows
	  except mariadb.Error as e:
		  print(f"Error selecting data: {e}")
