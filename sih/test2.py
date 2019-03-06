from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup as bs
import urlparse
import urllib
from urllib2 import urlopen
from urllib import urlretrieve
import sys
import requests
from PIL import Image, ImageTk    
import numpy as np
import cv2
import time
import face_recognition
from skimage import io
import sys
from twitter import *

#region Driver Setup
# options = webdriver.ChromeOptions()#"
# prefs={"profile.managed_default_content_settings.images": 1,'disk-cache-size': 4096 }
# options.add_experimental_option('prefs', prefs)
# options.headless = True 
# options.add_argument("--user-data-dir=/home/anurag/.config/google-chrome/")
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(chrome_options=options)
# driver=webdriver.PhantomJS()
#endregion
ans="xyz"
cnt=0
def reco_linked(source,base):
    driver.get("https://www.linkedin.com/in/"+source.split('/')[4]+"/detail/photo")
    time.sleep(5)
    img=driver.get_screenshot_as_file("sih/Samples/main_base.png")

    p1 = face_recognition.load_image_file(base)
    pe1 = face_recognition.face_encodings(p1)[0] 

    p2 = face_recognition.load_image_file("sih/Samples/main_base.png")
    pe2 = face_recognition.face_encodings(p2)
    if len(pe2)>0:
        pe2=face_recognition.face_encodings(p2)[0] 
    else:
        return False
    
    face_locations = face_recognition.face_locations(p2)
    face_encodings = face_recognition.face_encodings(p2, face_locations)

    match=False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([pe1], face_encoding, tolerance=0.50)
        if True in matches:
            match=True
            break
    if os.path.isfile("sih/Samples/main_base.png"):
        os.remove("sih/Samples/main_base.png") 
    return match

def reco_deep(u2):
    p1 = face_recognition.load_image_file('/home/anurag/Desktop/Py/sih/Samples/main_test.jpg')
    pe1 = face_recognition.face_encodings(p1, num_jitters=10)[0] 

    urlretrieve(u2, "/home/anurag/Desktop/Py/sih/Samples/main_base.jpg")
    p2 = face_recognition.load_image_file("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg")
    

    pe2 = face_recognition.face_encodings(p2, num_jitters=10)
    if len(pe2)>0:
        pe2=face_recognition.face_encodings(p2)[0] 
    else:
        return False
    face_locations = face_recognition.face_locations(p2)
    face_encodings = face_recognition.face_encodings(p2, face_locations)
    match=False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([pe1], face_encoding, tolerance=0.57)
        if True in matches:
            # face_distances = face_recognition.face_distance([pe1], face_encoding, tolerance=0.465)
            if os.path.isfile("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg"):
                os.remove("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg") 
            return face_distances
            
        
    if os.path.isfile("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg"):
        os.remove("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg") 
    return -1

def reco(u2,base):
    # '/home/anurag/Desktop/Py/sih/Samples/base_photo.jpg'
    p1 = face_recognition.load_image_file("public"+base)
    pe1 = face_recognition.face_encodings(p1)[0] 

    # urlretrieve(u2, "/home/anurag/Desktop/Py/sih/Samples/main_base.jpg")
    # p2 = face_recognition.load_image_file("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg")
    p2 = face_recognition.load_image_file(u2)

    pe2 = face_recognition.face_encodings(p2)
    if len(pe2)>0:
        pe2=face_recognition.face_encodings(p2)[0] 
    else:
        return False
    face_locations = face_recognition.face_locations(p2)
    face_encodings = face_recognition.face_encodings(p2, face_locations)
    match=False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([pe1], face_encoding, tolerance=0.50)
        # print face_recognition.face_distance([pe1], face_encoding)
        if True in matches:
            match=True
            break
        
    if os.path.isfile("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg"):
        os.remove("/home/anurag/Desktop/Py/sih/Samples/main_base.jpg") 
    return match

 

def about_page(source,base):
    driver.get(source)
    about_page=driver.page_source
    abt_soup = bs(about_page, "html.parser")
    user_id= abt_soup.find_all("meta",{"property":"al:android:url"})[0].get("content",None).split('/')[3]
    image="https://graph.facebook.com/"+user_id+"/picture?type=large&width=720&height=720"
    
    urlretrieve(image, "sih/Samples/"+user_id+".jpg")
    if reco("sih/Samples/"+user_id+".jpg",base) is True:
        # ans.append(source)
        global ans
        ans=source
        print source
        if os.path.isfile("sih/Samples/"+user_id+".jpg"):
            os.remove("sih/Samples/"+user_id+".jpg") 
        return True

    if os.path.isfile("sih/Samples/"+user_id+".jpg"):
            os.remove("sih/Samples/"+user_id+".jpg") 
    return False

