from collections import defaultdict
from dataclasses import dataclass
import traceback


@dataclass
class Student:
    student_id: str
    name: str
    teacher: str
    pingshi: float
    qimo: float
    zongping: float

    def calc_zongping(self):
        self.zongping = round((self.qimo * 0.7) + (self.pingshi * 0.3), 2)
        
    def __str__(self):
        return f"[stu_id={self.student_id}]: name={self.name}, teacher={self.teacher}, pingshi={self.pingshi}, qimo={self.qimo}, zongping={self.zongping}"


def progress_grades(filepath):
    students = []
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            lines = f.readlines()

            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) == 6:
                    student = Student(
                        student_id=parts[0],
                        name=parts[1],
                        teacher=parts[2],
                        pingshi=float(parts[3]),
                        qimo=float(parts[4]),
                        zongping=float(parts[5]),
                    )
                    student.calc_zongping()
                    students.append(student)
    except Exception:
        print(Exception)
        traceback.print_exc()
        return []
    return students


def calc_teacher_avgs(students: list[Student]) -> dict:
    teacher_data = defaultdict(lambda: [0.0, 0])

    for student in students:
        teacher_data[student.teacher][0] += student.qimo
        # 人数
        teacher_data[student.teacher][1] += 1

    result = {}

    for teacher, (total_qimo, count) in teacher_data.items():
        result[teacher] = round(total_qimo / count, 2)

    return result

if __name__ == '__main__':
    file = './exper-04/grade.txt'
    student_list = progress_grades(file)
    for stu in student_list:
        print(stu)
    teacher_avgs = calc_teacher_avgs(student_list)
    for teacher, avg in teacher_avgs.items():
        print(f"[teacher={teacher}]: avg={avg}")