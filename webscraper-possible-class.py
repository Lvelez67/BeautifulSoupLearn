import requests
import csv
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.data = []
        # self.product

    def get_type(self, choice):
        if choice == "url":
            url = input("Enter url: ")
            result = requests.get(url)  # Makes a get request for the url to get the html code
            doc = BeautifulSoup(result.text, "html.parser")  # Parses html from the request
            items = doc.find_all(class_="item-cell")
            return items
        elif choice == "file":
            file = input("Enter file directory: ")
            with open(file, "r") as f:
                doc = BeautifulSoup(f, "html.parser")
            items = doc.find_all(class_="item-cell")
            return items
        else:
            print("Incorrect Choice!!")
            newChoice = input("Would you like to insert a html file or url? (choice: file or url):")
            return self.get_type(newChoice)

    def sort_q(self, sort, dictionary):
        sorted_dict = dictionary  # Initialize sorted_dict with the original dictionary

        if sort == "yes":
            sort_type = input("High to low or Low to high prices? (choice: High or Low)")
            if sort_type == "High":
                sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0], reverse=True))
            elif sort_type == "Low":
                sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
            else:
                print("Incorrect choice!!")
                newSort = input("Would you like to sort the prices? (choice: yes or no)")
                return self.sort_q(newSort, dictionary)
        elif sort == "no":
            return dictionary
        else:
            newSort = input("Would you like to sort the prices? (choice: yes or no)")
            return self.sort_q(newSort, dictionary)
        return sorted_dict

    def w_size(self, size, dictionary):
        if size == "ten":
            limited_products = dict(list(dictionary.items())[:10])
            return limited_products
        elif size == "all":
            return dictionary
        else:
            print("Incorrect choice!!")
            size = input("Would you like to list the first 10 results or all? (choice: ten or all)")
            return self.w_size(size, dictionary)

    def file_type(self, format_, dictionary):
        if format_ == "csv":
            with open('ProductPrices.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in dictionary.items():
                    writer.writerow(value + [key])
        elif format_ == "text":
            with open("ProductPrices.txt", 'w') as f1:
                for key, value in dictionary.items():
                    f1.write('%s:%s\n' % (value, key))
        else:
            print("Incorrect choice!!")
            newFormat_ = input("Would you like the output to be in a text file or csv? (choice: text or csv)")
            return self.file_type(newFormat_, dictionary)

    def main(self):
        choice = input("Would you like to insert a html file or url? (choice: file or url):")
        sort = input("Would you like to sort the prices? (choice: yes or no)")
        size = input("Would you like to list the first 10 results or all? (choice: ten or all)")
        format_ = input("Would you like the output to be in a text file or csv? (choice: text or csv)")

        items = self.get_type(choice)

        products = {}
        num = len(items)

        for item in range(num):
            item_title = items[item].find(class_="item-title").contents[1]
            item_price = items[item].find(class_="price-current").contents[2:4]
            dollar = item_price[0].string
            cents = item_price[1].string
            Total = dollar + cents
            price = Total.replace(",", "")
            atri = items[item].find(class_="item-title").attrs
            link = atri['href']
            Value = [item_title, link]
            products.update({float(price): Value})

        products = self.sort_q(sort, products)
        products = self.w_size(size, products)
        self.file_type(format_, products)

# scraper = WebScraper()
# scraper.main()
# Webscraper before class

# import requests
# import csv
# from bs4 import BeautifulSoup


# def get_type(choice):
#     if choice == "url":
#         url = input("Enter url: ")
#         result = requests.get(url)                              #Makes a get request for the url to get the html code
#         doc = BeautifulSoup(result.text, "html.parser")         #Parses html from the request
#         items = doc.find_all(class_="item-cell")
#         print(type(doc))
#         return items
#     elif choice == "file":
#         file = input("Enter file directory: ")
#         with open(file, "r") as f:
#             doc = BeautifulSoup(f,"html.parser")
#         items = doc.find_all(class_="item-cell")
#         return items
#     else:
#         print("Incorrect Choice!!")
#         newChoice = input("Would you like to insert a html file or url? (choice: file or url):")
#         return get_type(newChoice)


# def sort_q(sort,dictionary):
#     sorted_dict = dictionary  # Initialize sorted_dict with the original dictionary

#     if sort == "yes":
#         sort_type = input("High to low or Low to high prices? (choice: High or Low)")
#         if sort_type == "High":
#             sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0], reverse=True))
#         elif sort_type == "Low":
#             sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
#         else:
#             print("Incorrect choice!!")
#             newSort = input("Would you like to sort the prices? (choice: yes or no)")
#             return sort_q(newSort, dictionary)
#     elif sort == "no":
#         return dictionary
#     else :
#         newSort = input("Would you like to sort the prices? (choice: yes or no)")
#         return sort_q(newSort,dictionary)
#     return sorted_dict


# def w_size(size,dictionary):
#     if size == "ten":
#         limited_products = dict(list(dictionary.items())[:10])
#         return limited_products    
#     elif size == "all":
#         return dictionary
#     else:
#         print("Incorrect choice!!")
#         size = input("Would you like to list the first 10 results or all? (choice: ten or all)")
#         return w_size(size,dictionary)


# def file_type(format_,dictionary):
#     if format_ == "csv":
#         with open('ProductPrices.csv', 'w') as csv_file:  
#             writer = csv.writer(csv_file)
#             for key, value in dictionary.items():
#                 writer.writerow(value + [key])
#     elif format_ == "text":
#         with open("ProductPrices.txt", 'w') as f1: 
# 	        for key, value in dictionary.items(): 
# 		        f1.write('%s:%s\n' % (value, key))
#         #pass
#     else:
#         print("Incorrect choice!!")
#         newFormat_ = input("Would you like the output to be in a text file or csv? (choice: text or csv)")
#         return file_type(newFormat_)


# def main():
#     choice = input("Would you like to insert a html file or url? (choice: file or url):")
#     sort = input("Would you like to sort the prices? (choice: yes or no)")
#     size = input("Would you like to list the first 10 results or all? (choice: ten or all)")
#     format_ = input("Would you like the output to be in a text file or csv? (choice: text or csv)")

#     items = get_type(choice)

#     products = {}
#     num = len(items)

#     for item in range(num) :
#         item_title =items[item].find(class_="item-title").contents[1]
#         item_price =items[item].find(class_="price-current").contents[2:4]
#         dollar = item_price[0].string
#         cents = item_price[1].string
#         Total = dollar+cents
#         price = Total.replace(",","")
#         atri =items[item].find(class_="item-title").attrs
#         link = atri['href']
#         Value = [item_title, link]
#         products.update({float(price):Value})
    
#     products = sort_q(sort,products)
#     products = w_size(size,products)
#     file_type(format_,products)

# main()

# def fileType(format_,data):
#     if format_.lower() == "csv":
#         with open('ProductPrices.csv', 'w') as csv_file:
#             writer = csv.writer(csv_file)
#             for key, value in dictionary.items():
#                 writer.writerow(value + [key])
#     elif format_.lower() == "text":
#         with open("ProductPrices.txt", 'w') as f1:
#             for key, value in dictionary.items():
#                 f1.write('%s:%s\n' % (value, key))
#     else:
#         print("Incorrect choice!!")
#         newFormat_ = input("Would you like the output to be in a text file or csv? (choice: text or csv)")
#         return self.file_type(newFormat_, dictionary)