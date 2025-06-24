import collections
import re
import json
from konlpy.tag import Kkma
import os
import pandas as pd

# text 문장 단위 분할하기
def splitText(text):
    sens = collections.deque()
    sentences = re.split("(?<=\. )|(?<=\? )|(?<=\! )|(?<=\n)", text)
    for item in sentences:
        if len(item) > 0 and item[0] != "\n" and item[0] != " " and item[0] != "\t" and item[0] != "\r":
            sens.append(item)
    return sens

with open('./essay_info.json','r',encoding='utf-8-sig') as f:
    file = json.load(f)

dirs = os.listdir('./json_per_score')[1:]


examples = dict()

for dir in dirs:
    low_score_essays = os.listdir('./json_per_score/' + dir + '/low_score_essays')
    high_score_essays = os.listdir('./json_per_score/' + dir + '/high_score_essays')
    low_score_essay_txt = []
    high_score_essay_txt = []
    if file[high_score_essays[0].replace('.json','')]['학년'] == '1학년':
        print(dir)
        continue
    for low_score_essay in low_score_essays:
        
        with open('./json_per_score/' + dir + '/low_score_essays/' + low_score_essay,'r',encoding='utf-8-sig') as f:
            essay = json.load(f)
        f.close()
        sentences = essay["morpheme"]['sentences']
        txt = ''
        for sent in sentences:
            txt = txt + sent['text']['content'] + '\n'
        low_score_essay_txt.append(txt)
    
    for high_score_essay in high_score_essays:
        
        with open('./json_per_score/' + dir + '/high_score_essays/' + high_score_essay,'r',encoding='utf-8-sig') as f:
            essay = json.load(f)
        f.close()
        sentences = essay["morpheme"]['sentences']
        txt = ''
        for sent in sentences:
            txt = txt + sent['text']['content'] + '\n'
        high_score_essay_txt.append(txt)
    
    examples[dir] = {"high_score_essays" : high_score_essay_txt, "low_score_essays": low_score_essay_txt}

with open('./examples.json','w',encoding='utf-8-sig') as f:
    json.dump(examples,f,indent='\t',ensure_ascii=False)
f.close()
        