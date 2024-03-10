# !pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  # 수정된 부분

# URL of the theater page
want_date = 20240323
CGV_THEATER_URL = f'http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0013&date={want_date}'  

option = webdriver.ChromeOptions()
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(options=option)
driver.delete_all_cookies()

driver.get(url=CGV_THEATER_URL)
innerIframe = driver.find_element(By.ID, "ifrm_movie_time_table")
driver.switch_to.frame(innerIframe)

# 해당 요소를 찾습니다.
element = driver.find_element(By.CSS_SELECTOR, "#slider > div > ul > li.on > div > a")

# href 속성 값을 가져와서 출력합니다.
href_value = element.get_attribute("href")
date_value = href_value.split("date=")[1].split("&")[0]

# CSS 선택자를 사용하여 날짜 정보를 포함하는 모든 li 요소 찾기
date_elements = driver.find_elements(By.CSS_SELECTOR, "body > div > div.sect-showtimes > ul > li")

if int(date_value) != int(want_date) :
    print(f"{want_date} 헤당 날짜 예약 불가능")
else :
    # 각 li 요소에서 date와 sreader 클래스를 가진 요소를 출력하기
    for date_element in date_elements:
        # date_attribute = date_element.get_attribute("date")
        title_attribute = date_element.find_element(By.CSS_SELECTOR, ".info-movie strong")
       
        if title_attribute == "듄2":
            print(f"{want_date} 에매 가능")
            break
        else:
            print(f"{want_date} 헤당 날짜 예약 불가능")


# 브라우저 닫기
driver.quit()
