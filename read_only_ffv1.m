clc;clear all;close all;
%% codec pack required https://codecguide.com/download_kl.htm


file_name = 'out.avi';

vidObj = VideoReader(file_name);

video_num_frames = vidObj.NumFrames;

video_data = zeros(vidObj.Height,vidObj.Width,3,video_num_frames, 'uint8');


frame_ind = 0;
while hasFrame(vidObj)
    frame_ind = frame_ind + 1;
    frame = readFrame(vidObj);
    video_data(:,:,:,frame_ind) = frame;
end





