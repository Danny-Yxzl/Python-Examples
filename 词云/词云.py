import matplotlib.pyplot as plt  #数学绘图库
import jieba
from wordcloud import WordCloud
import os


thisDir = os.path.dirname(os.path.abspath(__file__))


#1、读入txt文本数据
with open("%s/words.txt" % thisDir, "r", encoding="utf-8") as f:
    text = f.read()


#2、结巴分词，默认精确模式。可以添加自定义词典userdict.txt,然后jieba.load_userdict(file_name) ,file_name为文件类对象或自定义词典的路径
# 自定义词典格式和默认词库dict.txt一样，一个词占一行：每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒

cut_text = jieba.cut(text)
result = "/".join(cut_text)  #必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云


def draw_wordcloud(text,
                   save_path="%s/wordcloud.png" % thisDir,
                   background_color="white",
                   size=600,
                   repeat=False,
                   max_words=20):
    #无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
    wc = WordCloud(font_path="%s/font.ttf" % thisDir,
                   background_color=background_color,
                   width=size,
                   height=size,
                   max_words=max_words,
                   repeat=repeat)
    wc.generate(text)
    wc.to_file(save_path)  #按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰


draw_wordcloud(text, repeat=Truez)


"""# 4、显示图片
plt.figure("词云图") #指定所绘图名称
plt.imshow(wc)       # 以图片的形式显示词云
plt.axis("off")      #关闭图像坐标系
plt.show()"""