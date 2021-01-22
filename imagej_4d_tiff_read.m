clc;clear all;close all force;
addpath('bfmatlab')
addpath('../Fiji.app/scripts')%%% path to fiji folder


% shape = [2,3,4,5,6];
shape = [2,3,4,5];
% shape = [2,3,4];

A = reshape(1:prod(shape),shape);
fname = 'test2.tif';



ImageJ


imp = copytoImagePlus(A,'XYCZT');


ij.IJ.saveAsTiff(imp,fname);

imp = ij.IJ.openImage(fname);
imp.show()
IJM.getDatasetAs('B');












