 for item, _ in zip_longest(
        soup.find_all(
            "div",
            attrs={"class": "s-result-item", "data-component-type": "s-search-result"},
        ),
        soup.find_all("div", attrs={"class": "a-row a-size-base a-color-base"}),
    ):
        try:
            product_title = item.h2.text
            product_link = "https://www.amazon.in/" + item.h2.a["href"]
            product_price = item.find("span", attrs={"class": "a-offscreen"}).text
            try:
                product_rating = item.find("span", attrs={"class": "a-icon-alt"}).text
            except AttributeError:
                product_rating = "Not available"

#hello
      def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    titles = soup.find_all("td", attrs="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")
    return {
        title.a.text: float(rating.strong.text)
        for title, rating in zip(titles, ratings)
    }
def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    movies = get_imdb_top_250_movies()
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title", "IMDb rating"])
        for title, rating in movies.items():#yes
            writer.writerow([title, rating])
