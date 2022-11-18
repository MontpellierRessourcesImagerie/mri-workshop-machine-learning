cd('E:\Dropbox\Deep_Learning\Formation Deep Learning June 2019\Support formation\Convolutional network')
im = imread('108_Myxo_Ch1.png');

figure(1)
imagesc(im)
axis image
axis off
colormap('Gray')

Filter = [-2 -1 0;-1 0 1;0 1 2];
% Filter = transpose(Filter);
Filtered_im = max(0,conv2(im, Filter, 'same'));
% Filtered_im = filter2(Filter, im);

figure(2)
imagesc(Filtered_im)
axis image
axis off
colormap('Gray')

figure(3)
imagesc(Filter)
axis image
axis off
colormap('Gray')

[lx,ly] = size(Filtered_im);
im_pool = zeros(floor(lx/2), floor(ly/2));

for nx = 1 : 2 : lx
    for ny = 1 : 2 : ly
        I = Filtered_im(nx:nx+1, ny:ny+1);
        im_pool((nx+1)/2,(ny+1)/2) = max(max(I));
    end
end

figure(4)
imagesc(im_pool)
axis image
axis off
colormap('Gray')