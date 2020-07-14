import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

data = ""
for i in range(1, 6):
    driver = webdriver.Chrome()
    driver.get("https://www.barchart.com/options/most-active/stocks?page={}".format(i))
    text = driver.find_element_by_class_name("bc-datatable").text
    text = text.replace('''Symbol
Name Last Change %Chg Options Vol. % Put Options % Call Options Put/Call Time Links''', '')
    text = text.replace('Symbol Name Last Change %Chg Options Vol. % Put Options % Call Options Put/Call Time Links', '')
    driver.close()
    data += text

data = data.split('\n')
data = [item for item in data if item != '' and item[:2] != '<<' and item[:7] != 'Showing' and item[:5] != '1 2 3']

header = ['Symbol', 'Name',	'Last',	'Change', '%Chg', 'Options Vol.', '% Put Options', '% Call Options', 'Put/Call', 'Time']
with open('result.csv', "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    for i in range(0, len(data), 10):
        writer.writerow(data[i: i + 10])


