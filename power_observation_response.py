# PowerObservation response
  def processResponseToGetPowerObservationself, powerObservationRequestMessage):
    print("processResponseToGetPowerObservationself")
    printPowerObservationRequestMessage(powerObservationRequestMessage) # prints the request, for example WeatherForecastRequest(-1, -1, -1)
    powerObservationRequest=powerObservationRequestMessage.powerObservationRequest
    timeStamp=powerObservationRequestMessage.timeStamp
    startTime= powerObservationRequest.startTime
    endTime= powerObservationRequest.endTime
    rows=self.select_DC_power_Observation(timeStamp, startTime, endTime)
    response=self.buildPowerResponseMessage(rows)
    self.producer_RESPONSE_GET_POWER_OBSERVATION.sendMessage(response)  # sends the weatherForecastResponseMessage, this  should be connected 
    
    
    
  def buildPowerResponseMessage(self, rows):
    result = PowerObservationResponseMessage()
    result.timeStamp=getCurrentTime()
    result.jsonPowerObservation = json.dumps(rows)
    print("result of request", result.timeStamp, result.jsonPowerObservation)
    return result
