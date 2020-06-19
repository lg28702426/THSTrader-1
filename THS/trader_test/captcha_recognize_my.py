import time
import uuid

import pytesseract
import pywinauto
from pywinauto import clipboard

from THS.trader_test.captcha_recognize import captcha_recognize

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getCodeByGrid(grid,app):
    # grid = main.window(
    #     control_id=0x417,
    #     class_name='CVirtualGridCtrl'
    # )  # 获取grid
    grid.set_focus()
    time.sleep(0.5)


    rootPath = "captchas"
    file_path = rootPath +  "/" + str(uuid.uuid4()) + ".png"

    pywinauto.keyboard.SendKeys('^c')  # 输入C

    app.top_window().window(
        control_id=0x965,
        class_name='Static'
    ).CaptureAsImage().save(file_path)  #保存验证码

    captcha_num = captcha_recognize(file_path) # 识别验证码

    print(captcha_num)

    app.top_window().window(
        control_id=0x964,
        class_name='Edit'
    ).set_text(captcha_num)  # 输入验证码

    app.top_window().window(
        control_id=0x1,
        class_name='Button'
    ).click()  # 点击提交确认

    time.sleep(1)
    try:
        data = clipboard.GetData() # 显示剪切板数据
    except Exception as e:
        data = clipboard.GetData()
    return data