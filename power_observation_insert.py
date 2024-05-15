# PowerObservation data insert
  def processDC_POWER_OBSERVATION(self, dcPowerObservationMessage):
	  print("processDC_POWER_OBSERVATION")
	  dcPowerObservation = dcPowerObservationMessage.dcPowerObservation
	  timeObservation=dcPowerObservation.observationTime
	  dcPower=dcPowerObservation.dcPower
	  battery_energy=dcPowerObservation.batteriesGlobalEnergy
	  tankers=dcPowerObservation.tankersGlobalStock
	  mapConsumedOrProducedPower = dcPowerObservation.consumedOrProducedPower
	  source_photoVoltaic= mapConsumedOrProducedPower[SourceType.SOLAR]
	  source_wind=mapConsumedOrProducedPower[SourceType.WIND_TURBINE]
	  source_battery_power=mapConsumedOrProducedPower[SourceType.BATTERY]
	  source_fuelCell = mapConsumedOrProducedPower[SourceType.FUEL_CELL]
	  source_electrolyzer= mapConsumedOrProducedPower[SourceType.ELECTROLYZER]
	  data_to_insert = (timeObservation,dcPower,battery_energy,tankers,source_photoVoltaic,source_wind,source_battery_power,source_fuelCell,source_electrolyzer )
	  sql_query = '''
			INSERT INTO datazero2.DCpowerObservation (timeObservation,dcPower,battery_energy,tankers,source_photoVoltaic,source_wind,source_battery_power,source_fuelCell,source_electrolyzer)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
			ON DUPLICATE KEY UPDATE
            dcPower = VALUES(dcPower),
            battery_energy = VALUES(battery_energy),
            tankers = VALUES(tankers),
            source_photoVoltaic = VALUES(source_photoVoltaic),
            source_wind = VALUES(source_wind),
            source_battery_power = VALUES(source_battery_power),
            source_fuelCell = VALUES(source_fuelCell),
            source_electrolyzer = VALUES(source_electrolyzer)
            '''
	  self.cursor.execute(sql_query, data_to_insert)
	  self.conn.commit()
	  print("processDC_POWER_OBSERVATION")

