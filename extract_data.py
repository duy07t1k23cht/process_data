import glob
import os
import random
import shutil
import tarfile
import zipfile

import patoolib
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
        elif tar_path.endswith(".rar"):
            patoolib.extract_archive(tar_path, outdir=output_folder)

    my_tar.close()


def extract_file(compressed_file_path, output_folder):
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Extract
    if compressed_file_path.endswith(".tar.gz") or compressed_file_path.endswith(".tar.xz"):
        my_tar = tarfile.open(compressed_file_path)
        try:
            my_tar.extractall(output_folder)
        except Exception as e:
            print(e)
            print(compressed_file_path)
            my_tar.close()
    elif compressed_file_path.endswith(".zip"):
        with zipfile.ZipFile(compressed_file_path, "r") as zip_ref:
            zip_ref.extractall(output_folder)
    elif compressed_file_path.endswith(".rar"):
        patoolib.extract_archive(compressed_file_path, outdir=output_folder)

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
    parser.add_argument('--output_path', type=str, required=True,
                        help='Path to raw card dataset')

    args  = parser.parse_args()
    main(args)
