import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrap_linkedin_profile(linkedin_profile_url:str,mock:bool=False):
    """scrape information from the linkedin profiles,
    Manually scrape the information from the linkedin profile"""