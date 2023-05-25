
import json
import pandas as pd


# Read CSV into a dataframe
df = pd.read_csv("mqp.csv")

# Create an empty list to store JSON objects
json_list = []

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Create a dictionary for the row
    row_dict = {}
    new_dict = {}
    row_dict['question'] = row[1]
    json_list.append(row_dict)
    new_dict['question'] = row[2]
    json_list.append(new_dict)
    #row_dict['long_question'] = row[2]

# Convert the list of JSON objects to a JSONL string
jsonl_str = ""


with open("medical.jsonl", "w") as file:
    for json_obj in json_list:
        jsonl_str = json.dumps(json_obj) + "\n"
        file.write(jsonl_str)


