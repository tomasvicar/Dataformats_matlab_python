### first install java development kit (jdk) - on windows: download and install exe, add "jdk_path"/bin to Path enviromental variable
### pip install python-bioformats   - https://pythonhosted.org/python-bioformats/

fname = 'test3.tif'


import bioformats as bf
import javabridge 
import numpy as np
from read_image_series import read_image_series

shape = [2,3,4,5,6]

A = np.arange(np.prod(shape)).reshape(shape)+0.1




# javabridge.start_vm(class_path=bf.JARS)

# bf.formatwriter.write_image(fname,A,bf.omexml.PT_DOUBLE)
# bf.write_image(fname,A,bf.PT_UINT16)


B = read_image_series(fname)




# B = bf.load_image(fname) #3D - moreD reads one by one

# javabridge.kill_vm()











