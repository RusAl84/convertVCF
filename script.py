import quopri
import os

List_contact = []
File = "1.vcf"
with open (File) as file: # чтение файла с контактами
    for i in file:
        List_contact.append (i)
# print(List_contact)
# функция для обьединения перенесенных строк
def Func (List_for_change):
    List_contact_1 = []
    for i in List_contact:
        if len(i)>1:
            if i[-2] == '=':
                List_contact_1.append (i[:-2])
            else:
                List_contact_1.append (i)
    with open ('File.txt', 'w', encoding='UTF-8') as file:
        for i in List_contact_1:
            file.write (i)
    List_contact_1 = []
    with open ('File.txt') as file:
        for i in file:
            List_contact_1.append (i)
    # os.unlink ('File.txt') # удаление temp файла
    return (List_contact_1)

def dec(d):
    Str_1 = bytes (d, 'UTF-8')
    Str_2 = quopri.decodestring (Str_1)
    Str_2=str(Str_2, 'UTF-8')
    return Str_2

List_contact = Func(List_contact)
ulist=[]
for item in List_contact:
    # if item.startswith("N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"):
    #     d=item.replace("N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:","")
    #     ulist.append(dec(d))    
    if item.startswith("FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"):
        d=item.replace("FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:","")
        ulist.append(dec(d))
    if item.startswith("TEL;CELL:"):
        d=""
        d=item.replace("TEL;CELL:","")
        ulist.append(d)
# print(ulist)
with open ('Contacts_Decode.txt', 'w', encoding="UTF-8") as file:
    for i in ulist:
        file.write(str(i))