import sys
sys.setrecursionlimit(10000)
from uiautomator import device as d
#d = u2.connect('192.168.199.163')
print(d.info)
i=0
while i<10000:
        import random
        import time
        x1=random.randint(250,300)
        x2=random.randint(800,900)
        y1=random.randint(500,600)
        y2=random.randint(600,800)
        steps=random.randint(20, 22)
        d.swipe(x1, y1, x2, y2, steps)
