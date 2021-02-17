
clc;clear all;close all;




h5create('myfile3.h5','/DS1',[512 512,Inf],'ChunkSize',[512 512 1],'Datatype','single','Deflate',9)


tic
for k =1:100
    mydata = single(randn(512,512,1));
    h5write('myfile3.h5', '/DS1',mydata,[1,1,k],[512 512 1])

end
toc

h5disp('myfile3.h5')
% 

tic
for k =1:100

    mydata = h5read('myfile3.h5', '/DS1',[1,1,k],[512 512 1]);
    drawnow;
end

toc

