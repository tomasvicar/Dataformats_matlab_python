import numpy as np
import SimpleITK as sitk


fname = 'test6.mhd'
shape = [2,3,4,5,6]

A = np.arange(np.prod(shape)).reshape(shape)

writer = sitk.ImageFileWriter()
writer.SetImageIO("MetaImageIO")
writer.SetFileName(fname)
writer.Execute(sitk.GetImageFromArray(A))




file_reader = sitk.ImageFileReader()
file_reader.SetFileName(fname)
file_reader.ReadImageInformation()
B=sitk.GetArrayFromImage(file_reader.Execute())


tmp = A!=B
print(np.sum(tmp))




