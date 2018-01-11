
# coding: utf-8

# In[21]:


f=open("births.csv","r")
text=f.read()
split_text=text.split("\n")
#print(split_text)


# In[22]:


dictionary={}
new_list=split_text[1:len(split_text)]
#print(new_list)


# In[19]:


for each in new_list:
    each_split=each.split(",")
    if each_split[3] in dictionary:
        dictionary[each_split[3]]=dictionary[each_split[3]]+int(each_split[4])
    else:
        dictionary[each_split[3]]=int(each_split[4])
       


# In[20]:


print(dictionary)


# I have done a count on number of births on the unique days of the week.
