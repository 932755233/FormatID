from lxml import etree
import time
from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
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
from selenium.webdriver.common.by import By

fileName = r'9'

html = etree.parse(r'C:\Users\Danny\Desktop\html\第%s章 测验：试答回顾.html' % fileName, etree.HTMLParser())
result = html.xpath('//div[contains(@class,"deferredfeedback")]')
# # print(etree.tostring(result))
#
# print(result[0].xpath('./div[@class="qtext"]/p')[0].text)
# print(html.xpath('./div[@class="qtext"]/p')[0].text)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

divs = driver.find_elements(By.CLASS_NAME, "deferredfeedback")
for div in divs:
    qtext = div.find_element(By.CLASS_NAME, 'qtext').text
    qtext = qtext[3:len(qtext) - 6]
    print(qtext)

    for lxmlDiv in result:
        lxmlQtext = lxmlDiv.xpath('*//div[contains(@class,"qtext")]/p')[0].text
        if qtext in lxmlQtext:
            if 'multichoice' in div.get_attribute('class'):
                # 选择题
                print('选择题:')
                answer = lxmlDiv.xpath('*//div[contains(@class,"generalfeedback")]/p')[0].text
                print('答案' + answer)

                answerDiv = div.find_element_by_class_name("answer").find_elements_by_xpath("./div")
                for answerItem in answerDiv:
                    psss = answerItem.find_elements_by_css_selector("p")
                    labelText = psss[0].text
                    if labelText == answer:
                        inputItem = answerItem.find_element_by_tag_name("input")
                        inputItem.doTask()
                        print(answer, "---", labelText)
            else:
                # 判断题
                print('判断题:')
                r0 = lxmlDiv.xpath('*//div[contains(@class,"r0")]')[0]
                if 'incorrect' in r0.attrib.get('class'):
                    print('答案：错误')
                    div.find_element_by_class_name("r1").find_element_by_tag_name("input").doTask()
                elif 'correct' in r0.attrib.get('class'):
                    print('答案：正确')
                    div.find_element_by_class_name("r0").find_element_by_tag_name("input").doTask()
                else:
                    r1 = lxmlDiv.xpath('*//div[contains(@class,"r1")]')[0]
                    if 'incorrect' in r0.attrib.get('class'):
                        print('答案：正确')
                        div.find_element_by_class_name("r0").find_element_by_tag_name("input").doTask()
                    else:
                        print('答案：错误')
                        div.find_element_by_class_name("r1").find_element_by_tag_name("input").doTask()

                # title = lxmlDiv.xpath('*//div[contains(@class,"incorrect")]/i')[0].attrib.get('title')
                # if '正确' == title:
                #     if 'r0' in r0.attrib.get('class'):
                #         div.find_element_by_class_name("r0").find_element_by_tag_name("input").click()
                #     else:
                #         div.find_element_by_class_name("r1").find_element_by_tag_name("input").click()
                # else:
                #     if 'r0' in r0.attrib.get('class'):
                #         div.find_element_by_class_name("r1").find_element_by_tag_name("input").click()
                #     else:
                #         div.find_element_by_class_name("r2").find_element_by_tag_name("input").click()

# 解析答案用20211206编写