def linked_in(Query,base):
    driver.get('https://www.linkedin.com')
    username = driver.find_element_by_id('login-email')
    username.send_keys('manthankeim7@gmail.com')
    password = driver.find_element_by_id('login-password')
    password.send_keys('appleosxYOSEMITE')
    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    sign_in_button.click()
    driver.get('https:www.google.com')
    search_query = driver.find_element_by_name('q')
    search_query.send_keys('site:linkedin.com/in/ AND "'+Query+'"')
    search_query.send_keys(Keys.ENTER)
    time.sleep(0.5)
    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]
    time.sleep(0.5)
    for id in linkedin_urls:
        if reco_linked(id,base):
            print id
            return


def get_twitter(Query,base):
    twitter = Twitter(auth = OAuth("2699843612-5DsF2mtrFa532oAUxn6NClwHgzgJWxfo69AxCLL",
                  "qhO6LteGsQWL4Kl7InnmNE0mB0VhqZH9SNKQm5FunZ64r",
                  "F2AlqdrzHpHtgD26VhcVbvkIf",
                  "MgBE9SNSbRYNeltloW4EZLwosHIQiHa7SwNpDJV5wLCEmjwpd7"))
    results = twitter.users.search(q = '"'+Query+'"',page=2,count=50,include_entities=None)
    # print len(results)
    # print results
    for user in results:
        img_name="Samples/"+user["screen_name"]+user["profile_image_url"].split("_normal")[1]
        img_link=user["profile_image_url"].split("_normal")[0]+user["profile_image_url"].split("_normal")[1]
        urlretrieve(img_link,img_name)
        # print img_name
        # print img_link
        # print user["screen_name"]
        if reco(img_name,base) is True:
            print "http://www.twitter.com/"+user["screen_name"]
            # print user["url"]
            if os.path.isfile(img_name):
                os.remove(img_name)
            return user["url"]
        
        if os.path.isfile(img_name):
            os.remove(img_name)
        
    return None

def WebWork(Query,base):
    # print "Open the website"
    driver.get('https://www.facebook.com/public/'+Query)
    # username_box = driver.find_element_by_id('email')
    # password_box = driver.find_element_by_id('pass')

    
    

    # username_box.send_keys('xxxxxxxxxxx@gmail.com')
    # password_box.send_keys('xxxxxxxxxxx')

    

    # password_box.send_keys(Keys.ENTER)

    # login_button = driver.find_element_by_id('u_0_2')

    
    # print "Logged in..."
    # url="https://www.facebook.com/search/people/?q="+Query
    # driver.get(url)


    # t_end = time.time() + 10
    # html = driver.find_element_by_tag_name('html')
    # while time.time() <= t_end:    
    #     html.send_keys(Keys.END)
        


    page_source=driver.page_source
    soup = bs(page_source, "html.parser")
    
    for link in soup.findAll("a", {"class": "_2ial"}):
        dp_link=link.get('href')
        # print dp_link
        # print link.get('href')
        # print  " "
        # about_page(dp_link)
        if about_page(dp_link,base) is True:
            break
    



param1=sys.argv[1]
param2=sys.argv[2]
# if len(ans)>1:
#     mx= 1000000000000
#     idx=ans[0]
#     for i in ans:
#         d=reco_deep(i)
#         if d<mx:
#             mx=d
#             idx=i

#     print idx  
# else:
#     print ans[0]
# var=get_twitter(param1,param2)
if True:
    options = webdriver.ChromeOptions()#"
    prefs={"profile.managed_default_content_settings.images": 2,'disk-cache-size': 4096 }
    options.add_experimental_option('prefs', prefs)
    # options.headless = True 
    # options.add_argument("--user-data-dir=/home/anurag/.config/google-chrome/")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    WebWork(param1,param2)

    # linked_in(param1+" Future",param2)
    driver.quit()
else:
    print var

# linked_in(param1,param2)
# driver.quit()
# os.remove("/home/anurag/Desktop/Py/sih/Samples/base_photo.jpg") 
# print ans
