#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip freeze | grep scikit-learn


# In[1]:


import sklearn
sklearn.__version__


# In[2]:


import pickle
import pandas as pd


# In[3]:


with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)


# In[4]:


categorical = ['PUlocationID', 'DOlocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[5]:


year = 2021
month = 2


# In[6]:


df = read_data(f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet')


# In[7]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = lr.predict(X_val)


# In[8]:


y_pred.mean()


# In[ ]:





# In[9]:


df_result = pd.DataFrame()
df_result['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
df_result['prediction'] = y_pred


# In[11]:


df_result.head(3)


# In[12]:


df_result.to_parquet(
    'df_result.parquet',
    engine='pyarrow',
    compression=None,
    index=False
)


# In[ ]:




