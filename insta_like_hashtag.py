#-*-coding: utf-8-*-
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')             #Chromeを操作
driver.get('https://www.instagram.com/?hl=ja')    #インスタを開く
time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button').click()  #ログインボタンをxpathで指定
time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
driver.find_element_by_xpath('//*[@id="email"]').send_keys('')  #メールアドレス
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('')  #メールアドレス
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()  #ログインボタンをxpathで指定

time.sleep(6)                                           #ページを開くまで時間がかかるので取り敢えず6秒停止

for i in range(1,100):
  for j in range(1,3):
    time.sleep(1)                                           #ページを開くまで時間がかかるので取り敢えず１秒停止
    try:
#      driver.get('https://www.instagram.com/explore/tags/%E5%86%99%E7%9C%9F%E3%82%92%E6%92%AE%E3%82%8B%E3%81%AE%E3%81%8C%E5%A5%BD%E3%81%8D%E3%81%AA%E4%BA%BA%E3%81%A8%E7%B9%8B%E3%81%8C%E3%82%8A%E3%81%9F%E3%81%84/')  #写真撮るのが好きな人とつながりたい
      driver.get('https://www.instagram.com/explore/tags/%E5%86%99%E7%9C%9F/')  #写真
      pic = '//*[@id="react-root"]/section/main/article/div[1]/div/div[' + str(i) + ']/div[' + str(j) + ']/a/div'
  #    print(pic)
      driver.find_element_by_xpath(pic).click()  #個別の写真
      time.sleep(1)                                           #表示してから１秒待つ
      driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/article/div[2]/section[1]/a[1]/span').click()  #like
      time.sleep(1)                                           #likeボタンを押してから1秒待つ
  #    time.sleep(3600*1)
      time.sleep(60*0.1)
    except KeyboardInterrupt  :
      print ( "KeyboardInterrupt\n" )
      driver.quit()
    except:
      print "ignore errors"
      time.sleep(60*5)

driver.quit()
