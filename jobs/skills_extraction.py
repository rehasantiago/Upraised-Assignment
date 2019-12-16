from os import walk
import csv
import os
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
import sys
import json
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

class Skill_extract:
    def __init__(self):
        self.load_skill_mapping(os.path.join(os.path.dirname(__file__), "skillname_to_skilltags.tsv"))
        
    def load_skill_mapping(self, filename):
        self.skill_map = {} 
        f = open(filename, "r")
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            self.skill_map[row[0]] = row[1]
            
        f.close()

    def map_skill_to_job_id(self, job_text, method='local'):

        all_matched_skills  = []
        # print "job_text", jobtext
        # print(self.stop_words)
        
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(job_text) 
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        tx = CountVectorizer(ngram_range=(1,2))
        vx = tx.fit_transform([''.join(a+' ' for a in filtered_sentence)])
        job_set = set(tx.get_feature_names())
        print(job_set)
        i  = 0
        for skill, ft in self.skill_map.items():
            matched_skills = {}
            skill_set = set(ft.split(","))
            intersect = job_set.intersection(skill_set)
            #print(intersect)
            if len(intersect) >0:
                all_matched_skills.append(skill)
            
        return all_matched_skills

    def process(self, job_text, method='local'):
        response = self.map_skill_to_job_id(job_text, method=method)
        return ','.join(r for r in response)


