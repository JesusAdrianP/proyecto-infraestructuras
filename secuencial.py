def compute(n):
    import time, socket
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

if __name__ == '__main__':
    import random
    jobs = []
    for i in range(10):
        result = compute(random.randint(5, 20))
        host, n = result
        print('%s executed job %s with %s' % (host, i, n))