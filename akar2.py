import sys
import csv
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import re
import math
links_list=[]
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
counter = 0
pages=None
link=input("Please Enter The Category Link: ")
page = int(input("Enter The Page Number to start from: "))

availabletries=4
while True:
    try:
        Num_of_advertises=int(input("Enter Number of Ads: "))
        if type(Num_of_advertises) == int:
            pages = math.ceil(Num_of_advertises / 20)
            print(f"The data will be scraped from {pages} pages")
            sleep(2)
            break

    except Exception as e :
        availabletries-=1
        print("Please Enter Number only")
        print(f"You have {availabletries} tries left or the program will quit")
        if availabletries == 0:
            print("Because you didn't enter a valid number the program stopped so try again with a valid number!")
            break
if pages is None:
    driver.quit()
    sys.exit()
while True:
  counter += 1
  if counter == (pages + 1) : break
  try:
    driver.get(link+"/"+str(page))
    liData = driver.find_elements(By.CLASS_NAME ,'listing_LinkedListingCard__5SRvZ')
    if len(liData) == 0 :
        print("Congratulations you finished scraping ")
        break

    for element in liData:
        links_list.append("https://sa.aqar.fm"+element.get_attribute('href'))

    print(f"We are now in page: {page}")
    print(len(links_list))
    page += 1
  except:
      print(" we are in except")
      print("Check for Errors or you may finished scraping!")
      break

link_detictor =0
tries=0
dep_price = "لا"
rent_type = "لا"
InVilla = "لا"
DepDisc = 'لا'
advertiser = 'لا'
advertiserdate = 'لا'
street = 'لا'
area = 'لا'
inarea = 'لا'
Dep_width = 'لا'
Dep_length = 'لا'
rooms = "لا"
shops = "لا"
OtherRoom = "لا"
NumOfSala = 'لا'
NumOfBathrooms = 'لا'
Water = 'لا'
Floor = "لا"
BuildAge = "لا"
Furnature = "لا"
SingOrDoup = 'لا'
Kitchen = "لا"
Carenter = "لا"
Elevator = "لا"
Air = "لا"
Basement = "لا"
Electricity = "لا"
SpecEnter = "لا"
Trees = "لا"
price_for_meter = 'لا'
Abars = "لا"
Departinproj = 'لا'
Elwagha = "لا"
Porpos = "لا"
Piece = "لا"
DorgSala = "لا"
MasterRoom = "لا"
DriverRoom = "لا"
Flyingball = "لا"
Malahy = "لا"
Family = "لا"
bole = "لا"
PeotryHouse = "لا"
Hosh = "لا"
Molhak = "لا"
Sitterroom = "لا"
Doublex = "لا"
file=open('data.csv','w',encoding='utf-8',newline='')
csv_writer=csv.writer(file)
csv_writer.writerow(['السعر SAR' , 'نوع الإيجار' , 'وصف المكان' ,'المساحة م²' ,'في فيلا','المساحة الداخلية م²','عرض الشارع م' , 'الطول م' , 'العرض م' , 'عدد الحجرات' , 'عدد الصالات', 'عدد دورات المياه' , 'الدور' , 'عمر المبنى' , 'مؤثث' ,'عوائل' , 'مطبخ'
                            ,'مدخل سيارة' ,'مصعد' ,'مكيف' , 'توفر كهرباء' , 'توفر مياه','موقف خاص','عدد الأشجار', 'سعر المتر', 'الآبار','الواجهة','الغرض','علاقة المعلن بالعقار'
                           , 'القطعة' , 'درج صالة' , 'حجرة السائق' , 'ملاهى' ,'قسم عوائل', 'مسبح' ,'لينك المكان',
                            'بيت شعر' , 'حوش' ,'ملحق' ,'دوبلكس', 'غرفة خادمة', 'غرفة نوم ماستر', 'الغرف الأخرى', 'ملعب كرة طائرة','عدد المحلات', 'قبو' , 'شقة في مشروع', 'تاريخ الإضافة'])
