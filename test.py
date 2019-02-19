from emvincelib import iq, ml
import numpy as np
import time

#zmqSocket = iq.startZMQClient()
#iq.genTraceFiles(zmqSocket, "./data", "AES", 10)
#iq.stopZMQClient(zmqSocket)
#data = np.load("./data/AES.1.npy")
#print(len(data))
#featureVector = ml.getFeatureVector(data)
#print(len(featureVector))
#iq.plotPSD(data, show=1)

###############################################################################

# User defined function to process the sliding window data
def processWindow(window, a,b):
    print(len(window))
    print("param1: %d param2: %d" % (a,b))
    tempFileName= "./data/AES" + "." + str(time.time()) + ".npy"
    np.save(tempFileName, window)

zmqSocket = iq.startZMQClient()

sampleRate=20e6
iq.startSlidingWindow(zmqSocket, processWindow, (1, 2), sampleRate, 10, 5, 10)

iq.stopZMQClient(zmqSocket)
