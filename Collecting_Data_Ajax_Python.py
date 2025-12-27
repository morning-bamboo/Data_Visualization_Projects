import requests
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

start_page = int(input("enter the start page # (>=1): ")) #which page to start collecting
end_page = int(input("enter the end page #(<= 50): ")) #which page to end collecting

all_course = []

for i in range(start_page, end_page+1): #loop from beginning to the end_page (end_page+1)
    url = "https://api.hahow.in/api/products/search?limit=24&mixedResults=true&page=%d&sort=TRENDING"%(i-1) #(to match link with page #)
    response = requests.get(url, headers = headers)
    # print(url) #this is set to check the url at the beginning
    root_json = response.json() #here is a dict
    course_list = []
    for j in range(24):
        course_info_dict = {}
        title = root_json["data"]["productData"]["products"][j]["product"]["title"]

        # if / else: to make sure keys:values could be assigned correctly, in case there's no keys
        if "owner" in root_json["data"]["productData"]["products"][j]["product"]:
            author = root_json["data"]["productData"]["products"][j]["product"]["owner"]["name"]
        else:
            author = "N/A"

        if "basePricingInfo" in root_json["data"]["productData"]["products"][j]["product"]:
            base_price = root_json["data"]["productData"]["products"][j]["product"]["basePricingInfo"]["price"]
        else:
            base_price = "N/A"

        if "price" in root_json["data"]["productData"]["products"][j]["product"]:
            price = root_json["data"]["productData"]["products"][j]["product"]["price"]
        else:
            price = "N/A"

        if "numSoldTickets" in root_json["data"]["productData"]["products"][j]["product"]:
            num_sold = root_json["data"]["productData"]["products"][j]["product"]["numSoldTickets"]
        else:
            num_sold = "N/A"

        if "tags" in root_json["data"]["productData"]["products"][j]["product"]:
            tags = root_json["data"]["productData"]["products"][j]["product"]["tags"]
        else:
            tags = "N/A"

        if "purchasePlan" in root_json["data"]["productData"]["products"][j]["product"]:
            purchase_plan_price = root_json["data"]["productData"]["products"][j]["product"]["purchasePlan"]["price"]
        else:
            purchase_plan_price = "N/A"

        course_info_dict = {
            "title": title,
            "author":author,
            "base_price":base_price,
            "price":price,
            "num_sold":num_sold,
            "tags":tags,
            "purchase_plan_price":purchase_plan_price
        }

        course_list.append(course_info_dict)

    # print(course_list) # to print the info from the current page
    all_course.extend(course_list)

df = pd.DataFrame(all_course, columns=["title","author","base_price","price","num_sold","tags","purchase_plan_price"])

print(df.to_string()) # to display all the data in matrix form

df.to_csv("hahow_course_10pages.csv",index=False) #(save collected date into csv)