for element in links_list:
    link=element
    link_detictor += 1
    if link_detictor == (Num_of_advertises+1):
         break
    while True:
        try:
            print(f"Scraping data from link Num: {link_detictor}")
            driver.get(element)
            department_details = driver.find_element(By.CLASS_NAME ,"listingView_detailsContainer__UwEG1")
            try:
                dep_price1 = re.findall(r'[\d]+[.,\d]+', department_details.find_element(By.CLASS_NAME, "listingView_price__2kZQ8").text)
                dep_price=int(dep_price1[0].replace(",",""))
            except:
                dep_price1= re.findall(r'\d+', department_details.find_element(By.CLASS_NAME, "listingView_price__2kZQ8").text)
                dep_price=int(dep_price1[0])
            try:
                rent_type1 = re.findall(r'\s\w{1,4}',department_details.find_element(By.CLASS_NAME ,"listingView_price__2kZQ8").text)
                rent_type=rent_type1[1].strip()
            except:pass
            try:
                departmentdisc = department_details.find_element(By.CLASS_NAME ,'listingView_description__N7Hio').text
                DepDisc=departmentdisc.replace('\n' ,' ').strip()
                if 'فيلا'in DepDisc:
                    InVilla='نعم'
            except:pass

            morebutt=department_details.find_element(By.CLASS_NAME ,'SpecsCard-module_moreBtn__-U9Ri').click()
            sleep(1)
            try:
                advertiser1=department_details.find_element(By.CLASS_NAME ,'listingView_specsCard__hLMv9').find_element(By.XPATH,"./div[3]/div[2]").text
                advertiser=advertiser1[12:16]
            except:pass
            try:
                advertiserdate1=department_details.find_element(By.CLASS_NAME ,'listingView_specsCard__hLMv9').find_element(By.XPATH,"./div[3]/div[1]").text
                advertiserdate=advertiserdate1[15:25]
            except:pass

            data_box = department_details.find_element(By.CLASS_NAME ,'listingView_specsCard__hLMv9').find_elements(By.XPATH, "./div[2]/div")
            for element in data_box:
                if element.find_element(By.XPATH,"./div[1]").text == "عرض الشارع":
                    try:
                        street1 = re.findall(r'[\d]+[.,\d]+', element.find_element(By.XPATH, "./div[2]").text)
                        street=int(street1[0].replace(",", ""))
                    except:
                        street1 = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        street=int(street1[0])
                if element.find_element(By.XPATH, "./div[1]").text == "المساحة":
                    try:
                        area1 = re.findall(r'[\d]+[.,\d]+',element.find_element(By.XPATH,"./div[2]").text)
                        area = int(area1[0].replace(",",""))
                    except:
                        area1 = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        area=int(area1[0])
                if element.find_element(By.XPATH, "./div[1]").text == "المساحة الداخلية":
                    try:
                        inarea1 = re.findall(r'[\d]+[.,\d]+',element.find_element(By.XPATH,"./div[2]").text)
                        inarea=int(inarea1[0].replace(",",""))
                    except:
                        inarea1 = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        inarea=int(inarea1[0])

                if element.find_element(By.XPATH, "./div[1]").text == "الأطوال":
                        dimensions = re.findall(r'\d+', element.find_element(By.XPATH, './div[2]').text)
                        x =int(dimensions[0])
                        y = int(dimensions[1])
                        if x > y:
                            Dep_width = y
                            Dep_length=x
                        else:
                            Dep_width=x
                            Dep_length=y
                if element.find_element(By.XPATH, "./div[1]").text == "الغرف":
                    rooms1=re.findall(r'\d+',element.find_element(By.XPATH,"./div[2]").text)
                    rooms=int(rooms1[0])
                if element.find_element(By.XPATH, "./div[1]").text == "عدد المحلات":
                    shop=re.findall(r'\d+',element.find_element(By.XPATH,"./div[2]").text)
                    shops=int(shop[0])
                if element.find_element(By.XPATH, "./div[1]").text == "عدد الغرف الاخرى":
                    roomsat=re.findall(r'\d+',element.find_element(By.XPATH,"./div[2]").text)
                    OtherRoom=int(roomsat[0])

                if element.find_element(By.XPATH, "./div[1]").text == "الصالات":
                    sala = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                    NumOfSala=int(sala[0])

                if element.find_element(By.XPATH, "./div[1]").text == "عدد دورات المياه":
                    bathrooms=re.findall(r'\d+',element.find_element(By.XPATH,"./div[2]").text)
                    NumOfBathrooms=int(bathrooms[0])
                    Water="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "الدور":
                    floor=element.find_element(By.XPATH,"./div[2]").text
                    try:
                        Floor=int(floor.strip())
                    except:Floor=floor.strip()
                if element.find_element(By.XPATH, "./div[1]").text == "عمر العقار":
                    buildage = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                    BuildAge=int(buildage[0])
                if element.find_element(By.XPATH, "./div[1]").text == "مؤثثة":
                        Furnature="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "عوائل أم عزاب":
                    if element.find_element(By.XPATH, "./div[2]").text == "عوائل":
                        SingOrDoup="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "مطبخ":
                        Kitchen='نعم'
                if element.find_element(By.XPATH, "./div[1]").text == "مدخل سيارة":
                        Carenter="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "مصعد":
                        Elevator='نعم'
                if element.find_element(By.XPATH, "./div[1]").text == "قبو":
                        Basement="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "مكيف":
                        Air="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "عداد كهرباء منفصل":
                        Electricity="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "موقف خاص":
                        SpecEnter="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "عدد الأشجار":
                    try:
                        tree = re.findall(r'[\d]+[.,\d]+', element.find_element(By.XPATH, "./div[2]").text)
                        Trees=int(tree[0].replace(",", ""))
                    except:
                        tree = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        Trees=int(tree[0])
                if element.find_element(By.XPATH, "./div[1]").text == "سعر المتر":
                    try:
                        meter = re.findall(r'[\d]+[.,\d]+', element.find_element(By.XPATH, "./div[2]").text)
                        price_for_meter=int(meter[0].replace(",", ""))
                    except:
                        meter = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        price_for_meter=int(meter[0])
                if element.find_element(By.XPATH, "./div[1]").text == "عدد الآبار":
                    try:
                        bar = re.findall(r'[\d]+[.,\d]+', element.find_element(By.XPATH, "./div[2]").text)
                        Abars=int(bar[0].replace(",", ""))
                    except:
                        bar = re.findall(r'\d+', element.find_element(By.XPATH, "./div[2]").text)
                        Abars=int(bar[0])
                if element.find_element(By.XPATH, "./div[1]").text == "شقة في مشروع":
                        Departinproj="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "الواجهة":
                    Elwagha=element.find_element(By.XPATH,"./div[2]").text
                if element.find_element(By.XPATH, "./div[1]").text == "الغرض":
                    Porpos=element.find_element(By.XPATH, "./div[2]").text
                if element.find_element(By.XPATH, "./div[1]").text == "المخطط و القطعة":
                    Piece=element.find_element(By.XPATH, "./div[2]").text
                if element.find_element(By.XPATH, "./div[1]").text == "درج صالة":
                        DorgSala="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "ملعب كرة طائرة":
                        Flyingball="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "غرف نوم ماستر":
                        MasterRoom="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "غرفة سائق":
                        DriverRoom="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "ملاهي":
                        Malahy="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "قسم عوائل":
                        Family="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "مسبح":
                        bole="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "بيت شعر":
                        PeotryHouse="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "غرفة خادمة":
                        Sitterroom="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "حوش":
                        Hosh="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "ملحق":
                        Molhak="نعم"
                if element.find_element(By.XPATH, "./div[1]").text == "دوبلكس":
                        Doublex="نعم"

            if driver.find_element(By.CLASS_NAME , 'listingView_title__ttwtw') is not None:
                break

        except Exception as e:
            print(f"Problem in link : {element}")
            tries += 1
            if tries > 5:
                print(e)
                print(" breaking while loop after scraping all data")
                break
    csv_writer.writerow(
        [dep_price, rent_type, DepDisc, area, InVilla, inarea, street, Dep_length, Dep_width, rooms, NumOfSala,
         NumOfBathrooms,
         Floor, BuildAge, Furnature, SingOrDoup, Kitchen, Carenter, Elevator, Air, Electricity, Water, SpecEnter, Trees,
         price_for_meter,
         Abars, Elwagha, Porpos, advertiser, Piece, DorgSala, DriverRoom, Malahy, Family, bole, element, PeotryHouse,
         Hosh, Molhak, Doublex,
         Sitterroom, MasterRoom, OtherRoom, Flyingball, shops, Basement, Departinproj, advertiserdate])
# print(len(Doublex),len(linkatlist),len(Shops),len(Basement), len(OtherRoom),len(Molhak),len(Malahy),len(price_for_meter),len(DriverRoom) ,len(DorgSala),len(Piece),len(Adver_relation),len(Area),len(Elwagha) , len(InVilla), len(InnerArea) , len(SingOrDoup) , len(Kitchen) , len(Carenter) , len(Electricity), len(DepDisc) , len(Departinproj)
#        ,len(Family) , len(Water) , len(bole) , len(Sitterroom) , len(Abars) , len(Dep_length) , len(Dep_width) , len(Porpos) , len(Piece) , len(Elevator) , len(Air) , len(Malahy))

print("Congratulations All required data are scraped")
print("Good Luck")
file.close()
driver.quit()