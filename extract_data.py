import os
import glob
import random
import shutil
import tarfile
import tarfile
import zipfile
import cv2
import imgaug.augmenters as iaa
from pathlib import Path
import multiprocessing
from imgaug.augmenters import debug
from tqdm import tqdm


def extract_dataset(raw_dataset_folder, output_folder):
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Extract
    for tar_path in tqdm(os.listdir(raw_dataset_folder), desc="Extracting dataset"):
        if tar_path.endswith(".tar.gz") or tar_path.endswith(".tar.xz"):
            my_tar = tarfile.open(os.path.join(raw_dataset_folder, tar_path))
            try:
                my_tar.extractall(output_folder)
            except Exception as e:
                print(e)
                print(tar_path)
                my_tar.close()
                continue
        elif tar_path.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(raw_dataset_folder, tar_path), "r") as zip_ref:
                zip_ref.extractall(output_folder)

    my_tar.close()


def main(args):
    extract_dataset(
        args.raw_path,
        args.output_path
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extract data')

    parser.add_argument('--raw_path', type=str, required=True,
                        help='Path to raw card dataset')
    parser.add_argument('--output_path', type=int, required=True,
                        help='Path to raw card dataset')

    args  = parser.parse_args()
    main(args)