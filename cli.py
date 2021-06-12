import time
import os
# from tkinter.constants import E
import requests
from termcolor import colored
from bs4 import BeautifulSoup
import platform

def RIYASEWANA_SCRAPER_NO_FILE(weblink):

    r = requests.get(weblink)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    # print(soup.prettify)

    all_items = soup.find_all("li", {"class": "item round"})

    item_name = all_items[1].find("h2", {"class": "more"}).find("a").text
    item_link = all_items[1].find("h2", {"class": "more"}).find("a").get('href')
    
    item_location_all = all_items[1].find_all("div", {"class":"boxintxt"})

    # item_location = item_location_all[0].text
    # item_price = item_location_all[1].text
    # item_distance = item_location_all[2].text
    # item_date = item_location_all[3].text

    item_image = all_items[1].find("div", {"class":"imgbox"})
    item_image2 = item_image.find("a")
    item_image3 = item_image2.find("img")
    item_image4 = item_image3.get("src")
    item_image_link = "https:" + str(item_image4)


    for items in range(len(all_items)):
        
        try:
            item = all_items[items]
            
        except:
            print(colored("Unable to fetch data!", 'red'))
            exit()

        try:
            item_name = item.find("h2", {"class": "more"}).find("a").text
            print("Name: " + item_name)
        except:
            print(colored("Unable to get the name of this product!", 'red'))
        
        try:
            item_link = item.find("h2", {"class": "more"}).find("a").get('href')
            print("Link: " + item_link)
        except:
            print(colored("Unable to get the link of this product!", 'red'))

        try:
            try:
                item_location_all = item.find_all("div", {"class":"boxintxt"})
            except:
                pass
            try:
                item_location = item_location_all[0].text
            except:
                pass
            
            try:
                item_price = item_location_all[1].text
            except:
                pass
                
            try:
                item_distance = item_location_all[2].text
            except:
                pass
            
            try:
                item_date = item_location_all[3].text
            except:
                pass
        except:
            print(colored("Unable fetch data - 2nd!", 'red'))
        
        try:
            print("Location: " + item_location.replace(" ",""))
        except:
            print(colored("Unable to get the location of this product!", 'red'))

        try:
            print("Price: " + item_price.replace(" ",""))
        except:
            print(colored("Unable to get the price of this product!", 'red'))
        
        try:
            print("Distance Travelled: " + item_distance.replace(" ",""))
        except:
            print(colored("Unable to get the Distance Travelled  of this product!", 'red'))
        
        try:
            print("Date: " + item_date.replace(" ",""))
        except:
            print(colored("Unable to get the date of this product!", 'red'))
        
        try:
            item_image = item.find("div", {"class":"imgbox"})
            item_image2 = item_image.find("a")
            item_image3 = item_image2.find("img")
            item_image4 = item_image3.get("src")
            item_image_link = "https:" + str(item_image4)

            print("Image Link: " + item_image_link)
        except:
            print(colored("Unable to get the link of the image of this product!", 'red'))
        
        print("\n\n")
    
    print(colored("Waiting 30 seconds for the program to close!\nThank you for using the program!\nHave a great day!", 'red'))
    time.sleep(30)

