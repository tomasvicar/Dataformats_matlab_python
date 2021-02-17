
import h5py as h5



with h5.File("myfile3.h5", "r") as f:
    # datasetNames = [n for n in f.keys()]
    # for n in datasetNames:
    #     print(n)
        
        
    # DS1 = f['DS1']
    # print(DS1.shape)
    
    
    image = f['DS1'][0,...]
    
    
    
    
    
    
    
    
    
    
####write 
# f["train_img"][i, ...] = img[None] 


    

    
    
    
    









