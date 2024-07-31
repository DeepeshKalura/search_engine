
# term frequency 

import os
import sys
from collections import defaultdict
import json
from typing import List

#INFO: We are ussing that we have a crawler which gives me output in the /app/file path for current project

# indexing loginc  hai
def indexLogic() -> None:
    #INFO: This function will create a JSON file in /app/files/refine we will get the preocess json which we will use provide logic
    path = os.getcwd() + "/app/files"
    for filename in os.listdir(path):
        if(filename != "refine"):
            file_data = defaultdict(int)
            with open(path+"/"+filename, "r") as f:
            # INFO: Working Default Dict Functionality from collections
            # print(file_data)
            # file_data["shiva"] += 1
            # print(file_data)
            # Simple it create an O for each word
                for line in f:
                    for word in line.split():
                        file_data[word] += 1 

                f_name = filename.split(".")[0]
                with open(path+"/"+"refine"+"/"+f_name+".json", "w") as cjf:
                    cjf.write(json.dumps(file_data))

# ranking logic 
def rankLogic(query:str) -> List:
    path = os.getcwd() + "/app/files/refine"
    temp = defaultdict(int)
    query_breaker = query.split()
    for filename in os.listdir(path):
        with open(path+"/"+filename, "r") as f:
            data = json.load(f)
            res = defaultdict(int, data)
    #print(query_breaker)
        for i in query_breaker:
            temp[filename]+=res[i]
        
        sort_temp = sorted(temp.items(), key=lambda item: item[1], reverse=True) 

    return sort_temp

print(rankLogic("the index"))
    

# user frontend
