import requests
from bs4 import BeautifulSoup

def run_scout():
    print("--- [SCOUT STARTING: SEARCHING FOR JOBS] ---")
    
    # The URL we are scouting
    url = "https://realpython.github.io/fake-jobs/"
    
    # 1. Download the page
    response = requests.get(url)
    
    # 2. Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 3. Find all job cards (This depends on the website's structure)
    job_elements = soup.find_all("div", class_="card-content")
    
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        description_link = job.find_all("a")[1]["href"] # The link to the full details
        
        print(f"Found: {title} at {company}")
        print(f"Details at: {description_link}\n")

if __name__ == "__main__":
    run_scout()