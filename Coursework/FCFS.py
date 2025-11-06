# FCFS Scheduling Algorithm Implementation

def calculate_fcfs(processes):
    n = len(processes)
    burst_time = [process[1] for process in processes]  # Extracting burst times
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculating waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculating turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return processes, burst_time, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

def main():
    # Collecting user inputs for processes
    processes = []
    while True:
        try:
            process_number = int(input("Enter Process Number (or -1 to end): "))
            if process_number == -1:
                break
            
            burst_time = int(input(f"Enter Burst Time for Process {process_number}: "))
            processes.append((process_number, burst_time))
        
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    # Calculating values
    results = calculate_fcfs(processes)

    # Displaying results
    print("\nProcess Number\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(results[0])):
        print(f"{results[0][i][0]}\t\t{results[1][i]}\t\t{results[2][i]}\t\t{results[3][i]}")

    print(f"\nAverage Waiting Time: {results[4]:.2f}")
    print(f"Average Turnaround Time: {results[5]:.2f}")

if __name__ == "__main__":
    main()
