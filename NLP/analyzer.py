# encoding=utf-8
import jieba
import jieba.analyse
import xlrd
import re

books = xlrd.open_workbook('im.xlsx')
table = books.sheets()[1]
nrows = table.nrows

content = ''
for i in range(1, nrows):
    content += table.cell(i, 1).value

# 过滤无意义数据
def filterRaw(msg):
    sets = [
        '^我有问题要咨询哦~$',
        '^我刚刚浏览了【[\u4E00-\u9FA5]*】的信息，有问题要咨询哦~$',
        '^我对【[\u4E00-\u9FA5\w\W]*】很感兴趣，有问题要咨询。$',
        '^我是通过xxx装修公司的详情页来的用户$',
        '^我刚刚浏览了【1】的信息，有问题要咨询哦~$',
        '^你好$',
        '^您好$',
        '^在吗$',
        '^好的$',
        '^谢谢$',
        '^好的，谢谢$',
        '^哦哦$',
        '^对$',
        '^嗯$',
        '^嗨$',
        '^哈啰$',
        '^你好，在嘛？$',
    ]

    if (re.match("^[\u4E00-\u9FA5]", msg) == None):
        return False

    for ptrn in sets:
        match = re.match(ptrn, msg)
        if (match != None):
            return False
    return True

# 抽取topK高频词
def topTags(content, topK):
    jieba.analyse.set_stop_words('stopwords.txt')
    return jieba.analyse.extract_tags(content, topK)

# 基于TextRank获取关键词
def topTextRank(content, topK):
    jieba.analyse.set_stop_words('stopwords.txt')
    return jieba.analyse.textrank(content, topK)

# 获取topK高频词 && 出现次数
def topWeights(content, topK):
    words = {}
    segments = jieba.cut(content)
    for seg in segments:
        if seg in words:
            words[seg] += 1
        else :
            words[seg] = 1

    return sorted(words.items(), key=lambda item:item[1])

tags = topTextRank(content, 50)
for tag in tags:
    print(tag)
