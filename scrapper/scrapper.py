import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def search_incruit(keyword, pages=1):

    jobs = []

    for page in range(pages):

        page = page * 30

        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")

        lis = soup.find_all("li", class_="c_col")

        for li in lis:
            try:
                company = li.find("a", class_="cpname").text.strip()
                title_tag = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a")
                title = title_tag.text.strip()
                location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
                link = title_tag.get("href")
            except AttributeError:
                # 광고 등 구조가 다른 항목은 건너뜀
                continue

            job_data = {
                "site": "인크루트",
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }
            jobs.append(job_data)

    return jobs


def search_saramin(keyword, pages=1):

    jobs = []

    for page in range(1, pages + 1):

        url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}&recruitPage={page}"
        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.find_all("div", class_="item_recruit")

        for item in items:
            try:
                title_tag = item.find("h2", class_="job_tit").find("a")
                title = title_tag.get("title")
                link = "https://www.saramin.co.kr" + title_tag.get("href")
                company = item.find("strong", class_="corp_name").find("a").text.strip()
                location = item.find("div", class_="job_condition").find_all("span")[0].text
                location = " ".join(location.split())   # 공백/줄바꿈 정리 ("서울  강남구" -> "서울 강남구")
            except AttributeError:
                continue

            job_data = {
                "site": "사람인",
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }
            jobs.append(job_data)

    return jobs


def search_all(keyword, pages=1):

    jobs = []
    
    try:
        jobs += search_incruit(keyword, pages)
    except Exception as e:
        print("인크루트 크롤링 실패 :", e)

    try:
        jobs += search_saramin(keyword, pages)
    except Exception as e:
        print("사람인 크롤링 실패 :", e)

    return jobs


if __name__ == "__main__":
    result = search_all("python", 1)
    print("총", len(result), "건")
    for job in result[:5]:
        print(job)
