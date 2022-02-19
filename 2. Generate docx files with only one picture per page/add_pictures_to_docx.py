from docx import Document
from docx.shared import Inches
import os
import re

doc = Document()
# Here input an absolute path of a source directory
path = r"xx"
nums = 0
fileList = os.listdir(path)
for i in fileList:
    if re.search(r"\.jpg|\.png", i):
        # You can customize the size of the picture
        doc.add_picture(path + "\\" + i, width=Inches(6))
        nums += 1
doc.save(f"{str(nums)}.docx")
