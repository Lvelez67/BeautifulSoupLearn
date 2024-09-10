# import requests
# import csv
# from bs4 import BeautifulSoup

# url = "https://www.newegg.com/zotac-trinity-zt-d40820q-10p-nvidia-geforce-rtx-4080-super-16gb-gddr6x/p/N82E16814500581"

# result = requests.get(url)                              #Makes a get request for the url to get the html code
# doc = BeautifulSoup(result.text, "html.parser")         #Parses html from the request

# prices = doc.find_all(string="$")                       #finds all of a specific string  output =>['$', '$', '$', '$']
# parent = prices[1].parent                               #finds the parent tag of the string[1] found output => <li class="price-current"><span class="price-current-label"></span>$<strong>1,069</strong><sup>.97</sup></li>
# strong = parent.find("strong")                          #finds strong tag. This contains the dollar amount
# sup = parent.find("sup")                                #finds sup tag. This contains the cent amount
# dollar = strong.string                                  #takes the string contained in the strong tag
# cents = sup.string                                      #takes the string contained in the sup tag

# Total = dollar+cents

# print(Total)                                            #=> Total 1069.97


###############################################################################################################################
################################################ Copies html from url to file #################################################
###############################################################################################################################

# url = "https://www.newegg.com/zotac-trinity-zt-d40820q-10p-nvidia-geforce-rtx-4080-super-16gb-gddr6x/p/N82E16814500581"

# result = requests.get(url)                              #Makes a get request for the url to get the html code
# doc = BeautifulSoup(result.text, "html.parser")

# with open("cpurlhtml.html", "w") as file:
#     file.write(str(doc))

# 

# url = "https://www.newegg.com/p/pl?d=apple+watch&N=4131"

# result = requests.get(url)                              #Makes a get request for the url to get the html code
# doc = BeautifulSoup(result.text, "html.parser")

# with open("cpurlhtml.html", "r") as f:
#     doc = BeautifulSoup(f,"html.parser")

# items = doc.find_all(class_="item-cell")
# num = len(items)
# products = {}

# for item in range(num) :
#     item_title =items[item].find(class_="item-title").contents[1]
#     item_price =items[item].find(class_="price-current").contents[2:4]
#     dollar = item_price[0].string
#     cents = item_price[1].string
#     Total = dollar+cents
#     atri =items[item].find(class_="item-title").attrs
#     link = atri['href']
#     Value = [Total, link]
#     products.update({item_title:Value})

# #Write to csv
# with open('ProductPrices.csv', 'w') as csv_file:  
#     writer = csv.writer(csv_file)
#     for key, value in products.items():
#        writer.writerow([key]+ value)

#Find way to add href -done
#sort dictionary from lowest value to highest (make total into float and set it as the key then sort dict by key) -done
#Add custom search from video and multi page checking
#Add top 10

# What product would you like to search?
# ----
# Would like to see the top 10 cheapest or all products from Low to High?
# ----
# -Top 10 cheapest: show the top 10 with links in cli then ask if they want to write to a csv or txt.
# -All: ask if they want it as a csv or txt file

#Write to txt
# with open("ProductPrices.txt", 'w') as f1: 
# 	for key, value in products.items(): 
# 		f1.write('%s:%s\n' % (key, value))


# item_title =items[0].find(class_="item-title").contents[1]
# # title = item_title.contents[1]
# item_price =items[0].find(class_="price-current").contents[2:4]
# dollar = item_price[0].string
# cents = item_price[1].string
# Total = dollar+cents
# print(Total)
# print()


#class= price-current, item-title (contains href)
