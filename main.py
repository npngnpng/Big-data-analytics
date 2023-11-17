from service import GetLocalVisitorCountService
from selenium import webdriver

driver = webdriver.Chrome()

afterOne = GetLocalVisitorCountService.execute(driver, 202301, 202303)
afterTwo = GetLocalVisitorCountService.execute(driver, 202304, 202306)
afterThree = GetLocalVisitorCountService.execute(driver, 202307, 202309)
afterFour = GetLocalVisitorCountService.execute(driver, 202310, 202310)

print(afterOne)
print(afterTwo)
print(afterThree)
print(afterFour)

driver.close()
