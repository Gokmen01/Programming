# install xmltodict
import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontent = myXMLFile.read()
        return xmltodict.parse(filecontent)

artikelen = processXML(filename)
