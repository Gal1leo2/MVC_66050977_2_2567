from model import PetDatabase
from view import PetView

class PetController:
    def __init__(self):
        self.db = PetDatabase()

    def show_pets(self):
        """แสดงสัตว์ทั้งหมดโดยแยกตามประเภท"""
        if not self.db.pets:
            PetView.display_error("❌ ไม่มีสัตว์ในระบบ")
            return
        PetView.display_pet_list(self.db.pets)
