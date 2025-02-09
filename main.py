from controller import PetController

def main():
    controller = PetController()

    while True:
        print("\n🐾 ระบบจัดการสัตว์เลี้ยง 🐾")
        print("1. แสดงรายการสัตว์ทั้งหมด")
        print("2. อัปเดตข้อมูลสัตว์ (extra_info)")
        print("3. ออกจากระบบ")
        choice = input("เลือกเมนู: ")

        if choice == "1":
            controller.show_pets()
        elif choice == "2":
            controller.update_extra_info()
        elif choice == "3":
            print("👋 ออกจากระบบ...")
            break
        else:
            print("❌ กรุณาเลือกเมนูที่ถูกต้อง!")

if __name__ == "__main__":
    main()
