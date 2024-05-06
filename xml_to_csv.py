# import pandas as pd
#
# val = pd.read_xml('ip_vuln.xml', xpath=".//HOST")
#        # .to_csv('Asset_list.csv', sep=',', index=None, header=True)
# print(val)

import xml.etree.ElementTree as ET

xml_file_path = 'ip_vuln.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()
tree = ET.ElementTree(root)
for child in root:
        mainlevel = child.tag
        xmltocsv = ''
        print(mainlevel)
        for elem in root.iter():
            if elem.tag == root.tag:
                continue
            if elem.tag == mainlevel:
                xmltocsv = xmltocsv + '\n'
            xmltocsv = xmltocsv + str(elem.tag).rstrip() + str(elem.attrib).strip() + ';' + str(elem.text).rstrip() + ';'
print(xmltocsv)
