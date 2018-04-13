from writer import Writer
import datetime, time

class Logger:
  def __init__(self,interval,data,key,valueKey,maxValues):
    if type(interval) != int:
      self.interval = 300 #5 minute interval
    else:
      self.interval = interval
    if type(interval) != int:
      self.maxValues = 1440 #5 minute interval
    else:
      self.maxValues = maxValues
    if type(key) != str:
      self.key = "data"
    else:
      self.key = key
    if type(valueKey) != str:
      self.valueKey = "value"
    else:
      self.valueKey = valueKey
    self.data = data #Method to call to get value
    self.writer = Writer("output.json")
    self.legacyData = Writer("legacy.json")
  
  def log(self,interval=1):
    iteration = 0
    median = 0
    while True:
      median += self.data()
      iteration += 1
      
      if iteration % interval == 0:
        newDict = {
          self.valueKey: round((median / iteration),3),
          "time": str(datetime.datetime.now())
        }      
        
        print(str(newDict[self.valueKey]) + " - " + str(datetime.datetime.now()))
        self.writer.writeAppend(
          self.key,
          newDict,
          False
        )
        
        if len(self.writer.content[self.key]) >= self.maxValues:
          self.legacyData.writeAppend(self.key, self.writer.content[self.key][0], False)
          
          intermediateContent = {self.key : self.writer.content[self.key][1:]}
          print('Stored variable in legacy.json')   
          self.writer.alterContent(intermediateContent)
          
        
        median = 0
        iteration = 0
        #print(self.writer.content[self.key][0])      
      else:
        print(str(round((median / iteration), 3))) #+ " -> (" + str(round(median,3)) + ")")
      time.sleep(self.interval)
  
  
  
