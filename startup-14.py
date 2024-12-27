import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

df = pd.read_csv('seed8888.csv')

sf = Service("C:/Users/HP/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=sf)
driver.get("https://seedfund.startupindia.gov.in/")
time.sleep(5)

columns = [
    "Company Name",
    "Company Email",
    "INC-1 NAME",
    "INC-1 STATUS",
    "INC-1 COMMENTS",
    "INC-2 NAME",
    "INC-2 STATUS",
    "INC-2 COMMENTS",
    "INC-3 NAME",
    "INC-3 STATUS",
    "INC-3 COMMENTS"
]

fcom = ""
scom = ""
tcom = ""

fnm =""
snm=""
tnm = ""



fcomment = ""
scomment = ""
tcomment = ""
data = []
count = 1
for index, row in df.iterrows():
    cname = row['Company Name']
    email = row['ID']
    password = row['Password']
    time.sleep(1)
    
    # try:
    # # Identify the modal background element
    #     modal_background = driver.find_element(by=By.CSS_SELECTOR, value=".modal-backdrop.fade.show")

    # # # Click the modal background
    #     modal_background.click()
    # # Click the Login button
    #     # driver.find_element(by=By.XPATH, value='//*[@id="navbarCollapse"]/div/button').click()
        
    # except Exception as e:
    #     print(f"Error: {e}")
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="navbarCollapse"]/div/button').click()
    except :
        time.sleep(10)
        driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/header/nav/div/div[2]/div/button').click()

    time.sleep(1)
    username = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/header/fieldset/div[1]/div/div/div/div/form/fieldset/fieldset/div[2]/div[2]/div[1]/div/input')
    time.sleep(1)
    username.send_keys(email)
    time.sleep(1)

    passs = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/header/fieldset/div[1]/div/div/div/div/form/fieldset/fieldset/div[2]/div[2]/div[2]/div/input')
    time.sleep(1)
    passs.send_keys(password)
    time.sleep(1)
    try: 
        driver.find_element(by=By.XPATH, value='//*[@id="btnLogIn1"]').click()

    except:
        de = pd.DataFrame(data, columns=columns)
        de.to_csv('startupdata3.csv', index=False)
    
    time.sleep(8)
    try:
        driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/header/div[2]/div/div/div/div/button').click()
    
        clicked = True
    except :
        clicked = False
    if clicked == True :
        driver.get("https://seedfund.startupindia.gov.in/")
        continue
    
    time.sleep(3)
    
    try : #in progeress Page    
        first = driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[1]/div[1]').text
        first_split = first.split('\n')
        fsubmit = first_split[1]
        fnm = first_split[0]
        print(first_split)
        if first_split[2]=="VIEW DETAILS":
            driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[1]/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(1)
            try:
                driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span[1]/div[2]/div/table/tbody/tr/td[3]/span').click()
                        
            except Exception as e:
                print(f"Error: {e}")
                
                time.sleep(1)
            fcom =driver.find_element(by=By.XPATH, value='//*[@id="status_comment_0"]').text
            print(fcom)                                                
                    
            fcom_split = fcom.split('\n')

                # fcomment = fcom_split[5]
            fcomment = fcom_split
               # print(first_split)
        time.sleep(1)
                    
        second = driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[2]/div[1]').text
        second_split = second.split('\n')
        ssubmit = second_split[1]
        snm = second_split[0]
        print(second_split)
        if second_split[2]=="VIEW DETAILS":
            driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[2]/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(1)
            try:
                driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span[2]/div[2]/div/table/tbody/tr/td[3]/span').click()
                        
            except Exception as e:
                print(f"Error: {e}")
                
                time.sleep(1)
            scom =driver.find_element(by=By.XPATH, value='//*[@id="status_comment_1"]').text
                
            scom_split = scom.split('\n')
                # scomment = scom_split[5]
            scomment = scom_split
        
        time.sleep(1)
                
        third = driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[3]/div[1]').text
        third_split = third.split('\n')
        tsubmit = third_split[1]
        tnm = third_split[0]
        print(third_split)
        if third_split[2]=="VIEW DETAILS":
            driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[3]/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(1)  
            try:
                driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span[2]/div[2]/div/table/tbody/tr/td[3]/span').click()
                        
            except Exception as e:
                print(f"Error: {e}")
                
                time.sleep(1)
            tcom =driver.find_element(by=By.XPATH, value='//*[@id="status_comment_2"]').text
                
            tcom_split = tcom.split('\n')
                # tcomment = tcom_split[5]
            tcomment = tcom_split
                # print(tcom_split)
        time.sleep(1)
        
    except: # Rejected page     
        time.sleep(2)
    
        
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/fieldset/div/div/div[1]/div/div[1]/ul/li[4]/a').click()
        
        try : 
            first = driver.find_element(by=By.XPATH, value='//*[@id="tab-rejected"]/div/div/span/div[1]').text
            first_split = first.split('\n')
            fsubmit = first_split[1]
            fnm = first_split[0]
            print(first_split)
            if first_split[2]=="VIEW DETAILS":
                driver.find_element(by=By.XPATH, value='//*[@id="tab-rejected"]/div/div/span[1]/div[1]/div[1]/div[2]/div/button').click()
                time.sleep(2)
                try:
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[1]/div[2]/div/table/tbody/tr[1]/td[3]/span').click()
                    
                    except Exception as e:
                        print(f"Error: {e}")
                        
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[1]/div[2]/div/table/tbody/tr[2]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span/div[2]/div/table/tbody/tr[5]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span/div[2]/div/table/tbody/tr[6]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span/div[2]/div/table/tbody/tr[3]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span/div[2]/div/table/tbody/tr[8]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                            
                except Exception as e:
                    print(f"Error: {e}")
                
                time.sleep(1)
                fcom =driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[1]/div[2]').text
                print(fcom)                                                
                    
                fcom_split = fcom.split('\n')

                # fcomment = fcom_split[5]
                fcomment = fcom_split
                # print(first_split)
        except:
            fsubmit = ""
            fnm = ""
            fcom = ""
            # print("except")
        time.sleep(1)
                    
        try:
            second = driver.find_element(by=By.XPATH, value='//*[@id="tab-rejected"]/div/div/span[2]/div[1]').text
            second_split = second.split('\n')
            ssubmit = second_split[1]
            snm = second_split[0]
            print(second_split)
            if second_split[2]=="VIEW DETAILS":
                driver.find_element(by=By.XPATH, value='//*[@id="tab-rejected"]/div/div/span[2]/div[1]/div[1]/div[2]/div/button').click()
                time.sleep(2)
                try:
                    
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[1]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[2]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                        #--------
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[3]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[4]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[5]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")

                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[4]/td[3]/span').click()
                        
                    except  Exception as e:
                        print(f"Error: {e}")
                        
                except Exception as e:
                    print(f"Error: {e}")
                
                time.sleep(1)
                scom =driver.find_element(by=By.XPATH, value='/html/body/div/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]').text
                
                scom_split = scom.split('\n')
                # scomment = scom_split[5]
                scomment = scom_split
                
                # print(scom_split)

        except:
            ssubmit = ""
            snm = ""
            scom = ""
        time.sleep(1)
            
        try:    
            third = driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[3]/div[1]').text
            third_split = third.split('\n')
            tsubmit = third_split[1]
            tnm = third_split[0]
            print(third_split)
            if third_split[2]=="VIEW DETAILS":
                driver.find_element(by=By.XPATH, value='//*[@id="tab-submitted"]/div[2]/div/span[3]/div[1]/div[1]/div[2]/div/button').click()
                time.sleep(2)  
                try:
                    try:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[1]/td[3]/span').click()
                    except:
                        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/fieldset/div/div/div[1]/div/div[2]/div[4]/div/div/span[2]/div[2]/div/table/tbody/tr[3]/td[3]/span').click()
                        
                except Exception as e:
                    print(f"Error: {e}")
                
                time.sleep(1)
                tcom =driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/span[3]/div[2]').text
                
                tcom_split = tcom.split('\n')
                # tcomment = tcom_split[5]
                tcomment = tcom_split
                # print(tcom_split)
                    
                
        except :
            tsubmit = ""
            tnm = ""
            tcom = ""
        time.sleep(1)
    data.append([
        cname,
        email,
        fnm,
        fsubmit,
        fcomment,
        snm,
        ssubmit,
        scomment,
        tnm,
        tsubmit,
        tcomment,
        ])
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/fieldset/fieldset/header/nav/div/div[2]/ul/li/a').click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/fieldset/fieldset/header/nav/div/div[2]/ul/li/div/fieldset/div/a[2]').click()
        time.sleep(1)
    except:
        de = pd.DataFrame(data, columns=columns)
        de.to_csv('startupdata3.csv', index=False)
    count =count+1
    print(count)
    if count ==50:
        break

        
  
de = pd.DataFrame(data, columns=columns)


de.to_csv('startupdata3.csv', index=False)
