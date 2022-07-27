#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import requests
import io


# In[2]:


pip install requests


# In[2]:


import pandas as pd
import requests
import io
import re, json


# In[3]:


url = 'https://raw.githubusercontent.com/annexare/Countries/master/data/languages.json'
resp = requests.get(url)
data = json.loads(resp.text)
datas = pd.DataFrame(data)


# In[4]:


data_T = datas.T


# In[88]:


Language = data_T.reset_index()


# In[90]:


Language.rename(columns = {"index":"LangCode"}, inplace =True)
Language.rename(columns = {"name":"Country"}, inplace =True)


# In[91]:


Language.drop("rtl",axis=1,inplace=True)


# In[92]:


Language


# In[7]:


url = 'https://raw.githubusercontent.com/annexare/Countries/master/data/countries.json'
resp = requests.get(url)
data = json.loads(resp.text)
dataC = pd.DataFrame(data)


# In[8]:


dataC_T = dataC.T


# In[9]:


countries = dataC_T.reset_index()


# In[27]:


countries.rename(columns = {"name":"Country", "index":"CountryCode"}, inplace =True)


# In[40]:


countries


# In[39]:


countries.drop("continents",axis=1,inplace=True)


# In[11]:


url = 'https://raw.githubusercontent.com/annexare/Countries/master/data/continents.json'
resp = requests.get(url)
data = json.loads(resp.text)
dataCo = pd.DataFrame(data,index=[0])


# In[12]:


Continent = dataCo.T.reset_index()


# In[33]:


Continent.rename(columns = {"index":"ContinentCode"}, inplace =True)
Continent.rename(columns = {0:"Continent"}, inplace =True)


# In[34]:


Continent


# In[14]:


currency = countries[["index","name","currency"]]


# In[35]:


currency.rename(columns = {"index":"CurrencyCode","name":"Country"}, inplace =True)


# In[36]:


currency


# In[63]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:test@localhost/User'

db = create_engine(conn_string)
conn = db.connect()

currency.to_sql('currency', con=conn, if_exists='replace',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()

sql1 = '''select * from currency;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()


# In[93]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:test@localhost/User'

db = create_engine(conn_string)
conn = db.connect()

Language.to_sql('language', con=conn, if_exists='replace',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()


# In[94]:


sql = '''select * from language;'''


# In[96]:


cursor.execute(sql)


# In[97]:


for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()


# In[98]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:test@localhost/User'

db = create_engine(conn_string)
conn = db.connect()

countries.to_sql('countries', con=conn, if_exists='replace',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()

sql1 = '''select * from countries;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()


# In[ ]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


conn_string = 'postgresql://postgres:test@localhost/User'

db = create_engine(conn_string)
conn = db.connect()

Continent.to_sql('Continent', con=conn, if_exists='replace',index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()

sql1 = '''select * from Continent;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

# conn.commit()
conn.close()


# In[ ]:




