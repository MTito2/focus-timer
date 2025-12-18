import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.config import FIREBASE_PATH

import firebase_admin
from firebase_admin import credentials, firestore

cred_path = FIREBASE_PATH / "firebase_key.json"

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client() 
