class PetView:
    @staticmethod
    def get_extra_info(pet_type):
        """ขอข้อมูลพิเศษของสัตว์ตามประเภท"""
        if pet_type == "นกฟินิกซ์":
            return PetView.get_phoenix_info()
        elif pet_type == "มังกร":
            return PetView.get_dragon_info()
        elif pet_type == "นกฮูก":
            return PetView.get_owl_info()
        return None

    @staticmethod
    def get_phoenix_info():
        """ขอข้อมูลพิเศษสำหรับนกฟินิกซ์"""
        return input("🔥 สัตว์มีใบรับรองไฟไม่ลามหรือไม่? (true/false): ").strip().lower() == "true"

    @staticmethod
    def get_dragon_info():
        """ขอข้อมูลพิเศษสำหรับมังกร"""
        try:
            return int(input("🌫️ ระดับมลพิษที่เกิดจากควัน (%): ").strip())
        except ValueError:
            return None

    @staticmethod
    def get_owl_info():
        """ขอข้อมูลพิเศษสำหรับนกฮูก"""
        try:
            return int(input("🛫 ระยะทางบินได้โดยไม่ทานข้าว (km): ").strip())
        except ValueError:
            return None

    @staticmethod
    def display_error(message):
        """แสดงข้อความข้อผิดพลาด"""
        print(message)

    @staticmethod
    def display_success(message):
        """แสดงข้อความความสำเร็จ"""
        print(message)

    @staticmethod
    def display_summary(accepted, rejected):
        """แสดงรายงานสรุป"""
        print("📊 รายงานสรุป")
        print(f"✅ สัตว์ที่รับเข้า: {sum(accepted.values())}")
        print(f"❌ สัตว์ที่ถูกปฏิเสธ: {sum(rejected.values())}")
        for pet_type in accepted:
            print(f"{pet_type}: รับเข้า {accepted[pet_type]} / ปฏิเสธ {rejected[pet_type]}")
