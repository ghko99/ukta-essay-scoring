import json
import os
import shutil
with open('./json_per_score/high_school_essay_info.json','r',encoding='utf-8-sig') as f:
    essay_info = json.load(f)

for key, val in essay_info.items():
    subjects = key
    low_score_essays = [essay['essay_id'] for essay in val['low_score_essays']]
    high_score_essays = [essay['essay_id'] for essay in val['high_score_essays']]

    src_dir = './valid_json/'
    low_score_dst_dir = './json_per_score/' + subjects.replace('/','-') + '/low_score_essays/'
    high_score_dst_dir = './json_per_score/' + subjects.replace('/','-') + '/high_score_essays/' 
    for essay in low_score_essays:
        file_name = essay + '.json'
        shutil.copy(src_dir+file_name, low_score_dst_dir+file_name)
    for essay in high_score_essays:
        file_name = essay + '.json'
        shutil.copy(src_dir+file_name, high_score_dst_dir+file_name)
