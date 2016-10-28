from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", middlename="", lastname="", company="", homephone="",
                    mobilephone="", workphone="", email="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename",20),
            lastname=random_string("lastname", 20), company=random_string("company", 20),
                           homephone=("homephone", 20), mobilephone=("mobilephone",20),
            workphone=("workphone", 20), email=("email",20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))