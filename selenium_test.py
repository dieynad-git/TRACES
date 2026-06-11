#!/usr/bin/env python3 
from selenium import  webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By 
import time 


browser = webdriver.Chrome()
browser.get('https://www.strava.com/')

time.sleep(2) #ou browser.implicitly_wait(2)


## Ouvrir directement "https://www.strava.com/register/free" ? Au lieu d'ouvrir de 
## la page d'accueil de strava ? Je vois pas l'interet la

# Refuser les cookies non-essentiels
no_cookies = browser.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")
no_cookies.click()
print("Cookies refuses")

## Comment m'assurer que les cookies sont refuses ? Liste ?
#time.sleep(5)

try: 
    sign_up = browser.find_element(By.CLASS_NAME, "Button_btn__EdK33.Button_primary___8ywh.CallToAction_callToAction__CvDE5.MobileNav_headerCallToAction__eh4jD")
    ## Why does adding a '.' work for compound class names ?
    sign_up.click()

except NoSuchElementException:
    print("Sign up non trouve")

else: 
    print("Sign up trouve")

time.sleep(3)

# Prendre une capture
browser.save_screenshot('screen_selen.png')
browser.quit()

#22 29 207 