import os
import winreg
from pathlib import Path
import sys
from aligo import Aligo


def main(file_path):
    ali = Aligo(refresh_token=refresh_token)
    ali.upload_folder(refresh_token, file_path)


if __name__ == '__main__':
    refresh_token=sys.argv[1]
    file_path = sys.argv[2]
    main(refresh_token, file_path)
