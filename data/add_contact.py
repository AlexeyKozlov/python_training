from model.contact import Contact
import random
import string

constant = [Contact(firstname="name1", middlename="mid1", lastname="last1", company="comp1", homephone="home1",
                    mobilephone="mobile1", workphone="work1", email="email1"),
            Contact(firstname="name2", middlename="mid2", lastname="last2", company="comp2", homephone="home2",
                    mobilephone="mobile2", workphone="work2", email="email2"),

            ]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", middlename="", lastname="", company="", homephone="",
                    mobilephone="", workphone="", email="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename",20),
            lastname=random_string("lastname", 20), company=random_string("company", 20),
                           homephone=("homephone", 20), mobilephone=("mobilephone",20),
            workphone=("workphone", 20), email=("email",20))
    for i in range(2)
]


