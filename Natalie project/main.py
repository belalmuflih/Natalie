from selenium import webdriver
import time, os
import urllib.request



driver = webdriver.Chrome("./chromedriver.exe")
# url = input("Please enter url -> ")

url = input("please Paste the link here ->")
images = []

driver.get(url)
time.sleep(5)

title = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/h2').text

imgs = driver.find_elements_by_class_name('four-apartments')



for img in imgs:
	img = img.get_attribute("style")
	images.append(img[23:113])

try:
	os.mkdir(title)
except FileExistsError:
	print('file already exist please delete or rename it')
	input('Press Enterto exit')
	exit()

for i in range(-1, 4):
	urllib.request.urlretrieve(images[i],f"{title}/{title[i]}.jpg")

images = []

main_img = driver.find_element_by_class_name('img-main-box').get_attribute("style")

main_img = main_img[23:113]
images.append(main_img)

urllib.request.urlretrieve(main_img, f"{title}/{title} main pic.jpg")