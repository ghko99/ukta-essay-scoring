import pandas as pd

train = pd.read_csv('./train.csv',encoding='utf-8-sig')
valid = pd.read_csv('./valid.csv',encoding='utf-8-sig')
train_features = pd.read_csv('./train_features.csv',encoding='cp949')
valid_features = pd.read_csv('./valid_features.csv',encoding='cp949')

train_ids_list = train_features['essay_id'].to_list()
valid_ids_list = valid_features['essay_id'].to_list()

train = train[train['essay_id'].isin(train_ids_list)]
valid = valid[valid['essay_id'].isin(valid_ids_list)]

merged_train = pd.merge(train,train_features,on='essay_id')
merged_valid = pd.merge(valid,valid_features,on='essay_id')

merged_train.to_csv('./feat_train.csv',encoding='utf-8-sig',index=False)
merged_valid.to_csv('./feat_valid.csv',encoding='utf-8-sig',index=False)