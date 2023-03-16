# Script to parse XML file

import xml.sax
import csv
# import os



class DblpHandler (xml.sax.ContentHandler):
    """
    SAX parser to handle xml data
    """
    def __init__(self):
        self._charBuffer = []
        self._result = []

    def _getCharacterData(self):
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        print(data)
        return data #remove strip() if whitespace is important

    # call the parse method on an XML file
    def parse(self, f):
        xml.sax.parse(f, self)
        return self._result

     # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'dblp':
            self._result.append({})

    # Handle endElement
    def endElement(self, tagName):
        if tagName != 'dblp':
            print('start')
            print(tagName)
            print(self._result)
            self._result[-1][tagName] = self._getCharacterData()
            print(f'startElement: {self._result}')
            print('end')


    # Call when a character is read
    def characters(self, content):
        self._charBuffer.append(content)
        
    # Handle startDocument
    def startDocument(self):
        print('About to start!')

    # Handle endDocument
    def endDocument(self):
        print('Finishing up!')


##Write data to CSV file
def csvWriter(fileName):
	global rowsList
	
	set(map(tuple, rowsList))
	
	with open(fileName, 'wb') as fileHandle:
		wr =  csv.writer(fileHandle, dialect='excel')
		wr.writerow(['author', 'title', 'pages', 'year', 'volume', 'number', 'Extra Info', 'Product', 'State'])
		for row in rowsList:
			wr.writerow(list(row))


def main():

    # create a new content handler for the SAX parser
    handler = DblpHandler().parse('test.xml')
    print(handler)

    # when we're done, print out some interesting results
    print('Completed parsing')

if __name__ == '__main__':
    main()

