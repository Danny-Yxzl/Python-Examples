import os
import pygal


thisDir = os.path.dirname(os.path.abspath(__file__))


# 创建柱状图对象
bar_chart = pygal.Bar()

# 图表命名
bar_chart.title = 'NBA历史得分前五球星数据'

# 添加数据
bar_chart.add('贾巴尔', 38387)
bar_chart.add('马龙', 36928)
bar_chart.add('詹姆斯', 34384)
bar_chart.add('科比', 33643)
bar_chart.add('乔丹', 32292)

# 在浏览器中查看
bar_chart.render_in_browser()

# 导出为矢量图形（不含文字）
# bar_chart.render_to_file('D:/Desktop/NBA.svg')