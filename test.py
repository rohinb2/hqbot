import json
from choose_option import *

def test(filename):
    tests = None
    if filename:
        with open(filename, 'r') as f:
            tests = json.load(f)
    right = 0
    count = 0
    for test in tests:
        print(test)
        count += 1
        response = choose_option(test["question"], test["options"])
        #compare answer to first key in response
        if test["answer"].lower() == response[0][0]:
            right += 1

    print(right/float(count))

if __name__ == "__main__":
    test("test.json")
