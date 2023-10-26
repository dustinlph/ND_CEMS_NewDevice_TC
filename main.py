# coding = utf-8
import os
import csv
import sys
import json
from enum import Enum
"""
func options: get, set, once
*note: once -> get once
"""
testplan_path: str = os.path.join(os.getcwd(), 'testcases.json')
list_testcases: list = []
csv_title_list: list = ["Product", "Category", "Summary", "Text"]
model = "Huawei_SmartLogger"
list_scope = ["storedElectricityPrecent", "generatedElectricity"]


def execute(scope: list):
    list_testcases.append(csv_title_list)
    
    with open(testplan_path, encoding="utf-8") as file:
        testplan = file.read()
    file.close()
    testplan: dict = json.loads(testplan)

    for s in scope:
        for tc in range(len(testplan["tc"])):
            list_testcases.append(
                [
                testplan["project"],testplan["tc"][tc]["category"],
                testplan["tc"][tc]["title"].format(model=model, scope=s),testplan["tc"][tc]["content"].format(model=model, scope=s)
                ]
            )
    return list_testcases


def create_csv(testcase: list):
    print(type(testcase))
    with open(f"testcase/CEMS_NewDevice_TC_{model}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for tc in testcase:
            writer.writerow(tc)


if __name__ == '__main__':
    result = execute(list_scope)
    create_csv(result)
    # print(testplan_path)
    #print(result)
