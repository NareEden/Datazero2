# WeatherObservation response
 def processResponseToGetWeatherObservation(self, weatherObservationRequestMessage):
    print("processResponseToGetWeatherObservation")
    printWeatherObservationRequestMessage(weatherObservationRequestMessage) # prints the request, for example WeatherForecastRequest(-1, -1, -1)
    weatherObservationRequest=weatherObservationRequestMessage.weatherObservationRequest
    timeStamp=weatherObservationRequestMessage.timeStamp
    startTime= weatherObservationRequest.startTime
    endTime=weatherObservationRequest.endTime
    rows=self.select_WEATHER_OBSERVATION(timeStamp, startTime, endTime)
    response=self.buildObservationResponseMessage(rows)
    self.producer_RESPONSE_GET_WEATHER_OBSERVATION.sendMessage(response)  # sends the weatherForecastResponseMessage, this  should be connected 
    
    
  def buildObservationResponseMessage(self, rows):
    result_o =  WeatherObservationResponseMessage()
    result_o.timeStamp=getCurrentTime()
    result_o.jsonWeatherObservation = json.dumps(rows)
    print("result of request", result_o.timeStamp, result_o.jsonWeatherObservation)
    return result_o
