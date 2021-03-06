from selenium import webdriver
from time import sleep

class Instabot:
    def __init__(self, username,pw):
    
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("http://www.instagram.com") 
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)    
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()    
        sleep(5)  
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click() 
        #sleep(3)      
    def get_unfollowers(self): 
        #if we run python file by pyhton -i filename then the selenium file will became interactive and will
        #not be closed even after completion 
       
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)    
        self.driver.find_element_by_xpath("//a[contains(@href,'/following/')]")\
            .click()    
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers/')]")\
            .click()  
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]    
        print(not_following_back)


    def _get_names(self):
        sleep(2)   
        
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a') 
        names = [name.text for name in links if name.text != '']   
        #close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def like_picture(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/B5QyQsblLf7/')]").click()
        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        
        
        


my_bot = Instabot('username','password') 
my_bot.get_unfollowers()
my_bot.like_picture()       