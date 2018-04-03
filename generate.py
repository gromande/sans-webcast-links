from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def get_webcasts(year):
    url = "https://www.sans.org/webcasts/archive/" + str(year)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {"class": "table table-bordered table-striped"})

    webcasts = []
    for row in table.find_all('tr'):
        title_content = row.find('td', {"class": "table_data table_data_title"})

        if title_content is None:
            continue

        title_anchor = title_content.find('a')
        title_link = title_anchor.get("href")
        title = title_anchor.string

        date = row.find('td', {"class": "table_data table_data_date"})
        sponsor = row.find('td', {"class": "table_data table_data_sponsor"})
        speaker = row.find('td', {"class": "table_data table_data_speaker"})

        webcast = {"title": title, "date": date.string, "sponsor": sponsor.string,
                   "speaker": speaker.string}
        webcasts.append(webcast)

    return webcasts

result = {}
for year in range(2013, 2019):
    webcasts = get_webcasts(year)
    result[str(year)] = webcasts

print(json.dumps(result))
