from collections import defaultdict
import openpyxl
import docx
import os


os.chdir('C:\\Users\\Administrator\\Desktop')


wb = openpyxl.load_workbook('md.xlsx')
doc = docx.Document('d.docx')

sheet_a = wb.get_sheet_by_name('Sheet1')

group_name_k = ''
group_names = defaultdict(list)

for i in range(4,156):
        name = sheet_a.cell(row = i,column = 2).value
        if len(name) == 2:
                name = '  '.join(name)
        group_name = sheet_a.cell(row = i,column = 3).value
        if (group_name_k == group_name):
                group_names[group_name_k].append(name)
        else:
                group_name_k = group_name
                group_names[group_name_k].append(name)
        

        

s = ''
for g in group_names.keys():
        s = s + g + '\n'
        k = 0
        count = len(group_names[g])
        for gns in group_names[g]:
                count = count - 1
                if (k != 6):
                        s = s + gns + "  "
                        k = k + 1
                        if (count == 0):
                                s = s + '\n'
                elif (k == 6):
                        k = 0
                        s = s + gns + "  " + '\n'
doc.add_paragraph(s)                    
doc.save('d.docx')
                
