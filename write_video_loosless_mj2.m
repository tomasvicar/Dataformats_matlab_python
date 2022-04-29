clc; clear all; close all; 


frames = uint8(rand(100,200,3,50)*255);
file_name = 'out2.mj2';

v = VideoWriter(file_name,'Archival');

open(v)
for frame_num = 1:size(frames,4)
    frame = frames(:,:,:,frame_num);
    writeVideo(v,frame);
end
close(v)






vidObj = VideoReader(file_name);

video_num_frames = vidObj.NumFrames;

video_data = zeros(vidObj.Height,vidObj.Width, 3, video_num_frames, 'uint8');

frame_ind = 0;
while hasFrame(vidObj)
    frame_ind = frame_ind + 1;
    frame = readFrame(vidObj);
    video_data(:,:,:,frame_ind) = frame;
end


disp(sum(abs(frames - video_data),'all'))



