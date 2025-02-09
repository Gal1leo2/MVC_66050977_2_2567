from controller import PetController

def main():
    controller = PetController()

    while True:
        print("\n🐾 ระบบจัดการสัตว์เลี้ยง 🐾")
        print("1. ตรวจสอบและอัปเดตข้อมูลสัตว์")
        print("2. แสดงรายงานสรุป")
        print("3. ออกจากระบบ")
        choice = input("เลือกเมนู: ")

        if choice == "1":
            food_id = input("🔍 ใส่รหัสอาหารของสัตว์: ").strip()
            controller.validate_extra_info(food_id)
        elif choice == "2":
            controller.report_summary()
        elif choice == "3":
            print("👋 ออกจากระบบ...")
            break
        else:
            print("❌ กรุณาเลือกเมนูที่ถูกต้อง!")

if __name__ == "__main__":
    main()
