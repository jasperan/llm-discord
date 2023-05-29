'''
@
'''

dir_list = [
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

import os
import json
from bs4 import BeautifulSoup
import requests

def process_xml_files(root_dir):
    data = []
    for subdir, dirs, files in os.walk(root_dir):
        iterator = 0
        for file in files:
            print('[{}][{}]'.format((iterator / len(files))*100, file))
            if file.endswith('.xml'):

                filepath = subdir + '/' + file

                #print(filepath)
                with open(filepath, 'r', encoding='utf-8') as xml_file:
                    soup = BeautifulSoup(xml_file, 'lxml')
                    #print(soup)
                    qapair_parent = soup.find('qapairs')
                    #print(qapair_parent)
                    qapairs = soup.find_all('qapair')
                    #print(len(qapairs))
                    for qapair in qapairs:
                        question = qapair.find('question')
                        answer = qapair.find('answer')
                        #print(question, answer)
                        # Both question and answer exist and are non-empty
                        if question and question.text.strip() and answer and answer.text.strip():
                            # Clean up the text by replacing tabs, newlines, and multiple spaces with a single space
                            clean_question = ' '.join(question.text.split())
                            clean_answer = ' '.join(answer.text.split())
                            data.append({
                                "instruction" : "You are a medical expert and you will answer questions related to medical inquiries.",
                                "input": clean_question,
                                "output": clean_answer,
                            })
            iterator += 1
    return data

def write_json_file(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

#root_dir = '/home/datascience/MedQuAD/1_CancerGov_QA/'  # Change this to the root directory of your XML files
output_file = 'output.json'  # The file where you want to store your JSON data


for x in dir_list:
    #print(x)
    data = process_xml_files('{}{}'.format('H:/datasets/MedQuAD/', x))
    #print(len(data))
    write_json_file(data, 'output_{}.json'.format(x))