#!/usr/bin/env python
# coding: utf-8

# In[6]:


import glob
import os
from ciao_contrib.runtool import *
#cd 

#fileList = glob.glob("*_evt2.fits")

#for file in fileList:
a = dmkeypar("NGC660/1633/repro/acisf01633_repro_evt2.fits", OBSID, RA_TARG, DEC_TARG, INSTRUME, LIVETIME, ROLL_PNT, DATE-OBS) 
print(a)


# In[3]:




