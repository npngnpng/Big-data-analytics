# //*[@id="content"]/div/div[2]/table/tbody/tr[1]/td[4]/a/img
import pandas as pd
from pandas import DataFrame


def getCounts(country: str, startIndex: int, file: DataFrame):
    count = [0, 0, 0, 0]
    # countryCount
    ind = 0
    for i in range(12):
        count[ind] += file.loc[startIndex + i][country]
        if (i + 1) % 3 == 0:
            ind += 1

    return count


def execute(continent: str, country: str):
    file = pd.read_excel(r'/Users/gilgeunwoo/Desktop/overseas.xlsx', engine='openpyxl', sheet_name=continent, header=1)

    beforeCount = getCounts(country, 181, file)
    afterCount = getCounts(country, 229, file)

    return {'before': beforeCount, 'after': afterCount}


def addInDict(
        country: dict[str, list[int]],
        name: str,
        beforeOne: dict,
        beforeTwo: dict,
        beforeThree: dict,
        afterOne: dict,
        afterTwo: dict,
        afterThree: dict
):
    beforeOne[name] = country.get('before')[0]
    beforeTwo[name] = country.get('before')[1]
    beforeThree[name] = country.get('before')[2]
    afterOne[name] = country.get('after')[0]
    afterTwo[name] = country.get('after')[1]
    afterThree[name] = country.get('after')[2]