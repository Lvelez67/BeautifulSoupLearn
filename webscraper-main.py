import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
import logging
import csv

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_total_pages(doc):
    try:
        page_text = doc.find(class_="list-tool-pagination-text").strong
        return int(str(page_text).split("/")[-2].split(">")[-1][:-1])
    except Exception as e:
        logging.error(f"Error getting total pages: {e}")
        return 1

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching page: {e}")
        return None

def parse_items(doc, product):
    item_found = {}
    try:
        div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
        items = div.find_all(string=re.compile(re.escape(product), re.IGNORECASE))
        for item in items:
            parent = item.parent
            if parent.name != "a":
                continue
            link = parent["href"]
            next_parent = item.find_parent(class_="item-container position-relative")
            try:
                price = next_parent.find(class_="price-current").strong.string
                item_found[item] = {"price": int(price.replace(",", "")), "link": link}
            except Exception as e:
                logging.error(f"Error parsing item: {e}")
                print("This is normal!!!")
    except Exception as e:
        logging.error(f"Error parsing items: {e}")
    return item_found

def sChoice(all_items):
        sortChoice = input("Would you like to sort the results? (Yes or No)").strip().lower()
        if sortChoice == "no":
            newDict = dict(all_items)
            return newDict
        elif sortChoice == "yes":
            howSort = input("How would you like to sort? (Lowest or Highest) ").strip().lower()
            if howSort == "lowest":
                sorted_itemsLH = dict(sorted(all_items.items(), key=lambda x: x[1]["price"], reverse=False))
                return sorted_itemsLH
            elif howSort == "highest":
                sorted_itemsHL = dict(sorted(all_items.items(), key=lambda x: x[1]["price"], reverse=True))
                return sorted_itemsHL
            else:
                print("Please enter Lowest or Highest. ")
                return sChoice(all_items)
        else:
            print("Please enter Yes or No. ")
            return sChoice(all_items)


def write_to_file(choice):
    file_type = input("Would you like to save the data as a CSV or a text file? (Enter 'csv' or 'text'): ").strip().lower()
    
    if file_type == 'csv':
        filename = input("Enter the filename (without extension) for the CSV file: ") + ".csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Item", "Price", "Link"])  # Writing the header
                for item, details in choice.items():
                    writer.writerow([item, details["price"], details["link"]])
            print(f"Data successfully written to {filename}")
        except Exception as e:
            logging.error(f"Error writing to CSV: {e}")
    
    elif file_type == 'text':
        filename = input("Enter the filename (without extension) for the text file: ") + ".txt"
        try:
            with open(filename, mode='w', encoding='utf-8') as file:
                file.write("Item\tPrice\tLink\n")  # Writing the header
                for item, details in choice.items():
                    file.write(f"{item}\t{details['price']}\t{details['link']}\n")
            print(f"Data successfully written to {filename}")
        except Exception as e:
            logging.error(f"Error writing to text file: {e}")
    
    else:
        print("Invalid choice. Please enter 'csv' or 'text'.")
        write_to_file(choice)  # Retry if the input is invalid

def w_size(dictionary):
        size = input("Would you like to list the first 10 results or all? (choice: ten or all)").strip().lower()
        if size == "ten":
            limited_products = dict(list(dictionary.items())[:10])
            return limited_products
        elif size == "all":
            return dictionary
        else:
            print("Incorrect choice!!")
            return w_size(dictionary)

def main():
    product = input("What product would you like to search for? ")
    formatted_product = urllib.parse.quote_plus(product)
    url = f"https://www.newegg.com/p/pl?d={formatted_product}&N=4131"

    page_content = fetch_page(url)
    if not page_content:
        return

    doc = BeautifulSoup(page_content, "html.parser")
    pages = get_total_pages(doc)

    all_items = {}
    for page in range(1, pages + 1):
        url = f"https://www.newegg.com/p/pl?N=4131&d={formatted_product}&page={page}"
        page_content = fetch_page(url)
        if not page_content:
            continue
        doc = BeautifulSoup(page_content, "html.parser")
        items = parse_items(doc, product)
        all_items.update(items)


    choice = sChoice(all_items)
    sizeDict = w_size(choice)
    write_to_file(sizeDict)


if __name__ == "__main__":
    main()

#Possible terminal output
# for item in choice:
#     print(item[0])
#     print(f"${item[1]['price']}")
#     print(item[1]['link'])
#     print("-----------------------------------------------------")


# from webscraper-possible-class import WebScraper

# product = input("What product would you like to serarch for? ")

# url = f"https://www.newegg.com/p/pl?d={product.replace(" ", "+")}&N=4131"

# scraper = WebScraper(product)
# scraper.main()
 
# import requests
# from bs4 import BeautifulSoup
# import re
# import urllib.parse

# product = input("What product would you like to search for? ")

# formatted_product = urllib.parse.quote_plus(product)

# url = f"https://www.newegg.com/p/pl?d={formatted_product}&N=4131"

# page = requests.get(url).text                              #Makes a get request for the url to get the html code
# doc = BeautifulSoup(page, "html.parser")                   #Parses html from the request

# page_text = doc.find(class_="list-tool-pagination-text").strong
# pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

# item_found = {}

# for page in range(1, pages + 1):
#     url = f"https://www.newegg.com/p/pl?N=4131&d={formatted_product}&page={page}"
#     page = requests.get(url).text
#     doc = BeautifulSoup(page, "html.parser")
    
#     div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
#     items = div.find_all(string= re.compile(re.escape(product), re.IGNORECASE))

#     for item in items:
#         parent =item.parent
#         if parent.name != "a":
#             continue
#         link = parent["href"]
#         next_parent = item.find_parent(class_="item-container position-relative")
#         try:
#             price = next_parent.find(class_="price-current").strong.string
#             item_found[item] = {"price":int(price.replace(",","")),"link":link}
#         except:
#             pass

# sorted_items = sorted(item_found.items(), key = lambda x: x[1]["price"], reverse=True)

# for item in sorted_items:
#     print(item[0])
#     print(f"${item[1]["price"]}")
#     print(item[1]['link'])
#     print("-----------------------------------------------------")
