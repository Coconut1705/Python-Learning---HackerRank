a = 18
b = 16
if a > b:
    print("Ngon luôn")
else:
    print("Chưa ngon lắm")

print("=======================================If...Else Statement=========================================")    

conure_is_hungry = False
if conure_is_hungry:
    print("Dẹt đói")
else:
    print("Dẹt no rùi")

def check(tuoi):
    if tuoi >= 18:
        print("Truy cập thành công!")
    else:
        print("Bị từ chối: Bạn chưa đủ tuổi.")

check(20) # Kết quả: Truy cập thành công!
check(17)