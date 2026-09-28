import csv

def save_to_scv(jobs) :
    with open("download.csv", "w", encoding = "cp949") as file :
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No.", "회사", "제목", "지역", "상세보기"])
        for index,job in enumerate(jobs) :
            csv_writer.writerow([
                index + 1,
                job["company"],
                job["title"],
                job["location"],
                job["link"]
            ])