import requests
import csv
import time

def crawl_scores(start_sbd: int, end_sbd: int, year: int, output_file="data/raw/raw_national_exam_scores_2025.csv"):
    
    subjects = ["TOAN", "VAN", "NGOAI_NGU", "LI", "HOA", "SINH", "SU", "DIA", "TIN_HOC", "CN_CONG_NGHIEP", "CN_NONG_NGHIEP", "GDKT_PL", "TONGDIEM"]
    header = ["SBD"] + subjects
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for sbd in range(start_sbd, end_sbd + 1):
            sbd_str = f"{sbd:08d}"  
            url = f"https://s6.tuoitre.vn/api/diem-thi-thpt.htm?sbd={sbd_str}&year={year}"

            try:
                response = requests.get(url, timeout=5)
                data = response.json()

                if data.get("success") and data.get("total", 0) > 0:
                    student = data["data"][0]
                    row = [sbd_str] + [student.get(subj, -1) for subj in subjects]
                    writer.writerow(row)
                    print(f"[INFO] {sbd_str}: {row}")
                else:
                    print(f"[INFO] {sbd_str}: No data.")
                    time.sleep(2)  

                time.sleep(0.1)  

            except Exception as e:
                print(f"Error with SBD {sbd_str}: {e}")
                continue

crawl_scores(start_sbd=1000001, end_sbd=9009899, year=2025)