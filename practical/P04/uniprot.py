import requests
from scrapy.http import TextResponse

def getOrganism(upid):

    url = 'https://www.uniprot.org/uniprot/'+upid

    res = requests.get(url)

    statuscode = res.status_code

    while statuscode != 200:
        res = 0
    try:
        res = requests.get(url)
    except (
        requests.ConnectionError,
        requests.exceptions.ReadTimeout,
        requests.exceptions.Timeout,
        requests.exceptions.ConnectTimeout,
    ) as e:
        statuscode = 0
        print(e)
    if res:
        statuscode = res.status_code

    response = TextResponse(res.url, body=res.text, encoding='utf-8')

    organism = response.css('#content-organism > em::text').extract_first()

    return organism
