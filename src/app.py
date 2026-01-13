import os

def insecure(cmd):
    os.system(cmd)

def insecure(user_input):
    eval(user_input)


API_KEY = "sk_test_1234567890"
