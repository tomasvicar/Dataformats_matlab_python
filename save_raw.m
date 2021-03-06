function save_raw(Data,Name)



% Data = (squeeze((Data)));
vel = size(Data);

%%%%%% ZMENIT FORMAT
I = uint16(zeros(vel));
%%%%%%%%%%%%%%%%%%%%%%%%

I(:) = Data.*(2^0);
% I(:) = Data.*(2^16);



I = permute(I,[2,1,3:length(vel)]);
vel_tmp = vel;
vel(2) = vel_tmp(1);
vel(1) = vel_tmp(2);

%%%%%% ZMENIT parametry
mhd = cell(13,1);
mhd{1} = 'ObjectType = Image';
mhd{2} = ['NDims = ' num2str(length(vel))];
mhd{3} = 'BinaryData = True';
mhd{4} = 'BinaryDataByteOrderMSB = False';
mhd{5} = 'CompressedData = False';
mhd{6} = 'TransformMatrix = 1 0 0 0 1 0 0 0 1';
mhd{7} = 'Offset = 0 0 0';
mhd{8} = 'CenterOfRotation = 0 0 0';
% mhd{9} = 'AnatomicalOrientation = RAI';
s = num2str([0.1,0.1,0.1]);
% s = num2str([Info.resolution]);
mhd{10} = ['ElementSpacing = ' s];

mhd{12} = 'ElementType = MET_USHORT';  % uint16
% mhd{12} = 'ElementType = MET_UCHAR';  % uint8
% mhd{12} = 'ElementType = MET_UINT';  % uint32
% mhd{12} = 'ElementType = MET_FLOAT';  % single
% mhd{12} = 'ElementType = MET_DOUBLE';  % double

s = num2str(vel);
mhd{11} = ['DimSize = ' s];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%

mhd{13} = ['ElementDataFile = ' Name '.raw'];

fid=fopen([Name '.raw'],'w+');
fwrite(fid,I,'uint16');
fclose(fid);

fid=fopen([Name '.mhd'],'w+');
    for ii = 1:13
        fprintf(fid,'%s\n',mhd{ii,:});
    end
fclose(fid);