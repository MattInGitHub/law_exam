import docx
file = docx.Document("D:\\answer.docx")
print("段落数:"+str(len(file.paragraphs)))
#输出段落编号及段落内容
for i in range(len(file.paragraphs)):
    print("第"+str(i)+"段的内容是："+file.paragraphs[i].text)