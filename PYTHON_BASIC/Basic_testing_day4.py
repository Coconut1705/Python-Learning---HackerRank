print("============================Danh sách vòng lặp============================")

listA = ["GTA 5", "Minecraft", "The Witcher 3", "Cyberpunk 2077"]
for x in listA:
    print(x)

listB = ["LG", "Samsung", "Sony", "Toshiba"]
for i in range(len(listB)):
    print(i, listB[i]) 

listC = ["Python", "Java", "C++", "JavaScript"]
i = 0
while i < len(listC):
    print(i, listC[i])
    i += 1

listD = ["Red", "Blue", "Green", "Yellow"]
[print(x) for x in listD]

print("============================Đọc hiểu danh sách============================")

traicay = ["Táo", "Chuối", "Cam", "Dưa hấu"]
newlist = []
for x in traicay:
    if "C" in x:
        newlist.append(x)
print(newlist)