# Data processing decsision part for each table
  def processListenedMessage(self, topicValue, receivedMessage):
    if DEBUG:
      print("DataBase :: processListenedMessage <",  self.applicationName, ">")
    
    print("DataBase received topic", topicValue)                                   
  
    self.mutexApp.P()
      
    if topicValue == IT_DESC_DC:
      self.processIT_DESC_DC(receivedMessage)
    elif topicValue == ELEC_DESC_DC:
      self.processELEC_DESC_DC(receivedMessage)
    elif topicValue == WORKLOAD_FORECAST:
      self.processWORKLOAD_FORECAST(receivedMessage)
    elif topicValue == WEATHER_FORECAST:
      self.processWEATHER_FORECAST(receivedMessage)
    elif topicValue == WEATHER_OBSERVATION:
      self.processWEATHER_OBSERVATION(receivedMessage)
    elif topicValue == DC_POWER_OBSERVATION:
      self.processDC_POWER_OBSERVATION(receivedMessage)
    elif topicValue == GET_WEATHER_FORECAST:
      self.processResponseToGetWeatherForecast(receivedMessage)
    elif topicValue == GET_WEATHER_OBSERVATION:
      self.processResponseToGetWeatherObservation(receivedMessage)
    elif topicValue == GET_POWER_OBSERVATION:
      self.processResponseToGetPowerObservation(receivedMessage)
    else:
      print("Unexpected topic received", topicValue, "with message <", receivedMessage, ">")
    
    self.mutexApp.V()
    
    if DEBUG:
      print("End DataBase :: processListenedMessage <",  self.applicationName, ">")
