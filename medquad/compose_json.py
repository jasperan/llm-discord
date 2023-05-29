 
import json
import os
from rich import print

# list of file names
file_list = [
    '10_MPlus_ADAM_QA',
    '2_GARD_QA',
    '6_NINDS_QA',
    '11_MPlusDrugs_QA',
    '3_GHR_QA',
    '7_SeniorHealth_QA',
    '12_MPlusHerbsSupplements_QA',
    '4_MPlus_Health_Topics_QA',
    '8_NHLBI_QA_XML',
    '1_CancerGov_QA',
    '5_NIDDK_QA',
    '9_CDC_QA',
]

full_contents = list()



# function to read and join contents of json files
def read_json_files(file_list):
    global full_contents
    contents = list()
    for file_name in file_list:
        with open('{}_{}.json'.format('output', file_name), 'r') as f:
            data = json.load(f)
            contents.append(data)
            for x in data:
                full_contents.append(x)
            #print(type(data[1]))
            #print(contents)
    return contents

# call function to read and join contents of json files
unique_file = read_json_files(file_list)

print(len(full_contents))
#print(unique_file)

# write unique_file to a .json file
with open('unique_file.json', 'w') as new_file:
    json.dump(full_contents, new_file)
