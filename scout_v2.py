#this is a updated new version of scout ,, as this is a deep scout which will find a single job with specific skills we have
import requests
from bs4 import BeautifulSoup
from bridge_v1 import bridge_process # Importing the brain from Day 3
import time

def deep_scout(job_url):
    print(f"--- [DEEP SCOUT: ANALYZING {job_url}] ---")
    
    # 1. Visit the specific job page
    response = requests.get(job_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 2. Extract all text from the page (simplest way for AI to read)
    # We strip out script and style tags so the AI doesn't get confused by code
    for script in soup(["script", "style"]):
        script.extract()
    
    full_text = soup.get_text(separator=' ')
    
    # 3. Feed this giant wall of text to our Bridge (Day 3)
    # The Bridge will use the Librarian to find the skills
    bridge_process(full_text)

def run_scout_and_learn():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all job cards
    job_elements = soup.find_all("div", class_="card-content")
    
    # We only take the FIRST job to test (to avoid spamming the local brain)
    first_job = job_elements[0]
    details_link = first_job.find_all("a")[1]["href"]
    
    print(f"Found a target job! Diving into: {details_link}")
    
    # CALL THE DEEP DIVE
    deep_scout(details_link)

if __name__ == "__main__":
    run_scout_and_learn()