import time
WAIT_TIME = 3

while True:

    startTime = time.time()
    print "test"
    endTime = time.time()

    if endTime - startTime < WAIT_TIME:
        time.sleep(WAIT_TIME - (endTime - startTime))
