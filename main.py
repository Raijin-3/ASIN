import pandas
from selenium import webdriver
import time
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning) 


URL = "https://www.amazon.com/"

#setting up selenium chrome driver
chrome_driver_path = "E:\\Python\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)
     
result_dict = {'asin':[], 'result':[]}
#getting the asin number from local file
file = pandas.read_csv('file.csv')
file_dict = file.to_dict(orient='records')
for item in file_dict:
    asin_no = item['asin']
    driver.get(URL)
    search_bar = driver.find_element_by_id('twotabsearchtextbox')
    search_bar.send_keys(asin_no)
    search_bar.send_keys(u'\ue007')
    time.sleep(3)
    data = driver.find_elements_by_class_name('a-section')
    print(driver.current_url)
    
    
    content = []
    for item in data:
        content.append(item.text)    
        
     
    if content[0] == f"""1 result for {'"'}{asin_no}{'"'}""":
        i = asin_no
        j = "Item available"
        if not result_dict:
            result_dict = {
            "asin": i,
            "result":j
        }
        else:
            result_dict["asin"].append(i)
            result_dict["result"].append(j)
    
        
    else:
        i = asin_no
        j = "Not Searchable"
        if not result_dict:
            result_dict = {
            "asin": i,
            "result":j
        }
        else:
            result_dict["asin"].append(i)
            result_dict["result"].append(j)
    

print(result_dict)
df = pandas.DataFrame.from_dict(result_dict, orient="index")
df.to_csv("result.csv")




driver.quit()