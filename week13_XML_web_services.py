import xml.etree.ElementTree as ET
data = '''<person>
    <name> Chuck </name>
    <phone type = "intl">
        +1 734 303 24456
    </phone>
    <email hide = "yes"/>
    </person>''' 


tree = ET.fromstring(data)
print('Name:' , tree.find('name').text)
print(tree.find('email').get('hide')) # There is no .text because in email there is only hide attribute













"""import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id> 001 </id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
    </stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('count: ' , len(lst))
for item in lst:
    print('Name: ' , item.find('name').text)
    print('Id: ' , item.find('id').text)
    print('Attribute: ' , item.get('x'))"""
