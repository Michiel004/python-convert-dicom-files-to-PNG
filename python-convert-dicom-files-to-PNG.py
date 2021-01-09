import numpy as np
import png
import glob
import os
import pydicom

inputdir = './inputFolder'
outdir = './outputFolder'

test_list = [os.path.basename(x) for x in glob.glob(inputdir + '/*.dicom')]
LengtList = len(test_list)
#print(LengtList)
count = 0
for I in test_list:     
    print("Progress" + " " +  str(count/LengtList * 100) + "%")
    ds = pydicom.dcmread(inputdir + "/" + I)

    shape = ds.pixel_array.shape

    # Convert to float to avoid overflow or underflow losses.
    image_2d = ds.pixel_array.astype(float)

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    # Write the PNG file
    Text , Extention = I.split('.')
    with open(outdir + "/" + Text + ".png", 'wb') as png_file:
        w = png.Writer(shape[1], shape[0], greyscale=True)
        w.write(png_file, image_2d_scaled)
    
    count = count + 1