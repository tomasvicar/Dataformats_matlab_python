import imageio
import numpy as np

# pip install imageio
# pip install imageio-ffmpeg


file_name = 'out.avi'



frames = []

with imageio.get_reader(file_name) as f:
    for frame_num, frame in enumerate(f):
        
        frames.append(frame)
        
        
frames = np.stack(frames,axis=3)
            





