import requests
import os
from bs4 import BeautifulSoup


def main():
    login_url = "https://www.hackerrank.com/login"
    dest_url = "https://www.hackerrank.com/domains/cpp"
    HACK_RANK_PASSWORD = os.environ["HACK_RANK_PASSWORD"]
    params = {
        "login": "yangdai713@aim.com",
        "password": HACK_RANK_PASSWORD
    }

    with requests.Session() as s:
        p = s.post(login_url, params)
        if p.ok:
            print("You have successfully logged in.")
        else:
            print("login failed.")

        r = s.get(dest_url)
        bs = BeautifulSoup(r.text, 'html.parser')
        challenges = bs.find(class_='challenges-list').find_all('h4')
        for challenge in challenges:
            print(challenge.get_text())



if __name__ == '__main__':
    main()
