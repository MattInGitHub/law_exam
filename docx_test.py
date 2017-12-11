import docx
from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet(title="test")
file = docx.Document("D:\\answer\\one.docx")
print("段落数:"+str(len(file.paragraphs)))

que_list=[]
one = []

for i in range(len(file.paragraphs)):
    if len(one)==2:
        que_list.append(one)
        one = []
    one.append(file.paragraphs[i].text.replace('\u3000','').replace('\t','').replace(' ',''))
for que in que_list:
    # print(que)
    ws.append(que)
    wb.save("D:\\answer\\one.xlsx")

# txt = '1.我国《宪法》明确规定，国家保护和改善生活环境和（B），防治污染和其他公害。'
# txt2= 'A.自然环境B.生态环境C.生态平衡D.生存环境'
# a = txt2.split('.')
# print(a)