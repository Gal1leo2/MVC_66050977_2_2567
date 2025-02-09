import csv

class PetDatabase:
    def __init__(self, filename="pets.csv"):
        self.filename = filename
        self.pets = self.load_pets()
        self.accepted_count = {"นกฟินิกซ์": 0, "มังกร": 0, "นกฮูก": 0}
        self.rejected_count = {"นกฟินิกซ์": 0, "มังกร": 0, "นกฮูก": 0}

    def load_pets(self):
        """โหลดข้อมูลสัตว์จาก CSV"""
        pets = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["vaccine_count"] = int(row["vaccine_count"])  # Convert vaccine count to int
                    pets.append(row)
        except FileNotFoundError:
            pass  # ถ้าไม่มีไฟล์ CSV ก็ให้เป็นค่าว่าง
        return pets

    def update_extra_info(self, food_id, extra_info, accepted):
        """อัปเดตข้อมูลพิเศษของสัตว์ และบันทึกจำนวนรับ/ปฏิเสธ"""
        updated = False

        for pet in self.pets:
            if pet["food_id"] == food_id:
                pet["extra_info"] = extra_info
                if accepted:
                    self.accepted_count[pet["pet_type"]] += 1
                    self.save_pets()  # บันทึกการเปลี่ยนแปลงลง CSV ทันที
                else:
                    self.rejected_count[pet["pet_type"]] += 1
                updated = True
                break

        return updated

    def save_pets(self):
        """บันทึกข้อมูลสัตว์กลับไปที่ CSV (อัปเดตเฉพาะที่ถูกรับเข้า (Accepted Only))"""
        with open(self.filename, mode="w", newline='', encoding='utf-8') as file:
            fieldnames = ["food_id", "pet_type", "last_health_check", "vaccine_count", "extra_info"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.pets)  # เขียนข้อมูลใหม่ทั้งหมด

    def get_summary(self):
        """คืนค่าจำนวนสัตว์ที่รับเข้าและถูกปฏิเสธ"""
        return self.accepted_count, self.rejected_count
