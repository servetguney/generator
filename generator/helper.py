import ipaddress
from pathlib import Path


def get_last(mip:ipaddress):
    return int(str(mip).split('.')[3])

def get_third(mip:ipaddress):
    return str(".").join(items for items in str(mip).split('.')[0:3])
