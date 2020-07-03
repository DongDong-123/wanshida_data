# -*- coding: utf-8 -*-
# @Time    : 2020-06-24 22:16
# @Author  : liudongyang
# @FileName: Common.py
# @Software: PyCharm
# 公共方法
import random
import time
import redis
from redis_data import RedisConnect
pool = RedisConnect()


class CommonFunction:
    def __init__(self):
        self.rel_sctp = '2'
        self.year = time.strftime("%Y", time.localtime())
        self.month = time.strftime("%m", time.localtime())
        self.day = time.strftime("%d", time.localtime())

    def random_str(self, num):
        words = 'abcdefghijklmnopqrstuvwxyz'
        strs = ''.join(random.choices(words, k=num))
        return strs.capitalize()

    def person_fir_name(self):  # 个人客户first name
        name = self.random_str(random.randint(3,7))
        return name

    # 生成姓名数据
    def make_name_data(self, longth=None):
        first_name = random.choice([
            "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许", "何",
            "吕",
            "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏", "潘",
            "葛",
            "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳", "酆", "鲍", "史", "唐", "费",
            "廉",
            "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常", "乐", "于", "时", "傅", "皮", "卞", "齐",
            "康",
            "伍", "余", "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米",
            "贝",
            "明", "臧", "计", "伏", "成", "戴", "谈", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项", "祝", "董", "粱", "杜", "阮", "蓝",
            "闵",
            "席", "季", "麻", "强", "贾", "路", "娄", "危", "江", "童", "颜", "郭", "梅", "盛", "林", "刁", "钟", "徐", "邱", "骆", "高",
            "夏",
            "蔡", "田", "樊", "胡", "凌", "霍", "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "经", "房", "裘", "缪", "干", "解", "应",
            "宗",
            "丁", "宣", "贲", "邓", "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉", "钮", "龚", "程", "嵇", "邢", "滑", "裴",
            "陆",
            "荣", "翁", "荀", "羊", "於", "惠", "甄", "麴", "家", "封", "芮", "羿", "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富",
            "巫",
            "乌", "焦", "巴", "弓", "牧", "隗", "山", "谷", "车", "侯", "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫", "宁",
            "仇",
            "栾", "暴", "甘", "钭", "厉", "戎", "祖", "武", "符", "刘", "景", "詹", "束", "龙", "叶", "幸", "司", "韶", "郜", "黎", "蓟",
            "薄",
            "印", "宿", "白", "怀", "蒲", "邰", "从", "鄂", "索", "咸", "籍", "赖", "卓", "蔺", "屠", "蒙", "池", "乔", "阴", "欎", "胥",
            "能",
            "苍", "双", "闻", "莘", "党", "翟", "谭", "贡", "劳", "逄", "姬", "申", "扶", "堵", "冉", "宰", "郦", "雍", "舄", "璩", "桑",
            "桂",
            "濮", "牛", "寿", "通", "边", "扈", "燕", "冀", "郏", "浦", "尚", "农", "温", "别", "庄", "晏", "柴", "瞿", "阎", "充", "慕",
            "连",
            "茹", "习", "宦", "艾", "鱼", "容", "向", "古", "易", "慎", "戈", "廖", "庾", "终", "暨", "居", "衡", "步", "都", "耿", "满",
            "弘",
            "匡", "国", "文", "寇", "广", "禄", "阙", "东", "殴", "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩", "厍", "聂", "晁",
            "勾",
            "敖", "融", "冷", "訾", "辛", "阚", "那", "简", "饶", "空", "曾", "毋", "沙", "乜", "养", "鞠", "须", "丰", "巢", "关", "蒯",
            "相",
            "查", "後", "荆", "红", "游", "竺", "权", "逯", "盖", "益", "桓", "公", "万俟", "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方",
            "赫连", "皇甫", "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳", "淳于", "单于", "太叔", "申屠", "公孙", "仲孙", "轩辕", "令狐", "钟离", "宇文",
            "长孙", "慕容", "鲜于", "闾丘", "司徒", "司空", "亓官", "司寇", "仉", "督", "子车", "颛孙", "端木", "巫马", "公西", "漆雕", "乐正", "壤驷",
            "公良",
            "拓跋", "夹谷", "宰父", "谷梁", "晋", "楚", "闫", "法", "汝", "鄢", "涂", "钦", "段干", "百里", "东郭", "南门", "呼延", "归", "海",
            "羊舌",
            "微生", "岳", "帅", "缑", "亢", "况", "后", "有", "琴", "梁丘", "左丘", "东门", "西门", "商", "牟", "佘", "佴", "伯", "赏", "南宫",
            "墨",
            "哈", "谯", "笪", "年", "爱", "阳", "佟", "第五", "言", "福", "卓", "蔺", "屠", "蒙", "池", "乔", "阳", "郁", "胥", "能", "苍",
            "双",
            "闻", "莘", "党", "翟", "谭", "贡", "劳", "逄", "姬", "申", "扶", "堵", "冉", "宰", "郦", "雍", "却", "璩", "桑", "桂", "濮",
            "牛",
            "寿", "通", "边", "扈", "燕", "冀", "僪", "浦", "尚", "农", "温", "别", "庄", "晏", "柴", "瞿", "阎", "充", "慕", "连", "茹",
            "习",
            "宦", "艾", "鱼", "容", "向", "古", "易", "慎", "戈", "庾", "终", "暨", "居", "衡", "步都", "耿", "满", "弘", "匡", "国", "文",
            "寇",
            "广", "禄", "阙", "东欧", "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩", "厍", "聂晁", "勾", "敖", "融", "冷", "訾", "辛",
            "阚",
            "那", "简", "饶", "空曾", "毋", "沙", "乜", "养", "鞠", "须", "丰", "巢", "关", "蒯", "相查", "后", "荆", "红", "游", "竺", "权",
            "逮",
            "盍", "益", "桓", "公", "唱"])
        second_name = random.choice([
            "一", "是", "我", "不", "在", "人", "们", "有", "来", "他", "这", "上", "着", "个", "地", "到",
            "大", "里", "说", "去", "子", "得", "也", "和", "那", "要", "下", "看", "天", "时", "过", "出",
            "小", "么", "起", "你", "都", "把", "好", "还", "多", "没", "为", "又", "可", "家", "学", "只",
            "以", "主", "会", "样", "年", "想", "能", "生", "同", "老", "中", "从", "自", "面", "前", "头",
            "到", "它", "后", "然", "走", "很", "像", "见", "两", "用", "国", "动", "进", "成", "回", "什",
            "边", "作", "对", "开", "而", "已", "些", "现", "山", "民", "候", "经", "发", "工", "向", "事",
            "命", "给", "长", "水", "义", "三", "声", "于", "高", "正", "手", "知", "理", "眼", "志", "点",
            "心", "战", "二", "问", "但", "身", "方", "实", "做", "叫", "当", "住", "听", "革", "打", "呢",
            "真", "党", "全", "才", "四", "已", "所", "敌", "之", "最", "光", "产", "情", "路", "分", "总",
            "条", "白", "话", "东", "席", "次", "亲", "如", "被", "花", "口", "放", "儿", "常", "西", "气",
            "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
            "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
            "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
            "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
            "化", "太", "指", "变", "社", "似", "士", "者", "干", "石", "满", "决", "百", "原", "群",
            "究", "各", "六", "本", "思", "解", "立", "河", "爸", "村", "八", "难", "早", "论", "根",
            "共", "让", "相", "研", "今", "其", "书", "接", "应", "关", "信", "觉", "步", "反", "处",
            "记", "将", "千", "找", "争", "领", "或", "师", "结", "块", "跑", "谁", "草", "越", "字", "加",
            "紧", "爱", "等", "习", "阵", "月", "青", "半", "火", "法", "题", "建", "赶", "位",
            "唱", "海", "七", "任", "件", "感", "准", "张", "团", "屋", "离", "片", "科", "倒", "睛", "利",
            "世", "刚", "且", "由", "送", "切", "星", "晚", "表", "够", "整", "认", "响", "雪", "流", "未",
            "场", "该", "并", "底", "深", "刻", "平", "伟", "忙", "提", "确", "近", "亮", "轻", "讲", "农",
            "古", "黑", "告", "界", "拉", "名", "呀", "土", "清", "阳", "照", "办", "史", "改", "历", "转",
            "画", "造", "嘴", "此", "治", "北", "必", "服", "雨", "穿", "内", "识", "验", "传", "业", "菜", "兴"])
        last_name = random.choice([
            "命", "给", "长", "水", "义", "三", "声", "于", "高", "正", "手", "知", "理", "眼", "志", "点",
            "心", "战", "二", "问", "但", "身", "方", "实", "做", "叫", "当", "住", "听", "革", "打", "呢",
            "真", "党", "全", "才", "四", "已", "所", "敌", "之", "最", "光", "产", "情", "路", "分", "总",
            "条", "白", "话", "东", "席", "次", "亲", "如", "被", "花", "口", "放", "儿", "常", "西", "气",
            "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
            "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
            "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
            "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
            "化", "太", "指", "变", "社", "似", "士", "者", "干", "石", "满", "决", "百", "原", "群",
            "究", "各", "六", "本", "思", "解", "立", "河", "爸", "村", "八", "难", "早", "论", "根",
            "共", "让", "相", "研", "今", "其", "书", "接", "应", "关", "信", "觉", "步", "反", "处",
            "记", "将", "千", "找", "争", "领", "或", "师", "结", "块", "跑", "谁", "草", "越", "字"])
        fouth_name = random.choice([
            "命", "给", "长", "水", "义", "三", "声", "于", "高", "正", "手", "知", "理", "眼", "志", "点",
            "心", "战", "二", "问", "但", "身", "方", "实", "做", "叫", "当", "住", "听", "革", "打", "呢",
            "真", "党", "全", "才", "四", "已", "所", "敌", "之", "最", "光", "产", "情", "路", "分", "总",
            "条", "白", "话", "东", "席", "次", "亲", "如", "被", "花", "口", "放", "儿", "常", "西", "气",
            "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
            "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
            "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
            "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
            "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
            "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
            "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
            "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
            "化", "太", "指", "变", "社", "似", "士", "者", "干", "石", "满", "决", "百", "原", "群",
            "究", "各", "六", "本", "思", "解", "立", "河", "爸", "村", "八", "难", "早", "论", "根",
            "共", "让", "相", "研", "今", "其", "书", "接", "应", "关", "信", "觉", "步", "反", "处",
        ])
        if longth == 4:
            return first_name + second_name + last_name + fouth_name
        else:
            return first_name + second_name + last_name

    def org_name(self):  # 机构客户名称
        name = [self.random_str(random.randint(4,7)) for i in range(random.randint(3,5))]
        return ' '.join(name)

    def relation_type(self):
        """
        关系人类型，个人关系、机构关系，其他
        :return:
        """
        cust_type = ''
        if cust_type == 1:
            relation_type = random.choice([
                "B01",  # 夫妻关系
                "B02",  # 子女
                "B03",  # 父母
                "B04",  # 其他血亲
                "B05",  # 其他姻亲
                "B06",  # 同学
                "B07" ] # 朋友
            )
        elif cust_type == 2:
            relation_type = random.choice([
                "A01",  # 对公客户与法人代表
                "A02",  # 对公客户与联系人
                "A03",  # 对公客户与负责人
                "A04",  # 对公客户与董事
                "A05",  # 对公客户与股东
                "A06",  # 母公司与子公司
                "A07",  # 代理
                "A08",  # 投资与被投资
                "A09",  # 其他关联单位
                "A10",  # 企业团体
                "A11",  # 银行团体
                "A12" ] # 家族企业
            )
        else:
            relation_type = random.choice(
                  ["X",  # 未说明
                "C01"]  # 受益所有人
            )

        return relation_type


    def rel_layer(self):
        layer = random.randint(0,5)
        return layer

    def cert_type(self):  # 证件类型
        if self.rel_sctp == '1':
            cstp = random.choice([
            "11",  # 居民身份证或临时身份证
            "12",  # 军人或武警身份证件
            "13",  # 港澳台通行证
            "14",  # 外国公民护照
            "19"]  # 其他个人有效证件(需进一步说明)
        )
        else:
            cstp = random.choice([
                "21",  # 组织机构代码
                "29"]  # 其他机构代码(需进一步说明)
            )
        return cstp

    def person_cert_num(self):  # 个人证件号码
        ctid = self.random_num(18)

        return ctid

    def org_cert_num(self,num=9):  # 机构证件号码 默认9位数字字母组合
        strs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "0123456789"
        n = random.randint(3,6)
        cert = ''.join(random.choices(strs,k=n)) + ''.join(random.choices(nums, k=(num-n)))
        return cert

    def make_date(self, beg=-3, end=20, length=8):
        """制造 日期相关数据，可随机生成往前、往后的日期数据，默认日期格式yyyymmdd，可通过length设置格式，
        length=10, yyyy-mm-dd,
        """
        # 年
        make_year = int(self.year) + random.randint(beg, end)
        # 月
        make_month = int(self.month) + random.randint(0,11)
        if make_month > 12:
            make_month = make_month % 12

        # 日
        make_day = int(self.day) + random.randint(-5, 10)
        if make_day < 0:
            make_day = -make_day
        elif make_day == 0:
            make_day = 1
        else:
            if make_month == 2 and make_day > 28:
                make_day = make_day % 28
            elif make_month in (4,6,9,11) and make_day >30:
                make_day = make_day % 30
            elif make_day > 31:
                make_day = make_day % 31

        # 转为字符串
        make_year = str(make_year)

        if make_month < 10:
            make_month = '0' + str(make_month)
        else:
            make_month = str(make_month)

        if make_day < 10:
            make_day = '0' + str(make_day)
        else:
            make_day = str(make_day)
        if length == 10:
            return "-".join([make_year, make_month, make_day])
        else:
            return make_year + make_month + make_day
    # 国籍
    def chiose_country(self):
        countrys = random.choice(["CHN", "ALB", "DZA", "AFG", "ARG", "ARE", "ABW", "OMN", "AZE", "EGY", "ETH", "IRL", "EST", "AND", "AGO", "AIA", "ATG", "AUT", "ALA", "AUS", "MAC", "BRB", "PNG", "BHS", "PAK", "PRY", "PSE", "BHR", "PAN", "BRA", "BLR", "BMU", "BGR", "MNP", "BEN", "BEL", "ISL", "PRI", "BIH", "POL", "BOL", "BLZ", "BWA", "BTN", "BFA", "BDI", "BVT", "PRK", "GNQ", "DNK", "DEU", "TLS", "TGO", "DOM", "DMA", "RUS", "ECU", "ERI", "FRA", "FRO", "PYF", "GUF", "ATF", "MAF", "VAT", "PHL", "FJI", "FIN", "CPV", "GMB", "COG", "COD", "COL", "CRI", "GRD", "GRL", "GEO", "GGY", "CUB", "GLP", "GUM", "GUY", "KAZ", "HTI", "KOR", "NLD", "BES", "SXM", "HMD", "MNE", "HND", "KIR", "DJI", "KGZ", "GIN", "GNB", "CAN", "GHA", "GAB", "KHM", "CZE", "ZWE", "CMR", "QAT", "CYM", "CCK", "COM", "CIV", "KWT", "HRV", "KEN", "COK", "CUW", "LVA", "LSO", "LAO", "LBN", "LTU", "LBR", "LBY", "LIE", "REU", "LUX", "RWA", "ROU", "MDG", "IMN", "MDV", "FLK", "MLT", "MWI", "MYS", "MLI", "MKD", "MHL", "MTQ", "MYT", "MUS", "MRT", "USA", "UMI", "ASM", "VIR", "MNG", "MSR", "BGD", "PER", "FSM", "MMR", "MDA", "MAR", "MCO", "MOZ", "MEX", "NKR", "NAM", "ZAF", "ATA", "SGS", "SSD", "NRU", "NPL", "NIC", "NER", "NGA", "NIU", "NOR", "NFK", "PLW", "PCN", "PRT", "JPN", "SWE", "CHE", "SLV", "WSM", "SRB", "SLE", "SEN", "CYP", "SYC", "SAU", "BLM", "CXR", "STP", "SHN", "KNA", "LCA", "SMR", "SPM", "VCT", "LKA", "SVK", "SVN", "SJM", "SWZ", "SDN", "SUR", "SLB", "SOM", "TJK", "THA", "TZA", "TON", "TCA", "TTO", "TUN", "TUV", "TUR", "TKM", "TKL", "WLF", "VUT", "GTM", "VEN", "BRN", "UGA", "UKR", "URY", "UZB", "ESP", "ESH", "GRC", "HKG", "SGP", "NCL", "NZL", "HUN", "SYR", "JAM", "ARM", "YEM", "IRQ", "IRN", "ISR", "ITA", "IND", "IDN", "GBR", "VGB", "IOT", "JOR", "VNM", "ZMB", "JEY", "TCD", "GIB", "CHL", "CAF", "TWN"])
        return countrys

    def data_time(self):
        """数据生成时间"""
        datatime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return datatime

    def random_num(self, num):
        """ 接收int类型参数num，根据参数随机生成数字,返回字符串"""
        res_list = []
        while len(res_list) < num:
            elem = random.randint(0, 9)
            if res_list or elem:
                res_list.append(str(elem))

        return "".join(res_list)

    # 电话号码数据
    def make_tel_num(self, tp=11):
        """
        随机生成手机号码
        11:家庭电话
        12:工作电话
        21:固定电话
        22:移动电话
        23:传真
        :return: 返回字符串类型
        """
        if tp == '21' or tp == '23':
            phone = self.random_num(9)
        else:
            one_two = random.choice(["13", "14", "15", "16", "17", "18", "19"])
            three_nine = []
            for num in range(9):
                elem = random.randint(0, 9)
                three_nine.append(str(elem))
            phone = one_two + "".join(three_nine)
        return phone

    # 邮箱数据
    def make_email_data(self):
        extend = random.choice(["163.com", "126.com", "gmail.com", "qq.com", "sina.com", "outlook.com"])
        name_1 = self.random_str(6)
        name_2 = self.random_num(6)
        return name_1 + "_" + name_2 + "@" + extend


    def make_address(self, code=None):
        """
        # 地址数据
        :param code: 省市区代码
        :return: 详细地址
        """
        if not code:
            code = self.random_city()
        three_level_addr = pool.get_data(code)
        three_level_addr.replace('-', '')
        street_address = random.choice([
            "解放路", "千佛山", "趵突泉", "泉城路", "大明湖", "东关", "文东", "建新", "甸柳", "燕山", "姚家", "龙洞", "智远", "舜华路", "大观园", "杆石桥",
            "四里村",
            "魏家庄", "二七", "七里山", "六里山", "舜玉路", "泺源", "王官庄", "舜耕", "白马山", "七贤", "十六里河", "兴隆", "党家", "陡沟", "振兴街", "中大槐树",
            "道德街", "西市场", "五里沟", "营市街", "青年公园", "南辛庄", "段店北路", "张庄路", "匡山", "美里湖", "吴家堡", "腊山", "兴福", "玉清湖", "无影山",
            "天桥东街",
            "北村", "南村", "堤口路", "北坦", "制锦市", "宝华", "官扎营", "纬北路", "药山", "北园", "泺口", "桑梓店", "大桥", "山大路", "洪家楼", "东风", "全福",
            "孙村", "巨野河", "华山", "荷花路", "王舍人", "鲍山", "郭店", "唐冶", "港沟", "遥墙", "临港", "仲宫", "柳埠", "董家", "彩石", "文昌", "崮云湖",
            "平安",
            "五峰山", "归德", "万德", "张夏", "明水", "双山", "圣井", "埠村", "枣园", "龙山", "普集", "官庄", "相公庄", "绣惠", "文祖", "曹范", "白云湖",
            "高官寨",
            "宁家埠", "济阳", "济北", "回河", "孙耿", "崔寨", "太平", "榆山", "锦水"
        ])
        areas_name = random.choice([
            "万豪国际公寓", "晓月苑", "永定路商住中心", "橙色年代", "嘉慧苑", "致雅居", "彩虹城", "松园小区", "燕归园", "北京青年城", "金宝纯别墅", "翌景嘉园", "涧桥·泊屋馆",
            "京东丽景", "旭风苑公寓", "朝阳无限", "庄胜二期", "潇雅居", "GOGO新世代", "飞腾家园", "英嘉公寓", "高第", "金榜园", "迎曦园", "风格与林",
            "太阳国际公馆(瑞景嘉园)",
            "永合馨苑", "澳洲新星", "丰润世家", "洋桥花园", "长安新城", "金隅丽港城", "兴涛社区", "糖人街", "时代芳群", "运河园", "浉城百郦", "测试项目", "新洲商务大厦",
            "加来小镇",
            "新新公寓", "颍泽洲", "城市印象", "上河美墅", "同泰苑", "和枫雅居", "建兴家园", "昊腾花园", "高苑·花样年华", "金码大厦", "天辉公寓", "NOLITA那里", "政馨家园",
            "文林商苑", "蝶翠华庭", "晋元庄小区", "幸福源", "当代城市家园", "非常生活", "祥瑞苑", "雪梨澳乡", "清欣园", "晟丰阁", "倚林佳园", "华龙小区", "秀安园",
            "新华联锦园",
            "乐澜宝邸", "棉花城", "CLASS", "金宸公寓", "燕景佳园", "珠江帝景", "龙山新新小镇", "万景公寓", "飘HOME", "蓝堡", "新纪元公寓", "中信红树湾", "海德堡花园",
            "天缘公寓", "长城盛世", "鲁艺上河村", "瑞馨公寓", "鼎诚国际MM", "德胜世嘉", "榆园新居", "远洋天地", "星河城", "黎明新座", "世纪城", "大观园中华商住区",
            "中国第一商城",
            "后现代城", "中海凯旋", "新都丽苑", "陶然北岸", "观河锦苑", "星光公寓", "观筑", "绿城星洲花园", "御鹿家园", "都市心海岸", "山水汇豪", "漪内轩", "颐园(碧水云天)",
            "新荣家园", "双桥温泉北里住宅", "恬心家园", "正邦嘉园", "依翠园", "万科西山庭院", "新御景", "天行建商务大厦", "浉城百丽", "华腾园", "同仁园", "格林小镇",
            "东华经典(东华金座)", "俊景苑", "朗琴园", "快乐洋城", "新中环公寓", "非常宿舍", "清城名苑", "兴都苑(水榭楼台)", "雍景台", "风林绿洲(奕翠庭)", "团结公寓"
        ])
        building_name = str(random.randint(1, 50))
        unit_num = str(random.randint(1, 9))
        floor_num = str(random.randint(1, 30))
        room_num = str(random.randint(1, 4))
        return three_level_addr + street_address + "街道" + areas_name + building_name + "楼" + unit_num + "单元" + floor_num + "层" + room_num + "号"


    def random_city(self):
        """# 随机市"""
        city_code = ["130100", "130200", "130300", "130400", "130500", "130600", "130700", "130800", "130900", "131000", "131100", "140100", "140200", "140300", "140400", "140500", "140600", "140700", "140800", "140900", "141000", "141100", "150100", "150200", "150300", "150400", "150500", "150600", "150700", "150800", "150900", "152200", "152500", "152900", "210100", "210200", "210300", "210400", "210500", "210600", "210700", "210800", "210900", "211000", "211100", "211200", "211300", "211400", "220100", "220200", "220300", "220400", "220500", "220600", "220700", "220800", "222400", "230100", "230200", "230300", "230400", "230500", "230600", "230700", "230800", "230900", "231000", "231100", "231200", "232700", "320100", "320200", "320300", "320400", "320500", "320600", "320700", "320800", "320900", "321000", "321100", "321200", "321300", "330100", "330200", "330300", "330400", "330500", "330600", "330700", "330800", "330900", "331000", "331100", "340100", "340200", "340300", "340400", "340500", "340600", "340700", "340800", "341000", "341100", "341200", "341300", "341400", "341500", "341600", "341700", "341800", "350100", "350200", "350300", "350400", "350500", "350600", "350700", "350800", "350900", "360100", "360200", "360300", "360400", "360500", "360600", "360700", "360800", "360900", "361000", "361100", "370100", "370200", "370300", "370400", "370500", "370600", "370700", "370800", "370900", "371000", "371100", "371200", "371300", "371400", "371500", "371600", "371700", "410100", "410200", "410300", "410400", "410500", "410600", "410700", "410800", "410900", "411000", "411100", "411200", "411300", "411400", "411500", "411600", "411700", "420100", "420200", "420300", "420500", "420600", "420700", "420800", "420900", "421000", "421100", "421200", "421300", "422800", "429000", "430100", "430200", "430300", "430400", "430500", "430600", "430700", "430800", "430900", "431000", "431100", "431200", "431300", "433100", "440100", "440200", "440300", "440400", "440500", "440600", "440700", "440800", "440900", "441200", "441300", "441400", "441500", "441600", "441700", "441800", "441900", "442000", "445100", "445200", "445300", "450100", "450200", "450300", "450400", "450500", "450600", "450700", "450800", "450900", "451000", "451100", "451200", "451300", "451400", "460100", "460200", "469000", "500300", "510100", "510300", "510400", "510500", "510600", "510700", "510800", "510900", "511000", "511100", "511300", "511400", "511500", "511600", "511700", "511800", "511900", "512000", "513200", "513300", "513400", "520100", "520200", "520300", "520400", "522200", "522300", "522400", "522600", "522700", "530100", "530300", "530400", "530500", "530600", "530700", "530800", "530900", "532300", "532500", "532600", "532800", "532900", "533100", "533300", "533400", "540100", "542100", "542200", "542300", "542400", "542500", "542600", "610100", "610200", "610300", "610400", "610500", "610600", "610700", "610800", "610900", "611000", "620100", "620200", "620300", "620400", "620500", "620600", "620700", "620800", "620900", "621000", "621100", "621200", "622900", "623000", "630100", "632100", "632200", "632300", "632500", "632600", "632700", "632800", "640100", "640200", "640300", "640400", "640500", "650100", "650200", "652100", "652200", "652300", "652700", "652800", "652900", "653000", "653100", "653200", "654000", "654200", "654300", "659000", "442000", "441900", "533100"]
        return random.choice(city_code)

    def chiose_provance(self, city):
        pro = ["350000", "710000", "370000", "460000", "610000", "540000", "620000", "210000", "450000", "420000", "120000", "150000", "110000", "440000", "340000", "320000", "230000", "330000", "810000", "530000", "140000", "640000", "650000", "510000", "520000", "430000", "310000", "630000", "820000", "360000", "130000", "220000", "410000", "500000", "999999"]
        pro_code = city[:2] + "0000"
        if pro_code in pro:
            return pro_code
        else:
            return "999999"

    def cust_tyep(self):
        """客户类别"""
        return random.choice([
            '1',  # FI
            '2'  # CGI
        ])

    def org_type(self):
        """组织机构类别"""
        code = random.choice([
            "1",  # corporation
            "2",  # credit union
            "3",  # government
            "4",  # limited liability company
            "5",  # not for profit
            "6",  # partnership
            "7",  # private label liability company
            "8",  # public authorities
            "9",  # publist list company
            "10",  # sole proprietorships
            "11"  # other
        ])
        return code


    def random_code(self):
        """多个共用，具体含义见字段注释"""
        return random.choice(['1','2'])

    def random_chenghu(self):
        """称呼"""
        return random.choice(['Mr', 'Ms'])

    def cust_status(self):
        """
        随机生成客户状态，n正常，c关闭，n:c=9:1
        :return:
        """
        status = random.choice(["n"  if i != 9 else "c" for i in range(10)])
        return status

    # 客户真实有效性数据
    def make_reals_data(self):
        """
        正常为空，不正常：
        1:留存的联系地址与注册地址不一致
        2:留存联系地址不存在或者虚构
        3:留存的电话号码属于无效、空号、已停机或无法接通
        4:证件非本人、证件伪造、变造证件
        5:拒绝配合尽职调查工作
        正常数据与不正常数据比例为1:10
        :return:
        """
        return random.choice(['' if num >= 1 else str(random.randint(1, 5)) for num in range(10)])

    # 股权复杂度数据
    def make_complex_data(self):
        complex = random.choice([
            "1",  # 股权 3层以下
            "2",  # 股权 3层及以上，有商业目的
            "3"  # 股权 3层以上；或3个及以上注册地；涉及信托/不受监管的投资基金/代名人股东等；及没有明显商业目的
        ])
        return complex

    # 非自然人股权可辨识度数据
    def make_clear_data(self):
        clear = random.choice([
            "1",  # 全民集体所有制企业等结构清晰的企业
            "2",  # 公司制企业等结构相对清晰的企业
            "3",  # 公司制外资企业等结构较难识辨的企业
            "4",  # 个人独资企业、家族企业、合伙等难以尽调的企业
            "5"  # 其他风险较高股权或控制权结构（信托、代名股东等
        ])
        return clear

    def make_rule_type(self):
        """预警类型"""
        return random.choice([
            '00',  # 大额
            '01'  # 可疑
        ])

    def make_warn_kd(self):
        """预警方式"""
        return random.choice([
            '0',  # 人工手动
            '1'  # 系统自动
        ])

    def make_ctif_tp(self):
        """可疑主体类别"""
        return random.choice([
            '1',  # 持卡人
            '2'  # 商户
        ])

    def make_tran_kd(self):
        """交易种类"""
        return random.choice([
            '0',  # 差错交易
            '1'  # 普通交易
        ])