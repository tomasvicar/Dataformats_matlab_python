clc;clear all;close all force;
addpath('bfmatlab')


shape = [2,3,4,5,6];
% shape = [2,3,4,5];
% shape = [2,3,4];


A = reshape(1:prod(shape),shape);


fname = 'test.tif';


bfsave_volume_XYCZT(fname,A)



B = ReadImage6D(fname);
B = B{1};
B = squeeze(B(1,:,:,:,:,:));
B = permute(B,[4,5,3,2,1]);



size(B)

tmp = B~=A;
sum(tmp(:))




fname = 'G:\Sdílené disky\martin_data\NHDF\NHDF_8h PI\IR 0,5Gy_8h PI\rawdata\0003\01.ics';
B = ReadImage6D(fname);


