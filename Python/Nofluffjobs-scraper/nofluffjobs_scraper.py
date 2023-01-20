from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
           'Accept':
               'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

nofluffjob = "https://nofluffjobs.com"


def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)

    return (res)

def create_csv(link, comp, lin):
    try:
        pageTree = requests.get(
            f"{nofluffjob}{link}",
            headers=headers)
        soup = BeautifulSoup(pageTree.content, 'html.parser')
        soup = soup.find("section")
        links = soup.find_all("a", {"class": "col-sm-6 col-lg-4 mb-4"})
        next_page = soup.find("a", {"aria-label": "Next"})
        companies = soup.find_all("h3", {"class": "mb-0 text-truncate"})
        companies_list = []
        links_list = []
        if comp is not None and lin is not None:
            companies_list.extend(comp)
            links_list.extend(lin)

        for company in companies:
            print(company.get_text())
            companies_list.append(company.get_text())
        for link in links:
            print(link['href'])
            link = f"{nofluffjob}" + link['href']
            print(link)
            links_list.append(link)
        if soup.find("a", {"aria-label": "Next"}) is not None:
            print("cos")
            print(soup.find("a", {"aria-label": "Next"}))
            create_csv(next_page['href'],companies_list,links_list)
        else:
            companies_list=extractDigits(companies_list)
            links_list = extractDigits(links_list)
            for idx, ele in enumerate(companies_list):
                new_vals = []

                for ele in links_list[idx]:
                    new_vals.append(ele)

                companies_list[idx].extend(new_vals)
            with open('GFG', 'w') as f:

                fields = ['Company', 'Link']
                write = csv.writer(f)
                write.writerow(fields)
                write.writerows(companies_list)

    except Exception as e:
        print("Could not save: ")
        print(e)
    print("Action complete!")


if __name__ == "__main__":
    create_csv("/pl/companies/poznan?withOffersOnly=false&page=1",None,None)
