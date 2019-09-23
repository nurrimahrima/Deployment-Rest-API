# Deployment-Rest-API
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
**I. Introduction**
This is Machine Learning Deployment by Rest API. <br>
Application Programming Interface (API) is interface in the form of a set of functions, communication protocols, or tools that can be run by other programs. Where interface is the same part between two or more separate components in a computer system.

There are several applications of API, such as:
  1. Programming Language
  2. Library & Framework
  3. Operation System
  4. Web API/ Web Services
     Web API is a software system created to support interaction between 2 different applications over a network. There are two types of      Web Services, they are SOAP ( Sample Object Access Protocol) and REST (Representational State Transfer). REST API is the most            popular used among them.

This repository will demonstrate one of the implementation of REST API and our use case is Credit Scoring prediction. This Machine Learning API demonstration is using *Flask*, a web framework in Python, and then it will be deployed on API testing called *Postman*.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
**II. Summary Steps**
  1. Build a model using Jupyter Notebook, which is Credit Scoring prediction using Decision Tree.
  2. Save the model object as a pickle file (serialization) => 'DecisionTree.pkl'
  3. Create flask environment that will have an API endpoint.  
  4. Upload the flask script along with the trained model on *pythonanywhere*. 
  5. Make requests to the hosted flask script through *Postman*.

In the coding part, there will be three files created:
  1. modelCredit.py => to create model 
  2. serverDT.py => handle POST request and return result 
  3. requestDT.py => to send request 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖ 
**III. Datasets**
  - AGE <br>
  - LIMIT_BAL = Credit Limit<br>
  - EDUCATION = Education Level <br>
    1: S2/S3 <br>
    2: Dipl/S1 <br>
    3: SMA <br>
    4: Lainnya <br>
  - MARRIAGE = Marriage Status<br>
    1: Belum Menikah <br>
    2: Menikah <br>
    3: Lainnya <br>
  - SEX <br>
    1: Pria <br>
    2: Wanita <br>
  - PAY_1, PAY_2, PAY_3	= Late Payment <br>
    0: Tepat waktu <br>
    1: Terlambat 1 bulan, dst <br>
  - BILL_AMT1, BILL_AMT2, BILL_AMT3 = Bill Amount <br>
  - PAY_AMT1, PAY_AMT2, PAY_AMT3 = Pay Amount <br>
  
**All the customer will input the data as the data listed above**
The result of this prediction will be:
  0 = 'Tidak Terlambat' if the account is predicted not to be late paying
  1 = 'Terlambat' if the account is predicted to be late paying
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
**IV. How The Model Interface Works**
As statement above, this API deployment will be testing on API testing called *Postman*. How the user interface in Postman works will be explained in the notepad => 'how_test_works.txt'
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
**V. Interpretation**
- If the results issued are 'Tidak Terlambat' then it means that it is possible that the account will not make late payments in the next   several periods. Some actions that can be taken include:
    1. provide notification to keep credit within the middle to low risk limit
    2. giving promos or compensation for being a good creditor
    3. provide special treatment so that creditors can recommend the program to others
    4. retain customers to become loyal customers

- If the results issued are 'Terlambat' then it means that it is possible that the account will make late payments in the next several     periods. Some actions that can be taken include:
    1. give a warning for the late payment
    2. announce the sanctions if notifications are ignored
    3. terminating the creditor's account

 



