from model import PetDatabase
from view import PetView

class PetController:
    def __init__(self):
        self.db = PetDatabase()

    def validate_extra_info(self, food_id):
        """ตรวจสอบข้อมูลสัตว์และอัปเดต หากไม่ผ่านเงื่อนไขให้ปฏิเสธไป"""
        pet = next((p for p in self.db.pets if p["food_id"] == food_id), None)
        if not pet:
            PetView.display_error("❌ ไม่พบสัตว์ที่มีรหัสอาหารนี้")
            return

        pet_type = pet["pet_type"]
        extra_info = PetView.get_extra_info(pet_type)  
        accepted = self.check_validation(pet_type, extra_info)

        if self.db.update_extra_info(food_id, extra_info, accepted) and accepted:
            PetView.display_success("✅ อัปเดตข้อมูลสำเร็จ!")

    def check_validation(self, pet_type, extra_info):
        """ตรวจสอบว่าข้อมูลพิเศษผ่านเงื่อนไขหรือไม่ (Validation before update to model)"""
        if pet_type == "นกฟินิกซ์" and extra_info is True:
            return True
        elif pet_type == "มังกร" and isinstance(extra_info, int) and extra_info <= 70:
            return True
        elif pet_type == "นกฮูก" and isinstance(extra_info, int) and extra_info >= 100:
            return True
        else:
            PetView.display_error("❌ ข้อมูลไม่ถูกต้องหรือไม่ผ่านเงื่อนไข")
            return False

    def report_summary(self):
        """ดึงข้อมูลรายงานจาก Model และส่งไปแสดงผลที่ View"""
        accepted, rejected = self.db.get_summary()
        PetView.display_summary(accepted, rejected)
