
# coding: utf-8

# In[ ]:


import requests
import json

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r=requests.post(url,json={"LIMIT_BAL":400000,
                          "MARRIAGE":1,
                          "EDUCATION":1,
                          "SEX":2,
                          "AGE":35,
                          "PAY_1":1,
                          "PAY_2":2,
                          "PAY_3":0,
                          "BILL_AMT1":33720,
                          "BILL_AMT2":29480,
                          "BILL_AMT3":33720,
                          "PAY_AMT1":15000,
                          "PAY_AMT2":15000,
                          "PAY_AMT3":12000})
print(r.json())

