# FCFS CPU Scheduling Algorithm

This project implements the First Come First Served (FCFS) CPU scheduling algorithm in Python. FCFS is a non-preemptive scheduling algorithm where processes are scheduled based on their arrival time in the ready queue. The process that arrives first gets executed first, regardless of its burst time.

## Code Explanation

The code defines a list of processes, each represented as a dictionary with the following keys:

- `process_id`: Unique identifier for the process.
- `arrival_time`: Time at which the process arrives in the ready queue.
- `brust_time`: Time required by the process for execution (CPU burst time).

The code then sorts the processes based on their arrival times using `processes.sort(key=lambda process: process["arrival_time"])`. This ensures FCFS scheduling.

A loop iterates through each process, calculating its completion time, turn-around time, and waiting time. Here's the breakdown:

- `current_time`: Tracks the current time during scheduling, initially set to 0.
- `process["comp_time"] = current_time + process["brust_time"]`: Calculates the completion time by adding the current time and burst time.
- `current_time = process["comp_time"]`: Updates the current time to reflect the completion time.
- `process["turnAround_time"] = process["comp_time"] - process["arrival_time"]`: Calculates the turn-around time.
- `process["waiting_time"] = process["turnAround_time"] - process["brust_time"]`: Calculates the waiting time.

Finally, the code prints the list of processes with their details and calculates the average turn-around time and average waiting time for all processes.

## Turn-Around Time (TAT) and Waiting Time (WT)

- **Turn-Around Time (TAT):**
  - Represents the total time a process spends in the system from arrival to completion (including execution and waiting time).
  - In FCFS, processes may experience longer TATs if earlier arriving processes have longer burst times.
- **Waiting Time (WT):**
  - Represents the time a process spends waiting in the ready queue before execution.
  - Processes arriving earlier typically have lower WT compared to later arrivals in FCFS.

## Running the Code

1. Save the code as a Python file (e.g., `fcfs.py`).
2. Run the script using `python fcfs.py`.

The output will display the list of processes with their details and the calculated average turn-around time and average waiting time.
