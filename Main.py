from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Create FastAPI application
app = FastAPI()

# Get Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Check credentials
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is missing in .env file")

# Connect Python to Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# Test API
@app.get("/")
def home():
    return {"message": "FastAPI connected successfully to Supabase!"}