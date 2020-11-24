from selenium import webdriver
import time, os
import urllib.request
import shutil


# urllib.request.urlretrieve(images[i],f"{title}/{title[i]}.jpg")
# for img in after_click_images:
# 	img = img.get_attribute("style")
# 	images.append(img[23:113])




class Download:
	driver = webdriver.Chrome(r"C:\Users\belal\Google driver\chromedriver")
	images = []	

	def __init__(self, link):
		self.link = link

	def link_download(self):
		self.driver.get(self.link)
		time.sleep(4)
		self.title = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/h2').text
		self.main = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div')
		self.main_atrb = self.main.get_attribute('style')
		self.main_url = self.main_atrb[23:113]
		os.mkdir(self.title)
		urllib.request.urlretrieve(self.main_url, f"{self.title}/{self.title}.jpg")
		self.main.click()
		time.sleep(4)

	images = []

	def idk(self):
		self.thumbnail = self.driver.find_elements_by_class_name('thumbnail_199fmdb')
		for img in self.thumbnail:
			self.img_atrb = img.get_attribute("style")
			self.img_url = self.img_atrb[23:113]
			self.images.append(self.img_url)
		j = 2
		for i in range(-1, 3):
			urllib.request.urlretrieve(self.images[i], self.title + "/" + f"{self.title}{str(j)}" +".jpg")
			j += 5

		time.sleep(2)
		self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/button').click()
		time.sleep(2)
		try:
			nin = self.driver.find_element_by_class_name('image_1swebtw-o_O-imageLoaded_zgbg08')
			urllib.request.urlretrieve(nin, self.title + "/" + f"{self.title}{str(j)}" +".jpg")
		except Exception as e:
			pass
		time.sleep(2)

		self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/button[2]').click()


		self.images = []
		self.thumbnail = self.driver.find_elements_by_class_name('thumbnail_199fmdb')
		for img in self.thumbnail:
			self.img_atrb = img.get_attribute("style")
			self.img_url = self.img_atrb[23:113]
			self.images.append(self.img_url)
		
		j = 2
		for i in range(-1, 3):
			urllib.request.urlretrieve(self.images[i], self.title + "/" + f"{self.title}{str(j)}" +".jpg")
			j += 1



download = Download('https://brooklyngroup.com/apartment/A8991f')
download.link_download()
download.idk()
