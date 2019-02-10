import time
import zmq
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift
import seciqlib
from joblib import dump, load
import nnclassifier as nn

'''
def run_capture_hackrf(sleep_time=0.025, loop_iterations=10):
    print("Creating top_block class...")
    tb=top_block.top_block()

    print("Starting top_block...")
    tb.start()
    print("Started...")

    for _ in range(loop_iterations):
        print("starting...")
        tb.set_trigger(1)
        time.sleep(sleep_time)
        tb.set_trigger(-1)   
        time.sleep(0.5)
        print("")
    return 1
'''

def genTraceFiles():
    

#%matplotlib inline

# Ref: https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html

def consumer():
    consumer_id = random.randrange(1,10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    
    # The data segment which we need to be filled
    # sample-rate x time = num-samples
    # 20MHz X 10ms = 200000
    sampleLimit = 200000
    
    # initializing segment buffer
    segment = np.empty([0,0])
    
    # load the pre-trained model
    # From: https://drive.google.com/drive/folders/1UaREal6CJdcO6LxA5-mgdIv0hdZokmZ8?usp=sharing
    clf = load('10-class-neural-network-model-joblib.model') 
    
    # log file name
    #file_name = "samplerate-"+str(sampleLimit)+"-processing-times.txt"
    #filepr = open(file_name,'w+') 
    
    while True:
        buff = consumer_receiver.recv()
        #print(time.time())
        data = np.frombuffer(buff, dtype="float32")
        data = data[0::2] + 1j*data[1::2]        
        segment = np.append(segment, data)
        #print(type(segment))
        #print(len(segment))
        if(len(segment) >= sampleLimit):
            #print("Segment collected...")
            start_time = time.time()
            print("Timestamp: ", start_time, " milliseconds")
            feature_vector = seciqlib.getFeatureVector(segment[0:sampleLimit])
            #print("Feature vector created...")
            label = nn.predictClass(clf, [feature_vector.tolist()])
            #print("Classified...")
            print("Label: ", label)
            
            #processing_time = (time.time()-start_time)*1e3
            #print("Processing Time: ", processing_time, " milliseconds")
            #filepr.write(str(processing_time)+"\n")
            #filepr.flush()
            
            # Reset the segment
            segment = np.empty([0,0])
            
        
        #plt.psd(data, NFFT=len(data), Fs=4e6, Fc=1e3)
        #plt.plot(np.abs(data))
        #plt.show()
        #time.sleep(0.5)
        #return 1
        
consumer()