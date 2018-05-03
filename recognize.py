#coding=utf-8
from aip import AipImageClassify

APP_ID = '11154115'
API_KEY = 'q43giM57evcbrGhIrCaY2jpA'
SECRET_KEY = 'BXp4D26IqGfZzdcQztIysmYnPZyf5g45'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('E:\dishdata\\3.jpg')

""" 调用菜品识别 """
data = client.dishDetect(image);
for res in data['result']:
    for i in res.values():
        print i
