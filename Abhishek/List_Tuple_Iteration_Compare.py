import time

def prepare_data():
  dataList = [x for x in range(1000000)]
  return dataList

myList=prepare_data()
myTuple=tuple(myList)

#List Iteration
start_time_list=time.time()
for x in myList:
  #print(x, end=" ")
  pass
end_time_list=time.time()
print()
print("Time taken to iterate list: ", end_time_list-start_time_list)


#Tuple Iteration
start_time=time.time()
for x in myTuple:
  #print(x, end=" ")
  pass
end_time=time.time()
print()
print("Time taken to iterate tuple: ", end_time-start_time)