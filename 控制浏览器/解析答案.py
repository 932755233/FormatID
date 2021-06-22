from lxml import etree
import time
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(open(r'C:\Users\Danny\Desktop\html\专题测验：试答回顾.html', 'rb'), "lxml")
#
# div = soup.find_all(attrs="deferredfeedback")
# print(div.find_all(attrs="qtext"))

# tree = lxml.html.fromstring(html);
# result = lxml.html.tostring(tree,pretty_print=True); #格式化输出
# print(result)
#
# td = tree.cssselect('tr#places_area__row > td.w2p_fw ')[0]#按节点找
# print(td.text_content())
#
# root = etree.Element("root")
# print(etree.tostring(root))
html = etree.parse(r'C:\Users\Danny\Desktop\html\专题测验：试答回顾.html', etree.HTMLParser())
result = html.xpath('//div[contains(@class,"deferredfeedback")]')
# # print(etree.tostring(result))
#
# print(result[0].xpath('./div[@class="qtext"]/p')[0].text)
# print(html.xpath('./div[@class="qtext"]/p')[0].text)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

div = driver.find_elements_by_class_name("deferredfeedback")
for divv in div:
    qtext = divv.find_elements_by_class_name("qtext")
    for htmlDiv in result:
        htmlDivv = htmlDiv.xpath('./div/div/div[@class="qtext"]/p')
        # print(divv[0].text)
        qText = str(qtext[0].text[3:len(qtext[0].text) - 6])
        pText = str(htmlDivv[0].text)
        ssss = pText.find(qText)
        if qText in pText:
            htmlAnswer = htmlDiv.xpath('./div/div/div/div[@class="rightanswer"]')
            answerText = ''
            if "：" in htmlAnswer[0].text:
                answerText = htmlAnswer[0].text[6:]
            else:
                answerText = htmlAnswer[0].text[6:len(htmlAnswer[0].text) - 2]
            answerDiv = divv.find_element_by_class_name("answer").find_elements_by_xpath("./div")
            for answerItem in answerDiv:
                psss = answerItem.find_elements_by_css_selector("p")
                if len(psss) == 0:
                    pitem = answerItem.find_element_by_tag_name("label")
                else:
                    pitem = answerItem.find_element_by_tag_name("p")
                labelText = pitem.text
                if labelText == answerText:
                    inputItem =answerItem.find_element_by_tag_name("input")
                    inputItem.click()
                    print(pText, "---", labelText)
