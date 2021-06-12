from tkinter import *
import tkinter.font as font

import time
import requests
from termcolor import colored
from bs4 import BeautifulSoup

root = Tk()
root['background'] = "#313131"
root.title("Riyasewana Scraper")
root.resizable(False, False)

try:
    root.iconbitmap(r".\icon.ico")
except:
    pass

def RIYASEWANA_SCRAPER_TXT(weblink):

    r = requests.get(weblink)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    all_items = soup.find_all("li", {"class": "item round"})

    item_name = all_items[1].find("h2", {"class": "more"}).find("a").text
    item_link = all_items[1].find("h2", {"class": "more"}).find("a").get('href')
    
    item_location_all = all_items[1].find_all("div", {"class":"boxintxt"})

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
    print(colored("\nThe Output have been saved to a text file!\nThank you for using the program!\nHave a great day!", 'red'))

def RIYASEWANA_START():
    link_to_riyasewana = elink.get()

    try:
        RIYASEWANA_SCRAPER_TXT(link_to_riyasewana)
        
        try:
            filer = open("Riyasewana_Scraped.txt", "r", encoding="utf8")
            filer_content = filer.read()
        except:
            tmain.insert(END, "\nUNABLE TO READ THE GENERATED TEXT FILE")
            print(colored("UNABLE TO READ THE GENERATED TEXT FILE", 'red'))

        try:
            try:
                tmain.delete(0, END)
            except:
                pass
            tmain.insert(END, "\nSUCCESSFULLY SCRAPED: " + link_to_riyasewana + "\n\n" + filer_content)
            # tmain.insert(END, filer_content)
        except:
            try:
                tmain.delete(0, END)
            except:
                pass
            tmain.insert(END, "\nUNABLE TO INSER THE SCRAPED INFORMATION TO THE PROGRAM!\nTHE CONTENT IS SAVED TO A FILE\nYOU CAN STILL ACCESS IT")
            print(colored("\nUNABLE TO INSER THE SCRAPED INFORMATION TO THE PROGRAM!\nTHE CONTENT IS SAVED TO A FILE\nYOU CAN STILL ACCESS IT", 'red'))


    except:
        try:
            tmain.delete(0, END)
        except:
            pass
        tmain.insert(END, "\nUNABLE TO SCRAP THE RIYASEWANA WEBSITE!\nPLEASE TRY AGAIN LATER!\nTHE PROGRAM WILL CLOSE AUTOMATICALLY AFTER 30 SECONDS")
        print(colored("UNABLE TO SCRAP RIYASEWANA WEBSITE!\nPLEASE TRY AGAIN LATER!\nTHE PROGRAM WILL CLOSE AUTOMATICALLY AFTER 30 SECONDS", 'red'))
        time.sleep(30)
        exit()

def clearall():
    elink.delete(0, END)
    tmain.delete("1.0", END)
    
# https://riyasewana.com/search/suzuki/

# font types
font_text = font.Font(family='Arial', size="14", weight="bold")
font_entry = font.Font(family='Arial', size="13")
font_label = font.Font(family='Arial', size="13", weight="bold")
font_btns = font.Font(family='Arial', size="15", weight="bold")

# main text field to display the results scraped to the file
tmain = Text(root, width=51, height=14, bg="#1A1A1A", fg="#ffffff")
tmain.grid(row=5, column=0, columnspan=2, padx=10, pady=2)
tmain["font"] = font_text

ltop = Label(root, text="Enter the link below: ", bg="#313131", fg="#ffffff")
ltop.grid(row=3, column=0, columnspan=2, pady=7)
ltop['font'] = font_label

# enter the link here
elink = Entry(root, width=60, borderwidth=10, bg="#2C2C2C", fg="#ffffff")
elink.grid(row=4, column=0, columnspan=2)
elink['font'] = font_entry

# click this button to start the program, will be at the bottom ( left )
bstartscrapping = Button(root, text="Start Scraping", command=RIYASEWANA_START, bg="#00830C", fg="#ffffff", padx=100, pady=7)
bstartscrapping.grid(row=6, column=0, columnspan=1)
bstartscrapping['font'] = font_btns

# clear all
bclear_all = Button(root, text="Clear", command = clearall, bg="#DF7F25", fg="#ffffff", padx=90, pady=7)
bclear_all.grid(row=6, column=1, columnspan=1)
bclear_all['font'] = font_btns

root.mainloop()

print(colored("This program will be closed automatically in 30 seconds", 'green'))
time.sleep(30)
# exit()
