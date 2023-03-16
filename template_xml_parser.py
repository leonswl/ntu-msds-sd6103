# This program defines a custom DBLPSAXHandler class that inherits from xml.sax.ContentHandler. The startElement, characters, and endElement methods are overridden to extract the data we are interested in from the XML document.

# The make_parser function creates an instance of the default XMLReader class, which we then configure to turn off namespace handling and use our custom content handler. We then open the URL using the urllib module, read the XML data, and pass it to the parse method of the XMLReader instance.

# Finally, we print the extracted data to the console. Note that the DBLPSAXHandler class assumes that the XML document has exactly one article element, which may not always be the case. In practice, you may need to modify the code to handle multiple articles or other variations in the input data.

import xml.sax

class DBLPSAXHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.authors = []
        self.title = ""
        self.year = ""
        self.pages = ""

    def startElement(self, tag, attributes):
        self.current_tag = tag

    def characters(self, content):
        if self.current_tag == "author":
            self.authors.append(content.strip())
        elif self.current_tag == "title":
            self.title = content.strip()
        elif self.current_tag == "year":
            self.year = content.strip()
        elif self.current_tag == "pages":
            self.pages = content.strip()

    def endElement(self, tag):
        self.current_tag = ""

# create an XMLReader
parser = xml.sax.make_parser()

# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
handler = DBLPSAXHandler()
parser.setContentHandler(handler)
