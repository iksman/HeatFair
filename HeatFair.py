from logger import Logger
from gpiozero import CPUTemperature

def getData():
	return CPUTemperature().temperature

#Amount of meassurements taken for average before writing to output.json
meassurements = 12

#Time between each meassurement (in seconds)
interval = 20
#Total time per output in seconds = meassurements * interval

#Maximum of datapoints in first file before datapoints will be retired to legacy.json
datapoints = 500


logMaker = Logger	(
  interval,
  getData,
  "data",
  "temperature",
  datapoints
)

logMaker.log(meassurements)
