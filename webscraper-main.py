from webscraper import WebScraper

# product = input("What product would you like to serarch for? ")

# url = f"https://www.newegg.com/p/pl?d={product.replace(" ", "+")}&N=4131"

scraper = WebScraper(product)
scraper.main()
 