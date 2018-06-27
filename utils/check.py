import re


def is_mobile_num(mobile_str):
    phone = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    match = phone.match(mobile_str)

    return match
