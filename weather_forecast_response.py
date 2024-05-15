# WeatherForecast response
  def processResponseToGetWeatherForecast(self, weatherForecastRequestMessage):
    print("processResponseToGetWeatherForecast")
    printWeatherForecastRequestMessage(weatherForecastRequestMessage) # prints the request, for example WeatherForecastRequest(-1, -1, -1)
    weatherForecastRequest=weatherForecastRequestMessage.weatherForecastRequest
    timeStamp=weatherForecastRequestMessage.timeStamp
    startTime= weatherForecastRequest.startTime
    endTime=weatherForecastRequest.endTime
    rows=self.select_WEATHER_FORECAST(timeStamp, startTime, endTime)
    response=self.buildForecastResponseMessage(rows)
    self.producer_RESPONSE_GET_WEATHER_FORECAST.sendMessage(response)  # sends the weatherForecastResponseMessage, this  should be connected 

  def buildForecastResponseMessage(self, rows):
    result =  WeatherForecastResponseMessage()
    result.timeStamp=getCurrentTime()
    result.jsonWeatherForecast = json.dumps(rows)
    print("result of request", result.timeStamp, result.jsonWeatherForecast)
    return result
