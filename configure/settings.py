from pathlib import Path
import os

BASE_PATH = Path(__file__).resolve().parent.parent

DEBUG = True
SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'

FILE_UPLOAD_BASE_PATH = os.path.join(BASE_PATH, 'app/files')
