from utils import *
dataList = readFileData("/home/liangpan/visualization/ky/projects/data/wangluo.xlsx")
propressedData = part(dataList)
with open('propressedData.json','w+') as file:
    file.write(json.dumps(propressedData,indent=4,ensure_ascii=False))