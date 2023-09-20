import logging
import os

os.makedirs("logs", exist_ok=True)
handler = logging.FileHandler(filename="logs/test.log", encoding="utf-8")
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logging.basicConfig(level=logging.DEBUG, handlers=[handler])
