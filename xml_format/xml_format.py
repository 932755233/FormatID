# coding=utf-8
import xml.sax
import xml.sax.handler


class MyHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.index = ''
        self.isStart = 0
        self.zhushi = {'': ''}

    def startElement(self, name, attrs):
        # print(name,attrs["android:layout_width"])
        if name == "androidx.constraintlayout.widget.ConstraintLayout":
            print("ConstraintLayout开始")
            self.isStart = 1
            return
        if name == "androidx.constraintlayout.widget.Barrier":
            print("Barrier开始")
            self.isStart = 2
            return

        if self.isStart == 1:
            try:
                self.zhushi[attrs["android:id"][5:]] = attrs["android:text"]
            except KeyError:
                print(name)
        elif self.isStart == 2:
            print("@ViewById(R.id.%s)" % attrs["android:id"][5:])
            try:
                print(name, "%s; //%s" % (attrs["android:id"][5:], self.zhushi[attrs["app:layout_constraintBaseline_toBaselineOf"][4:]]))
            except KeyError:
                print(name, " %s; //%s" % (attrs["android:id"][5:], self.zhushi[attrs["app:layout_constraintBottom_toBottomOf"][4:]]))


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MyHandler()
    parser.setContentHandler(Handler)
    parser.parse(r'G:\work\petshop\centre\src\main\res\layout\layout_allot_order_form.xml')
