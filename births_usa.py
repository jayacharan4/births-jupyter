
# coding: utf-8

# In[8]:


file=open("US_births_1994-2003_CDC_NCHS.csv","r")
string=file.read()
split_string=string.split("\n")
split_string[0:10]


# In[5]:


def read_csv(file_name,header=False):
    file=open(file_name,"r")
    string=file.read()
    split_string=string.split("\n")
    if header==True:
        string_list=split_string[1:len(split_string)]
    final_list=[]
    for each in string_list:
        int_fields=[]
        string_fields=each.split(",")
        for every_element in string_fields:
            int_fields.append(int(every_element))
        final_list.append(int_fields)
    return final_list
    
    


# In[30]:


cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv",True)
cdc_list[1:10]


# In[11]:


def month_births(list):
    births_per_month=dict()
    for each in list:
        month=each[1]
        births=each[4]
        if month in births_per_month:
            births_per_month[month]=births_per_month[month]+births
        else:
            births_per_month[month]=births
    return births_per_month

    


# In[20]:


cdc_month_births=month_births(cdc_list)
print(cdc_month_births)


# In[21]:


def dow_births(list):
    unique_week_births=dict()
    for each in list:
        day_of_week=each[3]
        births=each[4]
        if day_of_week in unique_week_births:
            unique_week_births[day_of_week]=unique_week_births[day_of_week]+births
        else:
            unique_week_births[day_of_week]=births
    return unique_week_births


# In[22]:


cdc_day_births=dow_births(cdc_list)
print(cdc_day_births)


# In[31]:


def calc_counts(data,column):
    dictionary=dict()
    if column=="year":
         column=0
    if column=="month":
        column=1
    if column=="date_of_month":
        column=2
    if column=="day_of_week":
        column=3
    for each in data:
        column_data=each[column]
        births=each[4]
        if column_data in dictionary:
            dictionary[column_data]=dictionary[column_data]+births
        else:
            dictionary[column_data]=births
    return dictionary

        


# In[32]:


cdc_year_births=calc_counts(cdc_list,"year")
cdc_month_births=calc_counts(cdc_list,"month")
cdc_dom_births=calc_counts(cdc_list,"date_of_month")
cdc_dow_births=calc_counts(cdc_list,"day_of_week")


# In[34]:


cdc_year_births

