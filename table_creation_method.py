# Table creation method
def create_table(self):
    try:
      cur = self.conn.cursor()  # timestampMessage, timeStampForecast add
      cur.execute("""
      CREATE TABLE IF NOT EXISTS WeatherForecast (
          timeForecast BIGINT PRIMARY KEY, 
          speed FLOAT,
          radiation FLOAT,
          temperature FLOAT
      )
    """)
      cur.execute("""
                  CREATE TABLE IF NOT EXISTS WeatherObservation (
                      timeObservation BIGINT  PRIMARY KEY,
                      speed FLOAT,
                      radiation FLOAT,
                      temperature FLOAT
                  )
              """)
              
              
      cur.execute("""
                  CREATE TABLE datazero2.DCpowerObservation (
						timeObservation BIGINT PRIMARY KEY,
						dcPower FLOAT,
						battery_energy FLOAT,   
						tankers FLOAT,
						source_photoVoltaic FLOAT, # remove the source tanker 
						source_wind FLOAT,
						source_battery_power FLOAT,
						source_fuelCell FLOAT,
						source_electrolyzer FLOAT
                  )
              """)
              
              
      
      print("Tables created successfully")
      cur.close()
    except mariadb.Error as e:
        print(f"Error creating table: {e}")


  def delete_table(self):
    # Execute the query to drop the table
    self.cursor.execute(f"DROP TABLE {'WeatherObservation'};")
    self.conn.commit()
