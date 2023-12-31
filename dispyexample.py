# 'compute' is distributed to each node running 'dispynode'
def compute(n):
    import time, socket
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

if __name__ == '__main__':
    import dispy, random, time
    cluster = dispy.JobCluster(compute)
    jobs = []
    time1 = time.time()
    for i in range(10):
        # schedule execution of 'compute' on a node (running 'dispynode')
        # with a parameter (random number in this case)
        job = cluster.submit(random.randint(5,20))
        job.id = i # optionally associate an ID to job (if needed later)
        jobs.append(job)
    # cluster.wait() # waits for all scheduled jobs to finish
    for job in jobs:
        host, n = job() # waits for job to finish and returns results
        print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))
        # other fields of 'job' that may be useful:
        # print(job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time)
    time2 = time.time()
    cluster.print_status()
    print("Tiempo final dispy:",time2-time1)