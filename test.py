from emvincelib import iq, ml
import numpy as np

zmqSocket = iq.startZMQClient()

iq.genTraceFiles(zmqSocket, "./data", "AES", 10)

iq.stopZMQClient(zmqSocket)

data = np.load("./data/AES.1.npy")
print(len(data))
featureVector = ml.getFeatureVector(data)
print(len(featureVector))
iq.plotPSD(data, show=1)
