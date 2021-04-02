# coding=utf-8
import xml.sax

class DataCodeBean:
    id = ''
    code0 = ''
    code1 = ''
    code2 = ''
    code3 = ''


class MovieHandler(xml.sax.handler.ContentHandler):

    def startDocument(self):
        super().startDocument()

    def startElement(self, name, attrs):
        super().startElement(name, attrs)
        if name == 'Data':
            value = attrs['code']
            print(value)

    def characters(self, content):
        super().characters(content)

    def endElement(self, name):
        super().endElement(name)

    def endDocument(self):
        super().endDocument()


if __name__ == '__main__':
    handler = MovieHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('In_Data_20210225013816.xml')
