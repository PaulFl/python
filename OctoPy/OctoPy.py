from octorest import OctoRest

files = []

url = "http://baulne.paulf.tk:5002"
api_key = "CC9AFBA1A56747029B3BCD7C6E3AA60E"

ender3 = OctoRest(url=url, apikey=api_key)


def retrieve_files():
    return ender3.files()['files']


def order_files_type(files):
    return sorted(files, key=lambda i: i['type'])

