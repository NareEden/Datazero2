#  Data base class
class DataBase:
  
  def __init__(self, initialTime, user, password, host, database):
    
      DataZeroApp.__init__(self, "DataBase", initialTime, False)
      
      if DEBUG:
        print("DataBase :: DataBase")
  
   # create listener
      listenedTopics = [IT_DESC_DC, ELEC_DESC_DC, DC_POWER_OBSERVATION, 
  		      WORKLOAD_FORECAST, 
  		      WEATHER_FORECAST, WEATHER_OBSERVATION, GET_WEATHER_FORECAST, GET_WEATHER_OBSERVATION]
      self.listenerDataBase = ListenerDataBase(self, listenedTopics, self.applicationName+"_Listener")
    
      self.producer_RESPONSE_GET_WEATHER_FORECAST = DZProducer(RESPONSE_GET_WEATHER_FORECAST)  # initializes an object using a constant 
      self.producer_RESPONSE_GET_WEATHER_OBSERVATION = DZProducer(RESPONSE_GET_WEATHER_OBSERVATION)
      
      # connect to datazero2 database
      print("connect")
      self.user = user
      self.password = password
      self.host = host
      self.database = database
      self.conn = self.connect_to_database()
      self.cursor = self.conn.cursor()
      #self.create_table()
      self.show_tables()
  
      print("Here")
      #self.table_columns()
      #self.select_data()
      #self.show_tables()
      #self.connect_bash()
      #self.read_message()
      if DEBUG:
        print("End DataBase :: DataBase")
