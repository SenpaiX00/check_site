import requests
import urllib2, ssl
import random

# ------------------------------------------------------------------------------------------------
# Author: Senpai
# Date: September 2020
# Purpose: This script is intended to check a list of URLs for live (return 200 response) URLs &&
# ensure those URLs are not redirecting
# ------------------------------------------------------------------------------------------------

Live_List= [] # List of live sites (but may also redirect)
No_redirect=[] # List of live sites that DO NOT re-direct

def random_100():
    c = 0
    top = 100
    while c != top:
        print("random item from list is: ", random.choice(No_redirect))
        c += 1

def redirecting(): #Checks if the Live_List of URLs redirects, and filters out anysites that redirect after 30 seconds
    for site in Live_List:
        try:
            req = urllib2.Request(url=site)
            resp = urllib2.urlopen(req, timeout=20, context=ssl._create_unverified_context())
            redirected = resp.geturl() != url  # redirected will be a boolean True/False
            if redirected == True:
                No_redirect.append(site)
        except Exception as e:
            print("EXCEPTION BEING THROWN")

def only_200(url):
    Live_List.append(url)

def check_url(url):
    print("Checking URL: ", url)
    try:
        #r = requests.head(url) #some redirects after 20 seconds
        x = requests.get(url, verify=False)
        if x.status_code == 200:
            print("LIVE")
            only_200(url)
        if x.status_code != 200 : print("DEAD")
    except Exception as e:
        print("That doesn't work")
    #x = requests.head("https://fensftp.pearson.com/")
    #print(x.status_code)

sites = ["somesite.com"]
for site in sites:
    print("------------------------------------------------------------")
    url = "http://"+site
    check_url(url)
    url2 = "https://"+site
    check_url(url2)
print("Checking redirects now")
redirecting()
#print ("Printing sites that DO NOT Redirect")
#for site in No_redirect:
#    print(site)
print ("Randomizing output beep...boop...")
random_100()
