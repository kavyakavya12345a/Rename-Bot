import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "28200856"))
API_HASH = os.environ.get("API_HASH", "30e0567e3c97b0ea8e8d3fe50b2c2442")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7685215647:AAHbMjUXvVgnu-SM3A4H-sQQgkzMbKAjih4")
ADMIN = int(os.environ.get("ADMIN", "7154442141"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002413483136")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002174507683"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nowkavya:SQhrAFthqs0mZLBT@cluster0.9e8dz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "nowkavya")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
