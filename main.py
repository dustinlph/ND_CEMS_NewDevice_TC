# coding = utf-8
import os
import csv
import sys
import json
from enum import Enum

MODEL = "Mitsubishi_M8FM-Series"
SCOPES: list = ["instanceElectricity", "normalUsage", "reverseUsage"]

testplan_path: str = os.path.join(os.getcwd(), 'testcases.json')
list_testcases: list = []
csv_title_list: list = ["Product", "Category", "Summary", "Text"]


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
                testplan["tc"][tc]["title"].format(model=MODEL, scope=s),testplan["tc"][tc]["content"].format(model=MODEL, scope=s)
                ]
            )
    return list_testcases


def create_csv(testcase: list):
    with open(f"testcase/CEMS_NewDevice_TC_{MODEL}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for tc in testcase:
            writer.writerow(tc)


if __name__ == '__main__':
    result = execute(SCOPES)
    create_csv(result)
    print("DONE")

