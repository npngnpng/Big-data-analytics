def execute(before: dict, after: dict):
    increaseList = {}

    for k in before.keys():
        increaseList[k] = (after[k] - before[k]) / before[k] * 100

    return increaseList
