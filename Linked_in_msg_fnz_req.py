
# Importing Important Modules

from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time

#  Send url request & create instance of web driver

driver = webdriver.Chrome(executable_path='C:\\Users\Khushi Raj\Desktop\driver\chromedriver')
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('******@gmail.com')
time.sleep(2)
driver.find_element_by_id('password').send_keys('*********')
driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button").click()
driver.find_element_by_xpath("//*[@id='mynetwork-nav-item']/a").click()  # click on Mynetwork link to find All new Friend's
page_soup = soup(driver.page_source, 'lxml')
time.sleep(10)


def send_msg():
    try:
        driver.find_element_by_class_name('mn-community-summary__sub-section').click()

        for i in range(0, 4):
            driver.execute_script(
                "window.scrollBy(0, document.body.scrollHeight)")  # Scroll multiple times to get all li list for friends
            time.sleep(2)  # sleep and again scroll to generate all li

        page_soup_1 = soup(driver.page_source, 'lxml')
        time.sleep(5)
        frnd_lst = page_soup_1.findAll('div', attrs={'class': 'mn-connection-card__details'})
        time.sleep(5)        
        i = 1
        msg_sent_lst = []
        for req in frnd_lst:
            try:
                page_soup_1 = soup(driver.page_source, 'lxml')
                time.sleep(10)
                clk_msg_path = '/html/body/div[6]/div[4]/div[3]/div/div/div/div/div/div/div/div/section/ul/li[' + str(i) + ']/div/div[2]/div/button'
                driver.find_element_by_xpath(clk_msg_path).click()
                time.sleep(5)
                try:
                    msg_box_xpath = '/html/body/div[6]/div[4]/aside/div[2]/div[1]/form/div[2]/div/div[1]/div[1]/p'
                    msg_txt = "Hi, \n It's Raju .... "
                    driver.find_element_by_xpath(msg_box_xpath).send_keys(msg_txt)
                except Exception:
                    msg_box_xpath = '/html/body/div[6]/div[4]/aside/div[2]/div[1]/form/div[3]/div/div[1]/div[1]/p'
                    msg_txt = "Hi, \n It's Raju .... "
                    driver.find_element_by_xpath(msg_box_xpath).send_keys(msg_txt)

                snd_btn_xpath = '/html/body/div[6]/div[4]/aside/div[2]/div[1]/form/footer/div[2]/div[1]/button'
                chk_btn = driver.find_element_by_xpath(snd_btn_xpath)
                if chk_btn.is_enabled():
                    chk_btn.click()
                    print("msg sent")
                    # msg_url = req.find('a')['href']    # not working so use the next step one
                    msg_url = req.contents[1].attrs['href']
                    full_msg_url = 'https://www.linkedin.com' + msg_url
                    name = req.find('span', attrs={'class': 'mn-connection-card__name t-16 t-black t-bold'}).text.strip()
                    msg_sent_lst.append({'NAME': name, 'URL': full_msg_url})
                    i += 1

            except Exception:
                i += 1
                pass            

    except Exception:
        print("Very First Error on Finding Friends")


def send_frnd_req():
    fnd_lst = page_soup.find('ul', attrs={'class': 'js-discover-entity-list__pymk discover-entity-list ember-view'}).findAll('li')
    j = 1
    lst = []
    for req in fnd_lst[j - 1:]:
        try:
            xpath_to_add_fnz = '/html/body/div[5]/div[5]/div[4]/div/div/div/div/div/div/div[2]/section/section/ul/li[' + str(j) + ']/div/section/div[2]/footer/button'
            driver.find_element_by_xpath(xpath_to_add_fnz).click()
            try:
                alert = driver.switch_to_alert().accept()
                print("Aleart found")
                break
            except Exception:
                clk_url = req.find('a')['href']
                final_url = 'https://www.linkedin.com' + clk_url
                lst.append(final_url)
                print(str(j) + '.  Friend request is sent for URL :  ' + final_url)
                j += 1

        except Exception:
            j += 1
            pass


def main():
    send_frnd_req()
    send_msg()


if __name__ == '__main__':
    main()
