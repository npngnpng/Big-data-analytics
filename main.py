from service import GetLocalVisitorCountService as local
from service import GetOverseasVisitorCountService as overseas
from selenium import webdriver

driver = webdriver.Chrome()

beforeOne = local.execute(driver, 201901, 201903)
beforeTwo = local.execute(driver, 201904, 201906)
beforeThree = local.execute(driver, 201907, 201909)

afterOne = local.execute(driver, 202301, 202303)
afterTwo = local.execute(driver, 202304, 202306)
afterThree = local.execute(driver, 202307, 202309)

driver.close()

japan = overseas.execute('Asia', '일본')
overseas.addInDict(japan, '일본', beforeOne, beforeTwo, beforeThree, afterOne, afterTwo, afterThree)

thailand = overseas.execute('Asia', '태국')
overseas.addInDict(thailand, '태국', beforeOne, beforeTwo, beforeThree, afterOne, afterTwo, afterThree)

vietnam = overseas.execute('Asia', '베트남')
overseas.addInDict(vietnam, '베트남', beforeOne, beforeTwo, beforeThree, afterOne, afterTwo, afterThree)

philippines = overseas.execute('Asia', '필리핀')
overseas.addInDict(philippines, '필리핀', beforeOne, beforeTwo, beforeThree, afterOne, afterTwo, afterThree)

usa = overseas.execute('America', '미국')
overseas.addInDict(usa, '미국', beforeOne, beforeTwo, beforeThree, afterOne, afterTwo, afterThree)

print(beforeOne)
print(beforeTwo)
print(beforeThree)

print(afterOne)
print(afterTwo)
print(afterThree)