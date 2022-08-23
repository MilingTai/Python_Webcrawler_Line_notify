import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('chromedriver')
driver.implicitly_wait(8) 
 
url="https://www.farfetch.com/tw/shopping/women/isabel-marant-haley-denim-bucket-hat-item-17392773.aspx?storeid=13537"
driver.get(url)

#To get html(source_code) by driver.page_source  
html=driver.page_source
#print(html) 

price=driver.find_element(By.CSS_SELECTOR,'#content > div > div.ltr-wckt8b > div.ltr-1rujwwh > div > div > div.ltr-1q071fb > div.ltr-10c5n0l.eev02n90 > p.ltr-194u1uv-Heading.e54eo9p0') 
print(price.text[1:])

price_num= price.text[1:].replace(",","")
#If price get discount under 6000
#, then send discount message through LINE Notify
if int(price_num) < 6000:  #將爬取的價格字串轉型為整數
    headers = {
        "Authorization": "Bearer " 
        + "your 權杖(token) ", 
        "Content-Type": "application/x-www-form-urlencoded"
    }
    #To define sending message
    params = {"message": "Haley denim bucket hat OF Isabel Marant is on sale NOW!!! ONLY COST $" + price_num}
    
    #To call LINE Notify's API
    #if no error would get 200的狀態碼(status_code)
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  #200
    
driver.quit() 