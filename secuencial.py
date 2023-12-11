def compute(n):
    import time, socket
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

if __name__ == '__main__':
    import random, time 
    time1 = time.time()
    for i in range(10):
        result = compute(random.randint(5, 20))
        host, n = result
        print('%s executed job %s with %s' % (host, i, n))
    time2 = time.time()
    print("Tiempo final:", time2-time1)