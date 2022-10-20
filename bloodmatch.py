import requests
import json


def get_info():
    r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jh709")

    q = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M7")

    s = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F1")
    return r.text, q.text, s.text

def check_blood_type(q, s):
    if s == "O-":
        if q == "O-":
            return "Yes"
        else:
            return "No"
    if s == "O+":
        if q == "O-" or "O+":
            return "Yes"
        else:
            return "No"
    if s == "B-":
        if q == "O-" or "B-":
            return "Yes"
        else:
            return "No"
    if s == "B+":
        if q == "O-" or "O+" or "B-" or "B+":
            return "Yes"
        else:
            return "No"
    if s == "A-":
        if q == "O-" or "A-":
            return "Yes"
        else:
            return "No"
    if s == "A+":
        if q == "O-" or "O+" or "A-" or "A+":
            return "Yes"
        else:
            return "No"
    if s == "AB-":
        if q == "O-" or "A-" or "B-" or "AB-":
            return "Yes"
        else:
            return "No"
    if s == "AB+":
        return "Yes"


def dictionary(answer):
    d = {"Name": "jh709",
               "Match": answer}
    return d


def output(d): 
    file = "bloodmatch.json"
    out_file = open(file, 'w')
    json.dump(d, out_file)
    out_file.close()
    a = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=d)
    print(a.text)


def main():
    x, y, z = get_info()
    answer = check_blood_type(y, z)
    d = dictionary(answer)
    output(d)


if __name__ == '__main__':
    main()