import random
import csv
import os

# This function set a random burst time and memory requirement based on parameters passed into randint
def runTimeRequirementsEva():
  burstTime = random.randint(10*10**6, 10*10**12)
  memoryRequirement = random.randint(1,16)
  return [burstTime, memoryRequirement]
  
# calculates burst time given the data -> csv_reader
def BurstTime(csv_reader):
  TTRS = []
  TTR = 0 
  # number represents us incrementally adding the process cycles. each addition is then appended into TTRS 
  for process in csv_reader:
    if process != "Bursttime":
      TTR+=int(process)
      TTRS.append(TTR) 
  return TTRS

def waitTime(csv_reader):
  Wait_Times = []
  Wait_Time = 0
  # number represents us incrementally adding the process cycles. each addition is then appended into Wait_Times. 
  # But based on the concept of wait time we will start by appending 0, then add then rest as opposed to burst time 
  for process in csv_reader:
    if process != "Bursttime":
      Wait_Times.append(Wait_Time)
      Wait_Time+=int(process)
  return Wait_Times

def process():
  if os.stat('runTimeRequirements.csv').st_size == 0:
    print("exec")
    with open('runTimeRequirements.csv', 'w', newline='') as csv_file:
      csv_writer = csv.writer(csv_file)
      csv_writer.writerow(["Bursttime", "Memory"])
      for i in range(249):
        csv_writer.writerow(runTimeRequirementsEva())
  else:
    with open('runTimeRequirements.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_readerVal = []
        for process in csv_reader:
            if process[0] != "Bursttime":
              csv_readerVal.append(int(process[0]))
        csv_readerVal.sort()  
        burstTime = BurstTime(csv_readerVal)
        write_Times = waitTime(csv_readerVal)  
    return burstTime, write_Times

      
def  runTimeRequirementsEvaCalc():
  TTRS = process()[0]
  Wait_Times = process()[1]

  AVGTTRS = 0
  AVG_Wait_Time = 0
  for TTR in TTRS:
    AVGTTRS += TTR
  for Wait_Time in Wait_Times:
    AVG_Wait_Time += Wait_Time

  AVGTTRS /= len(TTRS)+1
  AVG_Wait_Time /= len(Wait_Times)
  return AVGTTRS, AVG_Wait_Time

def main():
    AVGTTRS = runTimeRequirementsEvaCalc()[0]
    AVG_Wait_Time = runTimeRequirementsEvaCalc()[1]
    print("The average turn around time = %f" %AVGTTRS)
    print("The average wait time = %f" %AVG_Wait_Time)
if __name__ == "__main__":
    main()