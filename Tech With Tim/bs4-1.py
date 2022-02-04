from bs4 import BeautifulSoup as bu
import requests as re
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
result = re.get(url)
doc = bu(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent()
print(parent)
print(parent[1].string)