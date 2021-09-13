import glob
import os
import shutil

from tqdm import tqdm


def extract_valid(card_type, is_front):
    output_folder_path = os.path.join(output_path, "{}_valid_{}".format(card_type, is_front))
    os.makedirs(output_folder_path, exist_ok=True)
    front_or_back = "front" if is_front else "back"

    for root, _, files in tqdm(os.walk(os.path.join(raw_path)), desc="Extracting {} valid {}".format(card_type, is_front)):
        for f in files:
            image_path = os.path.join(root, f)
            if image_path.find("invalid") < 0 and image_path.find("valid") >= 0 and image_path.find(card_type) >= 0 and image_path.find(front_or_back) >= 0:
                shutil.move(image_path, output_folder_path)


def extract():
    for root, dir, files in tqdm(os.walk(raw_path)):
        for f in files:
            image_path = os.path.join(root, f)
            parrent_path = image_path.split('/')[-2]
            
            if parrent_path.find('invalid') >= 0:
                valid = 'invalid'
            elif parrent_path.find('valid') >= 0:
                valid = 'valid'
            else:
                valid = 'confuse'
            
            if parrent_path.find('cmnd') >= 0 or parrent_path.find('CMND') >= 0:
                card_type = 'CMND'
            elif parrent_path.find('chip') >= 0:
                card_type = 'CHIP'
            elif parrent_path.find('cccd') >= 0 or parrent_path.find('CCCD') >= 0:
                card_type = 'CCCD'
            else:
                card_type = 'unknown'
            
            if parrent_path.find('back') >= 0:
                card_face = 'back'
            elif parrent_path.find('front'):
                card_face = 'front'
            else:
                card_face = 'unknown'

            out_path = os.path.join(output_path, card_type, '{}_{}'.format(valid, card_face))
            os.makedirs(out_path, exist_ok=True)
            shutil.move(image_path, out_path)
                
    

def main(args):
    global raw_path
    raw_path = args.raw_path

    global output_path
    output_path = args.output_path

    # os.makedirs(output_path, exist_ok=True)

    extract()

    # extract_valid(
    #     args.card_type,
    #     args.card_face
    # )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extract data')

    parser.add_argument('--raw_path', type=str, required=True,
                        help='Path to raw card dataset')
    parser.add_argument('--output_path', type=str, required=True,
                        help='Path to raw card dataset')
    # parser.add_argument('--card_type', type=int, required=True,
    #                     help='Path to raw card dataset')
    # parser.add_argument('--card_face', type=int, required=True,
                        # help='Path to raw card dataset')

    args  = parser.parse_args()
    main(args)
