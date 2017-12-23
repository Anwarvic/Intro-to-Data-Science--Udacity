from collections import OrderedDict
import pandas as pd
import math

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        # your code here
        df = pd.read_csv(name, header=None)
        updated_dict = OrderedDict()
        index = 0
        
        for idx, row in df.iterrows():
            lst = []
            beginning = row[:3]
            i = 0
            for item in row[3:]:
                if len(lst) == 0:
                    lst.extend(beginning)
                if type(item) in [long, float, int] and not math.isnan(item):
                    lst.append("%09d" % (item,))
                else:
                    lst.append(item)
                i += 1
                if i == 5:
                    updated_dict[index] = lst
                    lst = []
                    index += 1
                    i = 0
    
        df = pd.DataFrame(updated_dict).transpose().dropna(how='any').sort_values(by = [0, 1, 2, 3, 4], axis=0)
        df.to_csv("updated_"+name, index=False, header=None)
