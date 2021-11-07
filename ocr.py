# 导入easyocr
import easyocr
# 创建reader对象
reader = easyocr.Reader(['ch_sim','en'])
# 读取图像
print("----------------------------")
result = reader.readtext('D:/Desktop/1.png')
# 结果
print([result[i][1] for i in range(len(result))])
