import livia_client as client
import sys
import time
import math
print("connecting to "+sys.argv[1])
logger = client.logger(sys.argv[1],"")
print(logger.number)
count=0
while True :
    count+=.1
    logger.log(math.sin(count))
    print("logged: ",math.sin(count))
    time.sleep(2)