def RIYASEWANA_SCRAPER_TXT(weblink):

    r = requests.get(weblink)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    # print(soup.prettify)

    all_items = soup.find_all("li", {"class": "item round"})

    item_name = all_items[1].find("h2", {"class": "more"}).find("a").text
    item_link = all_items[1].find("h2", {"class": "more"}).find("a").get('href')
    
    item_location_all = all_items[1].find_all("div", {"class":"boxintxt"})

    # item_location = item_location_all[0].text
    # item_price = item_location_all[1].text
    # item_distance = item_location_all[2].text
    # item_date = item_location_all[3].text

    item_image = all_items[1].find("div", {"class":"imgbox"})
    item_image2 = item_image.find("a")
    item_image3 = item_image2.find("img")
    item_image4 = item_image3.get("src")
    item_image_link = "https:" + str(item_image4)

    filew = open("Riyasewana_Scraped.txt", "w", encoding="utf8")
    filew.write("")
    filew.close()

    file = open("Riyasewana_Scraped.txt", "r+", encoding="utf8")

    for items in range(len(all_items)):
        
        try:
            item = all_items[items]
            
        except:
            print(colored("Unable to fetch data!", 'red'))
            exit()

        try:
            item_name = item.find("h2", {"class": "more"}).find("a").text
            print("Name: " + item_name)
            file.write("Name: " + item_name)
        except:
            print(colored("Unable to get the name of this product!", 'red'))
            file.write("Unable to get the name of this product!")
        
        try:
            item_link = item.find("h2", {"class": "more"}).find("a").get('href')
            print("Link: " + item_link)
            file.write("\nLink: " + item_link)
        except:
            print(colored("Unable to get the link of this product!", 'red'))
            file.write("\nUnable to get the link of this product!")

        try:
            try:
                item_location_all = item.find_all("div", {"class":"boxintxt"})
            except:
                pass
            try:
                item_location = item_location_all[0].text
            except:
                pass
            
            try:
                item_price = item_location_all[1].text
            except:
                pass
                
            try:
                item_distance = item_location_all[2].text
            except:
                pass
            
            try:
                item_date = item_location_all[3].text
            except:
                pass
        except:
            print(colored("Unable fetch data - 2nd!", 'red'))
        
        try:
            print("Location: " + item_location.replace(" ",""))
            file.write("\nLocation: " + item_location.replace(" ",""))
        except:
            print(colored("Unable to get the location of this product!", 'red'))
            file.write("\nUnable to get the location of this product!")

        try:
            print("Price: " + item_price.replace(" ",""))
            file.write("\nPrice: " + item_price.replace(" ",""))
        except:
            print(colored("\nUnable to get the price of this product!", 'red'))
            file.write("\nUnable to get the price of this product!")
        
        try:
            print("Distance Travelled: " + item_distance.replace(" ",""))
            file.write("\nDistance Travelled: " + item_distance.replace(" ",""))
        except:
            print(colored("Unable to get the Distance Travelled  of this product!", 'red'))
            file.write("\nUnable to get the Distance Travelled  of this product!")
        
        try:
            print("Date: " + item_date.replace(" ",""))
            file.write("\nDate: " + item_date.replace(" ",""))
        except:
            print(colored("Unable to get the date of this product!", 'red'))
            file.write("\nUnable to get the date of this product!")
        
        try:
            item_image = item.find("div", {"class":"imgbox"})
            item_image2 = item_image.find("a")
            item_image3 = item_image2.find("img")
            item_image4 = item_image3.get("src")
            item_image_link = "https:" + str(item_image4)

            print("Image Link: " + item_image_link)
            file.write("\nImage Link: " + item_image_link)
        except:
            print(colored("Unable to get the link of the image of this product!", 'red'))
            file.write("\nUnable to get the link of the image of this product!")
        
        print("\n\n")
        file.write("\n\n")
    
    file.close()
    print(colored("\nThe Output have been saved to a text file!\nWaiting 30 seconds for the program to close!\nThank you for using the program!\nHave a great day!", 'red'))
    time.sleep(30)

def ENTIRE_PROGRAM():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            clear_screen_command = "cls"
        elif os_name == "Linux":
            clear_screen_command = "clear"
        else:
            clear_screen_command = "clear"
    except:
        print(colored("ERROR HAS OCCURED!\nUNABLE TO IDENTIFY THE CURRENT OPERATING SYSTEM!", 'red'))
        exit()


    os.system(clear_screen_command)
    choice_home = input("home>> ")
    
    if choice_home == "nf":
        os.system(clear_screen_command)
        link = input("Enter the link>> ")
        RIYASEWANA_SCRAPER_NO_FILE(link)

    elif choice_home == "help":
        os.system(clear_screen_command)
        print(colored("\nNOTE: These commands only work in the Home Page\nhelp --> Take you to this page\nnf   --> Scrap without saving to a file\ntxt  --> Scrap and save to a text file\n\nEnter 'home' to go back to the home page!", 'blue'))
        subchoice_help = input("\nhelp>> ")
        if subchoice_help == "home":
            ENTIRE_PROGRAM()
        
        else:
            print(colored("Please enter a valid option! \nThe program will start again within 5 seconds!", 'red'))
            time.sleep(5)
            ENTIRE_PROGRAM()

    elif choice_home == "txt":
        os.system(clear_screen_command)
        link = input("Enter the link>> ")
        RIYASEWANA_SCRAPER_TXT(link)
    
    else:
        print(colored("Please enter a valid option! \nThe program will start again within 5 seconds!", 'red'))
        time.sleep(5)
        ENTIRE_PROGRAM()

try:
    ENTIRE_PROGRAM()
except Exception as e:
    print("error has occured: ", e)

# link = "https://riyasewana.com/search/suzuki/alto"
# RIYASEWANA_SCRAPER_NO_FILE(link)