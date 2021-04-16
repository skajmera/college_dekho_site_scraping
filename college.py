from bs4 import BeautifulSoup
from pprint import pprint
import requests,json,os
def college_details():
    res=requests.get("https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/")
    soup=BeautifulSoup(res.text,'html.parser')
    raw_html=soup.find("div",class_="middle-container").find_all('div',class_="box")
    for i in (raw_html):
        link=("https://www.collegedekho.com/"+i.find('a').get('href'))
            ##  name of college ## 
        name=(i.find('a').get("title")) 
        m=(i.find(class_="title").find(class_="info").find_all('li'))
            ##   college type  ##
        ttype=(m[1].text)
        ser=requests.get(link)
        roup=BeautifulSoup(ser.text,'html.parser')
        ##  college contact  ##
        contact=roup.find(class_="block collegeContactBlock").find(class_="data").text.strip()
        ss=(roup.find_all(class_="block collegeContactBlock"))
        rate=roup.find(class_="rating-per")
        for j in ss:
            ##  college email  ##
            email=j.find_all("li")[1].text[10:].strip()  
            ## college address ##   
            address=j.find_all("li")[-1].text[9:].strip()    
        ##  college facilities  ##
        kk=roup.find(class_="block facilitiesBlock").find(class_="box").find_all(class_="title")
        facility=[]
        for k in kk:
            pr=k.text.strip()
            facility.append(pr)
        ##  college rating ##
        try:
            rating=(rate.find('span', class_="star-ratings-sprite-rating").get('style'))[6:-3]
            rating=int(rating)
            rating=(rating/20) 
        except :
            rating="None"
        ##  creat dictionary and import json file  ##
        dic={"college name":name,"type":ttype,"rating":rating,"address":address,"email":email,"contact":contact,"facilities":facility}
        f=open("college.json",'a')
        json.dump(dic,f,indent=4)
        f.close()
        print("complete")
college_details()    
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        