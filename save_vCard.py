import csv

Book = []
with open('contact.txt', 'r') as text:
    Book = text.read().split('\n')

Book_new = [i.split(', ') for i in Book]
Spisok_nomerov = [i[1:] for i in Book_new]
Name_full = [i[0] for i in Book_new]
Name = [i[0].split() for i in Book_new]


Result = []

for i in range(len(Name)):
    if len(Spisok_nomerov[i]) == 1:
        if len(Name[i]) == 3:
            Result.append(f'{Name_full[i]},{Name[i][0]},{Name[i][1]},{Name[i][2]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ')
        elif len(Name[i]) == 2:
            Result.append(f'{Name_full[i]},{Name[i][0]},,{Name[i][1]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ')
        elif len(Name[i]) == 1:
            Result.append(f'{Name_full[i]},,,{Name[i][0]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ')

    elif len(Spisok_nomerov[i]) == 2:
        if len(Name[i]) == 3:
            Result.append(f'{Name_full[i]},{Name[i][0]},{Name[i][1]},{Name[i][2]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ')
        elif len(Name[i]) == 2:
            Result.append(f'{Name_full[i]},{Name[i][0]},,{Name[i][1]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ')
        elif len(Name[i]) == 1:
            Result.append(f'{Name_full[i]},,,{Name[i][0]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ')

    elif len(Spisok_nomerov[i]) == 3:
        if len(Name[i]) == 3:
            Result.append(f'{Name_full[i]},{Name[i][0]},{Name[i][1]},{Name[i][2]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ::: {Spisok_nomerov[i][2]}')
        elif len(Name[i]) == 2:
            Result.append(f'{Name_full[i]},{Name[i][0]},,{Name[i][1]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ::: {Spisok_nomerov[i][2]}')
        elif len(Name[i]) == 1:
            Result.append(f'{Name_full[i]},,,{Name[i][0]},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,, {Spisok_nomerov[i][0]} ::: {Spisok_nomerov[i][1]} ::: {Spisok_nomerov[i][2]}')

Result.insert(0, 'Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value')

with open('contakt.csv', 'w') as csv_file:
    for row in Result:
        csv_file.write(row)
        csv_file.write('\n')



