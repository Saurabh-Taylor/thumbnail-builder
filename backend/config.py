import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "test")
IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")

print(OPENAI_API_KEY)
print(IMAGEKIT_PRIVATE_KEY)

DATABASE_URL = "sqlite:///./thumbnailbuilder.db" 

# print(OPENAI_API_KEY)
