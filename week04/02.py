def area_square():
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมจตุรัส")
    square = int(input("ใส่ความยาวด้าน: "))
    square1 = square*square
    print(f"พื้นที่ 4 เหลี่ยมจตุรัสนี้ คือ {square1}")

def area_square2():
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมผืนผ้า")
    weight = int(input("ส่ความกว้าง: "))
    height = int(input("ใส่ความยาว: "))
    square2 = weight*height
    print(f"พื้นที่ 4 เหลี่ยมผืนผ้านี้ คือ {square2}")

def area_circle():
    print("โปรแกรมคำนวณหาพื้นที่วงกลม")
    r = float(input("ใส่ความยาวของรัศมี: "))
    circle = 3.14*(r**2)
    print(f"พื้นที่ 4 เหลี่ยมวงกลมนี้ คือ {circle}")

def rps_game():
    import random
    print("โปรแกรมเป่ายิงฉุบ")
    while True :
        a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
        user = input("พิมพ์ ค้อน,กรรไกร,กระดาษ : ")
        if a == user :
            if a == "กรรไกร" :
                print("เสมอ เพราะ กรรไกรเหมือนกัน")
            elif a == "ค้อน" :
                print("เสมอ เพราะ ค้อนเหมือนกัน")
            elif a == "กระดาษ" :
                print("เสมอ เพราะ กระดาษเหมือนกัน")
            break
        elif user == "ค้อน" and a == "กรรไกร":
            print("คุณชนะ")
            break
        elif user == "กรรไกร" and a == "กระดาษ":
            print("คุณชนะ")
            break
        elif user == "กระดาษ" and a == "ค้อน":
            print("คุณชนะ")
            break
        else:
            print("คุณแพ้")
            break

def choice_return():
    while True:
        print("กรุณาเลือกโปรโปรแกรมที่ใช้งาน")
        print("กด 1 = โปรแกรมหาพื้นที่")
        print("กด 2 = โปรแกรมเป่ายิงฉุบ")
        print("กด 0 = ยกเลิกโปรแกรม")
        choice = int(input("พิมพ์โปรแกรมที่ต้องการ : "))
        if choice == 1:
            print("เลือกรูปทรงที่ต้องการหาพื้นที่")
            print("กด 1 = พื้นที่สี่เหลี่ยม")
            print("กด 2 = พื้นที่สี่เหลี่ยมผืนผ้า")
            print("กด 3 = พื้นที่วงกลม")
            print("กด 4 = ย้อนกลับ")
            c2 = int(input("พิมพ์พื้นที่ที่ต้องการหา : "))
            if c2 == 1:
                area_square()
            elif c2 == 2:
                area_square2()
            elif c2 == 3:
                area_circle()
            elif c2 == 4:

                choice_return()
        elif choice == 2:
            rps_game()
            print("กด 1 = เล่นอีกครั้ง")
            print("กด 2 = ย้อนกลับ")
            print("กด 3 = ปิดโปรแกรม")
            c3 = int(input("เลือกที่ต้องการที่นี่ : "))
            if c3 == 1:

                rps_game()
                return_rps_game()
                break
            elif c3 == 2:

                choice_return()
            elif c3 == 3:

                print("\nยกเลิกโปรแกรมสำเร็จ\n")
                break
        elif choice == 0:
            print("\nยกเลิกโปรแกรมสำเร็จ\n")
            break
        else:
            print("\nเกิดข้อผิดพลาด กรอกแค่ 1,2,0\n")


def return_rps_game():
    while True :
        print("กด 1 = เล่นอีกครั้ง")
        print("กด 2 = ย้อนกลับ")
        print("กด 3 = ปิดโปรแกรม")
        c3 = int(input("เลือกที่ต้องการที่นี่ : "))
        if c3 == 1:
            rps_game()
        elif c3 == 2:
            choice_return()
        elif c3 == 3:
            print("\nยกเลิกโปรแกรมสำเร็จ\n")
            break



while True:
    print("กรุณาเลือกโปรโปรแกรมที่ใช้งาน")
    print("กด 1 = โปรแกรมหาพื้นที่")
    print("กด 2 = โปรแกรมเป่ายิงฉุบ")
    print("กด 0 = ยกเลิกโปรแกรม")
    choice = int(input("พิมพ์โปรแกรมที่ต้องการ : "))
    if choice == 1:
        print("เลือกรูปทรงที่ต้องการหาพื้นที่")
        print("กด 1 = พื้นที่สี่เหลี่ยม")
        print("กด 2 = พื้นที่สี่เหลี่ยมผืนผ้า")
        print("กด 3 = พื้นที่วงกลม")
        print("กด 4 = ย้อนกลับ")
        c2 = int(input("พิมพ์พื้นที่ที่ต้องการหา : "))
        if c2 == 1:
            area_square()
        elif c2 == 2:
            area_square2()
        elif c2 == 3:
            area_circle()
        elif c2 == 4:
            choice_return()
    elif choice == 2:
        rps_game()
        print("กด 1 = เล่นอีกครั้ง")
        print("กด 2 = ย้อนกลับ")
        print("กด 3 = ปิดโปรแกรม")
        c3 = int(input("เลือกที่ต้องการที่นี่ : "))
        if c3 == 1:
            rps_game()
            return_rps_game()
            break
        elif c3 == 2:
            choice_return()
        elif c3 == 3:
            print("\nยกเลิกโปรแกรมสำเร็จ\n")
            break
    elif choice == 0:
        print("\nยกเลิกโปรแกรมสำเร็จ\n")
        break
    else:
        print("\nเกิดข้อผิดพลาด กรอกแค่ 1,2,0\n")


    




