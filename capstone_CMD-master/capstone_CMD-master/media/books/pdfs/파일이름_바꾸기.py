#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import glob

input_dir = input("Input Directory : ")
input_data_name = input("Input Data Name : ")

for idx, fname in enumerate(glob.glob(input_dir + "\\*.jpg")): # get *.jpg file to list type
    os.rename(fname, input_data_name + "_" + str(idx) + ".jpg") # file name change !

if not os.path.isdir('./{}'.format(input_data_name)):
     os.mkdir('./{}'.format(input_data_name))


# In[ ]:




