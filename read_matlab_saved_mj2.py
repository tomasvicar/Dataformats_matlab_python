
import numpy as np
import ffmpeg


# FFmpeg must be installed and accessible via the $PATH environment variable.
# https://ffmpeg.org/download.html#build-windows
# download folder and add this folder to path https://windowsloop.com/install-ffmpeg-windows-10/
 


out, _ = (
    ffmpeg
    .input('out2.mj2')
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)


video =np.frombuffer(out, np.uint8).reshape([-1, 100, 200, 3])

video = np.transpose(video, (1, 2, 3, 0))






