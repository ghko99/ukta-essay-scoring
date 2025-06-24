import pandas as pd
import json

with open('./essay_info.json','r',encoding='utf-8-sig') as f:
    essay_info = json.load(f)

valid = pd.read_csv('./feat_valid.csv',encoding='utf-8-sig')

high_school_valid = valid[valid['essay_id'].apply(lambda x: essay_info[x]['학교'] == '고등')]


subjects = list(set(high_school_valid['essay_main_subject'].to_list()))

df_per_subjects = []
high_school_essay_info = dict()
for sub in subjects:
    df = high_school_valid[high_school_valid['essay_main_subject'] == sub]
    df_per_subjects.append(df)
    high_school_essay_info[sub] = {"low_score_essays":[], "high_score_essays":[]}


for i in range(len(df_per_subjects)):
    top_10 = df_per_subjects[i].nlargest(10, "essay_scoreT_avg")
    bottom_10 = df_per_subjects[i].nsmallest(10,"essay_scoreT_avg")

    for k in range(len(top_10)):
        essay_id = top_10.iloc[k]['essay_id']
        score = top_10.iloc[k]['essay_scoreT_avg']
        essay = top_10.iloc[k]['essay']
        high_school_essay_info[subjects[i]]['high_score_essays'].append({"essay_id":essay_id, "score":score, "essay":essay})
    
    for k in range(len(top_10)):
        essay_id = bottom_10.iloc[k]['essay_id']
        score = bottom_10.iloc[k]['essay_scoreT_avg']
        essay = bottom_10.iloc[k]['essay']
        high_school_essay_info[subjects[i]]['low_score_essays'].append({"essay_id":essay_id, "score":score, "essay":essay})

with open("high_school_essay_info.json",'w',encoding='utf-8-sig') as f:
    json.dump(high_school_essay_info,f,indent='\t',ensure_ascii=False)

