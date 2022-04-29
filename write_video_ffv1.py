import numpy as np
import ffmpeg


# FFmpeg must be installed and accessible via the $PATH environment variable.
# https://ffmpeg.org/download.html#build-windows
# download folder and add this folder to path https://windowsloop.com/install-ffmpeg-windows-10/
 


frames = (np.random.rand(100,200,3,50)*255).astype(np.uint8)
frame_rate = 25 
file_name = 'out.avi'

ff_proc = (
    ffmpeg
    .input('pipe:',format='rawvideo',pix_fmt='rgb24',s=str(frames.shape[1]) + 'x' + str(frames.shape[0]),r=str(frame_rate))
    .output(file_name,vcodec='ffv1',an=None)
    .overwrite_output()
    .run_async(pipe_stdin=True)
)



for frame_num in range(frames.shape[3]):
    
    frame= frames[:,:,:,frame_num]
    
    ff_proc.stdin.write(frame.tobytes())
    

ff_proc.stdin.close()


out, _ = (
    ffmpeg
    .input('out.avi')
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)


video =np.frombuffer(out, np.uint8).reshape([-1, 100, 200, 3])

video = np.transpose(video, (1, 2, 3, 0))





print(np.sum(np.abs(frames - video)))



