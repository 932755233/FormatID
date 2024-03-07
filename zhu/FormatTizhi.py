import random


class FormatTizhi:
    # 一年级
    # 二年级
    yifeihuoliangStart = 1360
    yifeihuoliangEnd = 1650
    yifeihuoliangStartNv = 1100
    yifeihuoliangEndNv = 1300

    # 这里需要标准乘以十
    yimi50Start = 90
    yimi50End = 106
    yimi50StartNv = 108
    yimi50EndNv = 114

    # 这里需要标准乘以十
    yizuoweitiStart = 73
    yizuoweitiEnd = 106
    yizuoweitiStartNv = 70
    yizuoweitiEndNv = 133

    yiyifenzhongStart = 67
    yiyifenzhongEnd = 95
    yiyifenzhongStartNv = 76
    yiyifenzhongEndNv = 97

    # 三年级
    # 四年级

    sanfeihuoliangStart = 1540
    sanfeihuoliangEnd = 2150
    sanfeihuoliangStartNv = 1100
    sanfeihuoliangEndNv = 1500

    # 这里需要标准乘以十
    sanmi50Start = 95
    sanmi50End = 103
    sanmi50StartNv = 95
    sanmi50EndNv = 101

    # 这里需要标准乘以十
    sanzuoweitiStart = 69
    sanzuoweitiEnd = 98
    sanzuoweitiStartNv = 99
    sanzuoweitiEndNv = 132

    sanyifenzhongStart = 76
    sanyifenzhongEnd = 115
    sanyifenzhongStartNv = 88
    sanyifenzhongEndNv = 127

    sanyangwoStart = 28
    sanyangwoEnd = 35
    sanyangwoStartNv = 26
    sanyangwoEndNv = 37

    # 五年级
    # 六年级

    feihuoliangStart = 2300
    feihuoliangEnd = 2750
    feihuoliangStartNv = 1920
    feihuoliangEndNv = 2200

    # 这里需要标准乘以十
    mi50Start = 86
    mi50End = 90
    mi50StartNv = 90
    mi50EndNv = 96

    # 这里需要标准乘以十
    zuoweitiStart = 51
    zuoweitiEnd = 90
    zuoweitiStartNv = 96
    zuoweitiEndNv = 129

    yifenzhongStart = 128
    yifenzhongEnd = 147
    yifenzhongStartNv = 129
    yifenzhongEndNv = 159

    yangwoStart = 35
    yangwoEnd = 45
    yangwoStartNv = 33
    yangwoEndNv = 42

    wangfanStart = 133
    wangfanEnd = 145
    wangfanStartNv = 149
    wangfanEndNv = 155

    def getBean(self, nianji, xinbie):
        bean = {}
        bean["feihuoliang"] = ''
        bean["mi50"] = ''
        bean["zuoweiti"] = ''
        bean["yifenzhong"] = ''
        bean["yangwo"] = ''
        bean["wangfan"] = ''
        if nianji == '12' or nianji == '11':
            if xinbie == '1':
                # 男的
                bean["feihuoliang"] = str(random.randint(self.yifeihuoliangStart, self.yifeihuoliangEnd))
                bean["mi50"] = str(random.randint(self.yimi50Start, self.yimi50End))
                bean["zuoweiti"] = str(random.randint(self.yizuoweitiStart, self.yizuoweitiEnd))
                bean["yifenzhong"] = str(random.randint(self.yiyifenzhongStart, self.yiyifenzhongEnd))
            else:
                # 女的
                bean["feihuoliang"] = str(random.randint(self.yifeihuoliangStartNv, self.yifeihuoliangEndNv))
                bean["mi50"] = str(random.randint(self.yimi50StartNv, self.yimi50EndNv))
                bean["zuoweiti"] = str(random.randint(self.yizuoweitiStartNv, self.yizuoweitiEndNv))
                bean["yifenzhong"] = str(random.randint(self.yiyifenzhongStartNv, self.yiyifenzhongEndNv))
        elif nianji == '13' or nianji == '14':
            if xinbie == '1':
                # 男的
                bean["feihuoliang"] = str(random.randint(self.sanfeihuoliangStart, self.sanfeihuoliangEnd))
                bean["mi50"] = str(random.randint(self.sanmi50Start, self.sanmi50End))
                bean["zuoweiti"] = str(random.randint(self.sanzuoweitiStart, self.sanzuoweitiEnd))
                bean["yifenzhong"] = str(random.randint(self.sanyifenzhongStart, self.sanyifenzhongEnd))
                bean["yangwo"] = str(random.randint(self.sanyangwoStart, self.sanyangwoEnd))
            else:
                # 女的
                bean["feihuoliang"] = str(random.randint(self.sanfeihuoliangStartNv, self.sanfeihuoliangEndNv))
                bean["mi50"] = str(random.randint(self.sanmi50StartNv, self.sanmi50EndNv))
                bean["zuoweiti"] = str(random.randint(self.sanzuoweitiStartNv, self.sanzuoweitiEndNv))
                bean["yifenzhong"] = str(random.randint(self.sanyifenzhongStartNv, self.sanyifenzhongEndNv))
                bean["yangwo"] = str(random.randint(self.sanyangwoStartNv, self.sanyangwoEndNv))
        elif nianji == '15' or nianji == '16':
            if xinbie == '1':
                # 男的
                bean["feihuoliang"] = str(random.randint(self.feihuoliangStart, self.feihuoliangEnd))
                bean["mi50"] = str(random.randint(self.mi50Start, self.mi50End))
                bean["zuoweiti"] = str(random.randint(self.zuoweitiStart, self.zuoweitiEnd))
                bean["yifenzhong"] = str(random.randint(self.yifenzhongStart, self.yifenzhongEnd))
                bean["yangwo"] = str(random.randint(self.yangwoStart, self.yangwoEnd))
                bean["wangfan"] = str(random.randint(self.wangfanStart, self.wangfanEnd))
            else:
                # 女的
                bean["feihuoliang"] = str(random.randint(self.feihuoliangStartNv, self.feihuoliangEndNv))
                bean["mi50"] = str(random.randint(self.mi50StartNv, self.mi50EndNv))
                bean["zuoweiti"] = str(random.randint(self.zuoweitiStartNv, self.zuoweitiEndNv))
                bean["yifenzhong"] = str(random.randint(self.yifenzhongStartNv, self.yifenzhongEndNv))
                bean["yangwo"] = str(random.randint(self.yangwoStartNv, self.yangwoEndNv))
                bean["wangfan"] = str(random.randint(self.wangfanStartNv, self.wangfanEndNv))

        return bean
