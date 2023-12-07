import matplotlib

from service import GetLocalVisitorCountService as local
from service import GetOverseasVisitorCountService as overseas
from service import CreateGraphService as graph
from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


driver = webdriver.Chrome()

beforeOne = local.execute(driver, 201901, 201903)
beforeTwo = local.execute(driver, 201904, 201906)
beforeThree = local.execute(driver, 201907, 201909)

afterOne = local.execute(driver, 202301, 202303)
afterTwo = local.execute(driver, 202304, 202306)
afterThree = local.execute(driver, 202307, 202309)

driver.close()

overseasBeforeOne = {}
overseasBeforeTwo = {}
overseasBeforeThree = {}
overseasAfterOne = {}
overseasAfterTwo = {}
overseasAfterThree = {}

japan = overseas.execute('Asia', '일본')
overseas.addInDict(japan, '일본', overseasBeforeOne, overseasBeforeTwo, overseasBeforeThree, overseasAfterOne,
                   overseasAfterTwo, overseasAfterThree)

thailand = overseas.execute('Asia', '태국')
overseas.addInDict(thailand, '태국', overseasBeforeOne, overseasBeforeTwo, overseasBeforeThree, overseasAfterOne,
                   overseasAfterTwo, overseasAfterThree)

vietnam = overseas.execute('Asia', '베트남')
overseas.addInDict(vietnam, '베트남', overseasBeforeOne, overseasBeforeTwo, overseasBeforeThree, overseasAfterOne,
                   overseasAfterTwo, overseasAfterThree)

philippines = overseas.execute('Asia', '필리핀')
overseas.addInDict(philippines, '필리핀', overseasBeforeOne, overseasBeforeTwo, overseasBeforeThree, overseasAfterOne,
                   overseasAfterTwo, overseasAfterThree)

usa = overseas.execute('America', '미국')
overseas.addInDict(usa, '미국', overseasBeforeOne, overseasBeforeTwo, overseasBeforeThree, overseasAfterOne,
                   overseasAfterTwo, overseasAfterThree)

print(beforeOne)
print(beforeTwo)
print(beforeThree)

print(afterOne)
print(afterTwo)
print(afterThree)

fig, ax = plt.subplots(3, 2, figsize=(12, 15))

graph.createStickGraph(ax, 0, 0, beforeOne, afterOne, '국내 1분기', 17)
graph.createStickGraph(ax, 1, 0, beforeTwo, afterTwo, '국내 2분기', 17)
graph.createStickGraph(ax, 2, 0, beforeThree, afterThree, '국내 3분기', 17)

graph.createStickGraph(ax, 0, 1, overseasBeforeOne, overseasAfterOne, '해외 1분기', 5)
graph.createStickGraph(ax, 1, 1, overseasBeforeTwo, overseasAfterTwo, '해외 2분기', 5)
graph.createStickGraph(ax, 2, 1, overseasBeforeThree, overseasAfterThree, '해외 3분기', 5)

plt.tight_layout()
plt.show()
