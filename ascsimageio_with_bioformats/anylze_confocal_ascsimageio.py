import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from aicsimageio import AICSImage
import xml.etree.ElementTree as ET
import xmltodict

# https://allencellmodeling.github.io/aicsimageio/
# hot fix of dimension incompatibility (dont know why):
# shape_tmp = data.shape
# dims_tmp = dims
# if len(shape_tmp) != len(dims_tmp):
#     # shape_tmp = shape_tmp[1:]
#     if isinstance(dims_tmp, list):
#         dims_tmp = ['W', ] + dims_tmp
#     else:
#         dims_tmp = ('W', ) + dims_tmp

# coords, dims = _infer_coords_and_dims(shape_tmp, coords, dims_tmp)

def hex_to_rgb_list(color_hex):
    # Check for the '#' at the start and remove it
    if color_hex.startswith("#"):
        color_hex = color_hex[1:]
        
    # Extract the RGB components and convert them to integers
    r = int(color_hex[0:2], 16)
    g = int(color_hex[2:4], 16)
    b = int(color_hex[4:6], 16)
    
    return [[r], [g], [b]]


path = "../Smrt_Exosomy_FADU"
path_save = "../res_Smrt_Exosomy_FADU" 

fnames = glob.glob(path + '/*.czi')

for ind_fname, fname in enumerate(fnames):
    
    img_aics = AICSImage(fname)
    # img_aics.dims = [1] + img_aics.dims 
    img = img_aics.data.squeeze()
    channel_names = img_aics.channel_names 
    physical_pixel_sizes = img_aics.physical_pixel_sizes
    
    metadata = xmltodict.parse(ET.tostring(img_aics.metadata, encoding='utf8').decode('utf8'))
    dyes = []
    colors = []
    for channel_meta in metadata['ImageDocument']['Metadata']['DisplaySetting']['Channels']['Channel']:
        dyes.append(channel_meta['DyeName'])
        colors.append(hex_to_rgb_list(channel_meta['Color']))
    
    
    plt.imshow(img[0, :, :])
    plt.show()
    
    
    
    
    
        
        
        
    
        
    
    
    # computed_data = img_aics.dask_data.reshape(-1).compute()
    # img = np.array(computed_data)


    # img = np.array(img_aics.dask_data)
    # img_aics.dims
    # img_aics.get_image_data(T=0, Z=0, C=0)
    
    # dgfgfdgf
    
    # print(img_aics.dask_data.shape)
    # print(img_aics.dask_data.ndim)
    
