import csv

CSV_FILE = "pets.csv"

class PetDatabase:
    def __init__(self):
        self.pets = self.load_pets()

    def load_pets(self):
        """โหลดข้อมูลจาก CSV"""
        pets = []
        try:
            with open(CSV_FILE, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["vaccine_count"] = int(row["vaccine_count"])
                    row["extra_info"] = row["extra_info"] if row["extra_info"] else None  # ถ้า extra_info ว่าง ให้เป็น None
                    pets.append(row)
        except FileNotFoundError:
            print(f"⚠️ ไม่พบไฟล์ {CSV_FILE}")
        return pets

    def update_extra_info(self, food_id, extra_info):
        """อัปเดตค่า extra_info ของสัตว์ที่มี food_id ตรงกัน"""
        updated = False
        for pet in self.pets:
            if pet["food_id"] == food_id:
                pet["extra_info"] = extra_info
                updated = True
                break

        if updated:
            self.save_to_csv()
            return True
        return False

    def save_to_csv(self):
        """บันทึกข้อมูลทั้งหมดกลับลง CSV"""
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["food_id", "pet_type", "last_health_check", "vaccine_count", "extra_info"])
            for pet in self.pets:
                writer.writerow([pet["food_id"], pet["pet_type"], pet["last_health_check"], pet["vaccine_count"], pet["extra_info"]])
