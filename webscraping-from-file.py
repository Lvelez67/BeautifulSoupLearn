from bs4 import BeautifulSoup
import re

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f,"html.parser")

# print(doc)                         #prints html file parsed by html.parser
# print(doc.prettify())              #prints html file with indentation (Looks Pretty?)

# tag = doc.title                    #sets the title tag equal to tag
# print(tag)                         #prints first title tag only

# print(tag.string)                  #prints out the string inside of title

# tag.string = "hello"               #modifies the string in the file
# print(tag)                          
# print(doc)                         #shows it is actually modified in the doc

# tags = doc.find("a")               #finds the first occurence of the a tag
# print(tags)

# tags = doc.find_all("p")[0]        #finds all occurences of the p tag (with [0] it selects the first p tag found)
# print(tags.find_all("b"))          #finds all occurences of the b tag within the p tag found  

###############################################################################################################################
################################################## Searching and Filtering ####################################################
###############################################################################################################################

# with open("index2.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")           #You can access the attributes and modify them like in a dictionary
# tag["value"] = "new value"
# tag["color"] = "blue"              #You can add new attributes the same way         

# print(tag.attrs)                   #tag.attrs will show all the attributes in a dictionary

# tags = doc.find_all(["p", "div", "li"]) #can search for a list of tags

# tags = doc.find_all(["option"], string="Undergraduate", value="undergraduate") #more specific search. will find all that meets the criteria

# tags = doc.find_all(class_ = "btn-item") #finds all classses with the name "btn-item"

# tags = doc.find_all(string=re.compile("\$.*"), limit=1)  #seaches for a regular expression \$.* means $ and anything that comes after it will be selected. limit, limits how many results.
#                                                 # output => ['\n        $2345\n      ', '\n        $123\n        '] to remove the blankspaces use

# for tag in tags:
#     print(tag.strip())


# tags = doc.find_all("input", type="text")     #changing parts of the html file
# for tag in tags:
#     tag['placeholder'] = "I changed you"

# with open("changed.html", "w") as file:       #overwriting or creating a file with the changes
#     file.write(str(doc))

