import requests
from bs4 import BeautifulSoup
import drawsvg as draw

USERNAME = "siby_369" 

def fetch_rating(username):
    url = f"https://www.codechef.com/users/{username}"
    r = requests.get(url)
    if r.status_code != 200:
        return "N/A"

    soup = BeautifulSoup(r.text, "html.parser")
    rating_tag = soup.find("div", class_="rating-number")
    return rating_tag.text.strip() if rating_tag else "N/A"

def generate_svg(rating, username):
    d = draw.Drawing(250, 80, origin="center")

    # Background
    d.append(draw.Rectangle(-125, -40, 250, 80, fill="#1E1E1E", rx=10, ry=10))

    # Text
    d.append(draw.Text(f"CodeChef: {username}", 14, 0, 15, fill="white", center=True))
    d.append(draw.Text(f"Rating: {rating}", 20, 0, -10, fill="#FFD700", center=True))

    d.save_svg("codechef_stats.svg")

def main():
    rating = fetch_rating(USERNAME)
    generate_svg(rating, USERNAME)

if __name__ == "__main__":
    main()
