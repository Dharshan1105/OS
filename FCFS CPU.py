#FCFS CPU Scheduling

processes=[
    {"process_id":1,"arrival_time":4,"brust_time":5},{"process_id":2,"arrival_time":6,"brust_time":4},
    {"process_id":3,"arrival_time":0,"brust_time":3},{"process_id":4,"arrival_time":6,"brust_time":2},
    {"process_id":5,"arrival_time":5,"brust_time":4}]


processes.sort(key= lambda process:process["arrival_time"])


#find turn around time,waiting time,completion time
current_time=0
for process in processes:
    if current_time<process["arrival_time"]:
        current_time=process["arrival_time"]

    process["comp_time"]=current_time + process["brust_time"]

    current_time=process["comp_time"]

    process["turnAround_time"]=process["comp_time"] - process["arrival_time"]

    process["waiting_time"]=process["turnAround_time"] - process["brust_time"]

print(processes)


#finding averavge turn around time and average waiting time 
tat=0
wt=0
for process in processes:
    tat+=process["turnAround_time"]
    wt+=process["waiting_time"]

avg_tat=tat/len(processes)
avg_wt=wt/len(processes)

print("average turn around time:",avg_tat)
print("average waiting time:",avg_wt)


"""Trun Around Time ---->Trun Around Time is a time interval which represent the time period between the completion time and arrival time (whitch
includes both brust time and waiting time)"""

"""waiting Time --->Waiting time is a time interval which represent the time period between the arrival time and execution time"""

    

  



    



