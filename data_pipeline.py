from functions import *
import time
import datatime

print ("Starting data pipeline at ", datetime.datetime.now().striftime('%Y-%m-%d %H:%M:%S'))
print("------------------------------------")

#Step 1: Extract videos IDs
t0: time.time()
getVideoIDs()
t1 = time.time()
print ("Step 1:Done")
print ("----> Video IDs downloaded in", str(t1-t0), "seconds", "\n")


#Step 2: Extract transcriptions for videos 
t0: time.time()
getVideoTranscripts()
t1 = time.time()
print ("Step 2: Done")
print ("----> Transcripts downloaded in", str(t1-t0), "seconds", "\n" ")

#Step 3: Transform data
t0: time.time()
transformData()
t1 = time.time()
print ("Step 3: Done")
print ("----> Data transformed downloaded in", str(t1-t0), "seconds", "\n" ")

#Step 4: Generate text embeddings
t0: time.time()
createTexEmbeddings()
t1 = time.time()
print ("Step 4: Done")
print ("----> Embeddings generated in", str(t1-t0), "seconds", "\n" ")