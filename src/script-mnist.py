import subprocess
import os
import pathlib
import argparse
import shutil
import random
import uuid

from glob import glob

import numpy as np
import cv2

def blur(n_kernel, input_path, output_path):
    files = glob(f'{input_path}/**/*.jpg', recursive=True)
    
    for file in files:
        img = cv2.imread(file)
        kernel = np.ones((n_kernel,n_kernel),np.float32)/25
        dst = cv2.filter2D(img,-1,kernel)
        
        file_name = os.path.basename(file)
        dir_name = os.path.dirname(file)
        parent_dir_name = os.path.basename(dir_name)

        print(f'{output_path}/{parent_dir_name}/{file_name}')

        if not os.path.exists(f'{output_path}/{parent_dir_name}'):
            os.makedirs(f'{output_path}/{parent_dir_name}')
        
        cv2.imwrite(f'{output_path}/{parent_dir_name}/{file_name}', dst)
    print('number of processing files: %i' % len(files))
    
    
def main(n_kernel):
    input_path = '/opt/ml/processing/input' #fixed input path
    output_path = f'/opt/ml/processing/output' #fixed output path

    blur(n_kernel, input_path, output_path)

    print('Gaussian blur complete.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tiling images.')
#     parser.add_argument('n_images', type=int, help='kernerl of gaussian')
    parser.add_argument('n_kernel', type=int, help='kernerl of gaussian')
    args = parser.parse_args()

    main(args.n_kernel)
