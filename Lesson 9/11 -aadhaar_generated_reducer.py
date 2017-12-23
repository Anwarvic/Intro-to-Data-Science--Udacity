import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    word_counts = {}
    old_key = None
    value = 0
    for line in sys.stdin:
        data = line.strip().split("\t")
        key, count = data[0], int(data[1])
        if key != old_key and old_key != None:
            print old_key + "\t" + str(value)
            value = 0
        old_key = key
        value += count
    if old_key != None:
        print old_key + "\t" + str(value) 

reducer()
