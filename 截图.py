from PIL import ImageGrab
from time import time
import os

now = float(time())

im = ImageGrab.grab()
im.save('%s/Screenshot.png' % os.path.dirname(os.path.abspath(__file__)))
im.close()

print("程序耗时：", float(time()) - now)