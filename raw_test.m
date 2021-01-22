clc;clear all;close all;
%%% is not totaly fine - some unnececery CT info save


shape = [2,3,4,5];
% shape = [2,3,4];

A = uint16(reshape(1:prod(shape),shape));
fname = 'test5';


save_raw(A,fname)





[B,info] = load_raw([fname '.mhd']);






tmp = A~=B;
sum(tmp(:))