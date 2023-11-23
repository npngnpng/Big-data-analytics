from service import GetLocalVisitorCountService
from selenium import webdriver

driver = webdriver.Chrome()

beforeOne = GetLocalVisitorCountService.execute(driver, 201901, 201903)
beforeTwo = GetLocalVisitorCountService.execute(driver, 201904, 201906)
beforeThree = GetLocalVisitorCountService.execute(driver, 201907, 201909)
beforeFour = GetLocalVisitorCountService.execute(driver, 201910, 201912)

afterOne = GetLocalVisitorCountService.execute(driver, 202301, 202303)
afterTwo = GetLocalVisitorCountService.execute(driver, 202304, 202306)
afterThree = GetLocalVisitorCountService.execute(driver, 202307, 202309)
afterFour = GetLocalVisitorCountService.execute(driver, 202310, 202310)


print(beforeOne)
print(beforeTwo)
print(beforeThree)
print(beforeFour)

print(afterTwo)
print(afterThree)
print(afterFour)
print(afterOne)
print(afterTwo)
print(afterThree)
print(afterFour)

driver.close()
