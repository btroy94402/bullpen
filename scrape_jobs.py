### Written by Brian Troy July 7, 2021 (bitroy@yahoo.com)

def extract(page, my_url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url=f"{my_url}{page}"
    r =  requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
	
def transform(soup):
    divs = soup.find_all('div',class_ = 'job_seen_beacon')
    for item in divs:   
        spans = item.find('h2').find_all('span') #Sometimes there are multiple spans.  Sometimes the title is span[0], and sometimes span[1]
        if len(spans) == 1:
            title = spans[0].text
        elif len(spans)  == 2:
            title =  spans[1].text
        company = item.find('span', class_ = 'companyName').text.strip()
        location = item.find('div', class_ = "companyLocation").text.strip()
        posted = item.find('span', class_ = "date").text.strip().replace("Active ", "").replace("+ ","").replace("days ago","").replace("day ago","").replace("Today","0").replace("Just posted", "0").replace("today","0")
        try:
            salary = item.find('span', class_ = 'salary-snippet').text.strip()
        except:
            salary = 'not available'
        summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n',' ')
        job = {
            'title': title,
            'company': company,
            'location': location,
            'days_posted': posted,
            'salary': salary,
            'summary': summary}      
        joblist.append(job)
    return
	
if __name__ == "__main__":

	import requests
	from bs4 import BeautifulSoup
	import pandas as pd
	from datetime import date

	url_data_engineer = 'https://www.indeed.com/jobs?q=data%20engineer&l=san%20mateo%2C%20ca&start='
	url_data_science = 'https://www.indeed.com/jobs?q=data%20scientist&l=San%20Mateo%2C%20CA&start='
	url_data_wafer = 'https://www.indeed.com/jobs?q=data%20wafer&l=san%20mateo%2C%20ca&start='
	url_python_vba = 'https://www.indeed.com/jobs?q=Python%20Vba&l=San%20Mateo%2C%20CA&start='

	urls = []
	urls.append(url_data_engineer)
	urls.append(url_data_science)
	urls.append(url_data_wafer)
	urls.append(url_python_vba)

	names=["data_engineer_jobs_","data_science_jobs_","data_wafer_jobs_","python_vba_jobs_"]

	for j in range(len(urls)):
		joblist = []
		for i in range(13):
			print(f"Getting Page: {i}")
			c = extract(i,urls[j])
			transform(c)
		df = pd.DataFrame(joblist)

		df.to_csv(f'C:\\Users\\bitro\\Desktop\\web_scrape_jobs\\Job_Listings\\{names[j]}{date.today()}.csv',index=False)
		print('Done')