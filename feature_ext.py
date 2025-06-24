import pandas as pd
from apps.cohesion.process import process
from apps.cohesion.process import initialize_models
import json
from tqdm import tqdm

initialize_models()    
train = pd.read_csv('./train.csv',encoding='utf-8-sig')
valid = pd.read_csv('./valid.csv',encoding='utf-8-sig')

for i in tqdm(range(len(train))):
    essay_id = train.iloc[i]['essay_id']
    essay = train.iloc[i]['essay']
    try:
        features = process(essay)
        with open('./train_json/' + essay_id + '.json','w',encoding='utf-8-sig') as f:
            json.dump(features,f,indent='\t',ensure_ascii=False)
        f.close()
    except:
        continue

for i in tqdm(range(len(valid))):
    essay_id = valid.iloc[i]['essay_id']
    essay = valid.iloc[i]['essay']
    try:
        features = process(essay)
        with open('./valid_json/' + essay_id + '.json','w',encoding='utf-8-sig') as f:
            json.dump(features,f,indent='\t',ensure_ascii=False)
        f.close()
    except:
        continue