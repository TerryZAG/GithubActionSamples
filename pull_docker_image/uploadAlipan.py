import os
import sys
from aligo import Aligo


def main(refresh_token, folder_path):
    ali = Aligo(refresh_token=refresh_token)
    ali.upload_folder(folder_path)


if __name__ == '__main__':
    refresh_token = sys.argv[1]
    folder_path = sys.argv[2]
    print(folder_path)
    main(refresh_token, folder_path)
