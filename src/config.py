import os

from dotenv import load_dotenv

load_dotenv()


SB_URL: str | None = os.getenv("SUPABASE_URL")
SB_KEY: str | None = os.getenv("SUPABASE_KEY")


TIMEZONE = "Europe/Berlin"
SCAN_TIME = "03:00"

if SB_URL is None or SB_KEY is None:
    raise ValueError("SB_URL and SB_KEY environment variables must be set!")
