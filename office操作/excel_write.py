from tempfile import TemporaryFile
from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet('Wangzi')
sheet1.write(0, 0, '0,0')
sheet1.write(0, 1, '0,1')

book.save('D:/Desktop/simple.xls')
#book.save(TemporaryFile())