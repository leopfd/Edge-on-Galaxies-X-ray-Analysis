#!/usr/bin/env python
# coding: utf-8

# In[47]:


import os
from ciao_contrib.runtool import *
import glob
import pycrates as pcr
from paramio import *
from crates_contrib.utils import *
import numpy as np

objList = sorted(glob.glob("NGC*"))
#print(objList)


for obj in objList[7:30:]:
    print("RUNNING {}".format(obj))
    fileList = glob.glob('{}/*/repro/*reproj*'.format(obj))
    #print(fileList)
    #infiles=str(fileList).strip('[]')
    #print(infiles)
    srcflux.punlearn
    srcflux.bands="0.3:1.5:0.92","1.5:7:3.8"
    srcflux.bkgresp="False"
    srcflux.psfmethod="arfcorr"
    srcflux.clobber="True"
    #print(srcflux)
    srcflux(infile="{}/*/repro/*reproj*".format(obj),pos="{}/sources/merged_0.3-7_src.fits".format(obj),outroot="{}/sources/srcflux/src".format(obj))
    print("FINISHED {}".format(obj))


# In[ ]:





# In[ ]:




