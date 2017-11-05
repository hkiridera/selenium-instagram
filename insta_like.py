#-*-coding: utf-8-*-
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')             #Chromeを操作
driver.get('https://www.instagram.com/?hl=ja')    #インスタを開く
time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button').click()  #ログインボタンをxpathで指定
time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
#driver.find_element_by_xpath('//*[@id="email"]').send_keys('')  #メールアドレス
#driver.find_element_by_xpath('//*[@id="pass"]').send_keys('')  #メールアドレス
#driver.find_element_by_xpath('//*[@id="loginbutton"]').click()  #ログインボタンをxpathで指定


time.sleep(30)                                           #ページを開くまで時間がかかるので取り敢えず6秒停止

for i in range(1,1000):
  driver.get('https://www.instagram.com/')  #個別のページを開く
  time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
  try:
    driver.find_element_by_xpath('//*[@id="mainFeed"]/div/div/div[1]/div/article[1]/div[2]/section[1]/a[1]/span').click()  #like
#    time.sleep(3600*1)
    time.sleep(60*2)
  except KeyboardInterrupt  :
    print ( "KeyboardInterrupt\n" )
    driver.quit()
  except:
    print "ignore errors"
    time.sleep(60*5)

driver.quit()
