def job_scheduling(jobs):
    n = len(jobs)
    # sort the jobs based on their ending time
    jobs.sort(key=lambda x: x[1])

    # keep track of the maximum profit and the number of jobs
    max_profit = 0
    count = 0

    # use an array to keep track of the latest ending time of a job
    latest_ending_time = -1

    for i in range(n):
        # if the current job does not overlap with the latest ending time
        if jobs[i][0] >= latest_ending_time:
            # update the latest ending time
            latest_ending_time = jobs[i][1]
            # update the maximum profit
            max_profit += jobs[i][2]
            # increase the count of jobs
            count += 1
            
    print("The number of tasks and earnings available for others\n Task:",count)
    return max_profit

n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    start_time = int(input("Enter start time: "))
    end_time = int(input("Enter end time: "))
    profit = int(input("Enter profit: "))
    jobs.append((start_time, end_time, profit))
sum=job_scheduling(jobs)
print("Earnings:",sum)
