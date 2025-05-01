import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

base_url = "https://www.metacritic.com/browse/game/xbox-series-x/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2025&platform=xbox-series-x&page="

games_data = []

for page in range(0, 2):  
    url = base_url + str(page)
    print(f"Scraping page {page}...")

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("div", class_="c-finderProductCard")
    if not cards:
        print(f"No product cards found on page {page}")
        continue

    for card in cards:
        try:
            rank_text = card.find("h3", class_="c-finderProductCard_titleHeading").find_all("span")[0].text.strip()
            rank = rank_text.replace('.', '')  # remove the fullstop
        except:
            rank = None
        try:
            title = card.find("h3", class_="c-finderProductCard_titleHeading").find_all("span")[1].text.strip()
        except:
            title = None
        try:
            release_date = card.find("div", class_="c-finderProductCard_meta").find_all("span")[0].text.strip()
        except:
            release_date = None
        try:
            rating = card.find("div", class_="c-finderProductCard_meta").find_all("span")[2].text.strip()
        except:
            rating = None
        try:
            description = card.find("div", class_="c-finderProductCard_description").text.strip()
        except:
            description = None
        try:
            score = card.find("div", class_="c-finderProductCard_metascoreValue").find("span").text.strip()
        except:
            score = None
        try:
            relative_link = card.find("a", class_="c-finderProductCard_container")["href"]
            full_link = "https://www.metacritic.com" + relative_link
        except:
            full_link = None
        try:
            images_container = card.find("div", class_="c-finderProductCard_images")
            left_container = images_container.find("div", class_="c-finderProductCard_leftContainer")
            img_container = left_container.find("div", class_="c-finderProductCard_imgContainer")
            blurry_container = img_container.find("div", class_="c-finderProductCard_blurry")
            picture_tag = blurry_container.find("picture")
            img_tag = picture_tag.find("img")
            raw_img_url = img_tag["src"]
            img_url = raw_img_url.replace("&amp;", "&")
        except:
            img_url = None

        games_data.append({
            "Rank": rank,
            "Title": title,
            "Release Date": release_date,
            "Rating": rating,
            "Score": score,
            "Description": description,
            "Link": full_link,
            "Image URL": img_url
        })

    time.sleep(random.uniform(2, 4))

# Build final dataframe
df = pd.DataFrame(games_data)
print(df)

# Save to CSV
df.to_csv("metacritic_games_xbox.csv", index=False)