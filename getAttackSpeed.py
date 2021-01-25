import re
import pytesseract
from PIL import Image
from PIL import ImageGrab

def getAttackSpeed(x_begin,y_begin,x_end,y_end):
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标

    bbox = (x_begin,y_begin,x_end,y_end)
    im = ImageGrab.grab(bbox)
    im.save('cut.png')
    # 调用tesseract识别图像
    text = pytesseract.image_to_string(Image.open("cut.png"), lang="eng")
    # print(text)
    # 筛选出识别出的一堆数据中的小数
    matchObj = re.search(r'.*([0-9]{1,}[.][0-9]*).*', text)
    if (matchObj):
        attackSpeed = float(matchObj.group(1))
        # 偶尔会把1识别成7，如果为7则返回0
        if (attackSpeed == 7):
            return 0

        # print('攻速:' + matchObj.group(1))
        return float(matchObj.group(1))

if __name__ == '__main__':
    # 循环调用函数，输出返回结果
    # 四个参数可以使用微信截图，鼠标移动时显示的参数提示
    while (1):
        temp = getAttackSpeed(690, 1234, 833,1336)
        print('攻速:',temp)

