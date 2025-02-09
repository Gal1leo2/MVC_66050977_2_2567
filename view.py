class PetView:
    @staticmethod
    def display_success(message):
        print(f"✅ {message}")

    @staticmethod
    def display_error(message):
        print(f"❌ {message}")

    @staticmethod
    def display_pet_list(pets):
        """แสดงรายการสัตว์ทั้งหมด"""
        print("\n📋 รายการสัตว์ทั้งหมด 📋")
        for pet in pets:
            pet_type = pet["pet_type"]
            if pet_type == "นกฟินิกซ์":
                PetView.display_phoenix(pet)
            elif pet_type == "มังกร":
                PetView.display_dragon(pet)
            elif pet_type == "นกฮูก":
                PetView.display_owl(pet)

    @staticmethod
    def display_phoenix(pet):
        """แสดงข้อมูลนกฟินิกซ์"""
        print("\n🔥 นกฟินิกซ์ 🔥")
        print(f"🐦 รหัสอาหาร: {pet['food_id']}")
        print(f"📅 วันที่ตรวจสุขภาพ: {pet['last_health_check']}")
        print(f"💉 จำนวนวัคซีน: {pet['vaccine_count']}")
        print(f"🔥 ใบรับรองไฟไม่ลาม: {'✅ มี' if pet['extra_info'] == 'True' else '❌ ไม่มี'}")
        print("-" * 30)

    @staticmethod
    def display_dragon(pet):
        """แสดงข้อมูลมังกร"""
        print("\n🐉 มังกร 🐉")
        print(f"🐲 รหัสอาหาร: {pet['food_id']}")
        print(f"📅 วันที่ตรวจสุขภาพ: {pet['last_health_check']}")
        print(f"💉 จำนวนวัคซีน: {pet['vaccine_count']}")
        print(f"🌫️ ระดับมลพิษจากควัน: {pet['extra_info']}%")
        print("-" * 30)

    @staticmethod
    def display_owl(pet):
        """แสดงข้อมูลนกฮูก"""
        print("\n🦉 นกฮูก 🦉")
        print(f"🦉 รหัสอาหาร: {pet['food_id']}")
        print(f"📅 วันที่ตรวจสุขภาพ: {pet['last_health_check']}")
        print(f"💉 จำนวนวัคซีน: {pet['vaccine_count']}")
        print(f"🛫 ระยะทางบินได้โดยไม่ทานข้าว: {pet['extra_info']} km")
        print("-" * 30)
