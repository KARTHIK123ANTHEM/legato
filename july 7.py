#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import *   
def valid(a):
    if len(str(a))<=6:return False
    return True
def compare(c1,c2):
    c1=datetime.strptime(c1,"%d--%m--%Y")
    c2=datetime.strptime(c2,"%d--%m--%Y")
    return c2>=c1


# In[2]:


def overlap(s1,e1,s2,e2):
    overlap=[]
    if valid(s1) and valid(s2) and valid(e1) and not valid(e2):
        if compare(s1,s2) and compare(s2,e1):
            return ["","","",s2,"as ohi start falls in anthem dates"]
    if valid(s2) and valid(s1) and valid(e2) and not valid(e1):
        if compare(s2,s1) and compare(s1,e2):
            return ["","","",s1,"as anthem start falls in ohi dates"]
    if valid(s1) and valid(s2) and valid(e1) and valid(e2):
        if compare(s1,e1) and compare(s2,e2):
            if compare(s1,e2) and compare(s2,e1):
                if compare (s1,s2):
                    overlap.append(s2)
                    overlap.append("anthem")
                else:
                    overlap.append(s1)
                    overlap.append("ohi")
                if compare(e1,e2):
                    overlap.append(e1)
                else:
                    overlap.append(e2)
            overlap.append(overlap[0]+" to "+overlap[2])
        else:overlap.append("no overlap because there is  no overlap ")
        return overlap
    if not valid(s1) or not valid(e1):
        overlap.append("no overlap because one of the dates in anthem is missing")
    if not valid(s2) or not valid(e2):
        if len(overlap)==0:overlap.append("no overlap because one of the dates in ohi is missing")
        else:overlap[0]+=" and one of the dates in ohi is missing"
    return overlap
#print(overlap("1--2--2000","1--2--2003","1--2--2002","1--2--2004"))


# In[3]:


def check(cs1,ce1,cs2,ce2,s1,e1,s2,e2):
    dates=[]
    if valid(cs1):dates.append(cs1)
    else:dates.append(s1)
    if valid(ce1):dates.append(ce1)
    else:dates.append(e1)
    if valid(cs2):dates.append(cs2)
    else:dates.append(s2)
    if valid(ce2):dates.append(ce2)
    else:dates.append(e2)
    return overlap(dates[0],dates[1],dates[2],dates[3])
print(check("","","1/2/2003","","","1/2/2004","1/2/2000","1/2/2003")) 


# In[6]:


import pandas as pd
read_file = pd.read_excel (r'C:/Users/AI04833/OneDrive - Anthem/datesoverlap.xlsx')
read_file.to_csv (r'C:/Users/AI04833/OneDrive - Anthem/datesoverlap.csv',index = None, header=True)
df = pd.read_csv('C:/Users/AI04833/OneDrive - Anthem/datesoverlap.csv')
print(df.at[2,"CAQH start"])
df


# In[7]:


import csv
ind=df.index
print(ind)
header=['CAQH_start', 'CAQH end', 'CAQH ohi start', 'CAQH ohi end', 'wgs start','wgs end', 'ohi start', 'ohi end','overlap','description','primary']
with open('C:/Users/AI04833/OneDrive - Anthem/ans.csv','w') as f1:
    writer=csv.writer(f1,lineterminator='\n',)
    writer.writerow(header)
    for i in ind:
        over=check(df.at[i,"CAQH start"],df.at[i,"CAQH end"],df.at[i,"CAQH ohi start"],df.at[i,"CAQH ohi end"],df.at[i,"wgs start"],df.at[i,"wgs end"],df.at[i,"ohi start"],df.at[i,"ohi end"])
        if len(over)>2:
            ans=[df.at[i,"CAQH start"],df.at[i,"CAQH end"],df.at[i,"CAQH ohi start"],df.at[i,"CAQH ohi end"],df.at[i,"wgs start"],df.at[i,"wgs end"],df.at[i,"ohi start"],df.at[i,"ohi end"],over[0]+"to"+over[2],"all dates present",over[1]]
        else:
            ans=[df.at[i,"CAQH start"],df.at[i,"CAQH end"],df.at[i,"CAQH ohi start"],df.at[i,"CAQH ohi end"],df.at[i,"wgs start"],df.at[i,"wgs end"],df.at[i,"ohi start"],df.at[i,"ohi end"],"",over[0],"no primary"]
        writer.writerow(ans)
d=pd.read_csv('C:/Users/AI04833/OneDrive - Anthem/ans.csv')
d


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




