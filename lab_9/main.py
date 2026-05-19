from HumanitarianStudent import HumanitarianStudent
from NaturalStudent import NaturalStudent
from MixedStudent import MixedStudent
from HumanitarianTeacherVisitor import HumanitarianTeacherVisitor
from NaturalTeacherVisitor import NaturalTeacherVisitor
from ScholarshipVIsitor import ScholarshipVisitor
from ParentInjectionVisitor import ParentInjectionVisitor
from HostelVisitor import HostelVisitor
from CanteenVisitor import CanteenVisitor

def parse_action(line: str):
    parts = line.strip().split()
    if len(parts) == 0:
        return None

    action_type = parts[0]

    if action_type == "teach":
        subject_type = parts[1]
        credits_count = int(parts[2])
        if subject_type == "humanitarian":
            return HumanitarianTeacherVisitor(credits_count)
        elif subject_type == "natural":
            return NaturalTeacherVisitor(credits_count)

    elif action_type == "pay":
        where = parts[1]
        money_amount = int(parts[2])
        if where == "hostel":
            return HostelVisitor(money_amount)
        elif where == "canteen":
            return CanteenVisitor(money_amount)

    elif action_type == "obtain":
        from_where = parts[1]
        money_amount = int(parts[2])
        if from_where == "scholarship":
            return ScholarshipVisitor(money_amount)
        elif from_where == "parental":
            return ParentInjectionVisitor(money_amount)

    return None

def run_simulation(file_name: str):
    file = open(file_name, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    clean_lines = []
    for line in lines:
        if line.strip() != "":
            clean_lines.append(line.strip())

    student_type = clean_lines[0]
    needed_credits = int(clean_lines[1])
    start_money = int(clean_lines[2])

    if student_type == "humanitarian":
        student = HumanitarianStudent(needed_credits, start_money)
    elif student_type == "natural":
        student = NaturalStudent(needed_credits, start_money)
    elif student_type == "mixed":
        student = MixedStudent(needed_credits, start_money)
        return

    action_lines = clean_lines[3:]
    for line in action_lines:
        visitor = parse_action(line)
        if visitor != None:
            student.accept(visitor)
            if student.is_expelled == True:
                break

    print(f"--- Результат для файлу: {file_name} ---")
    if student.is_expelled == True:
        print("Статус: Студента відраховано.")
        print(f"Грошей залишилося: {student.money} грн")
        print(f"Кредитів набрано: {student.earned_credits} з {student.required_credits}")
    elif student.has_graduated == True:
        print("Статус: Успішно отримано диплом!")
        print(f"Грошей в кишені: {student.money} грн")
        print(f"Кредитів набрано: {student.earned_credits} з {student.required_credits}")
    else:
        print("Статус: Навчання завершено, але диплом НЕ отримано.")
        print(f"Грошей залишилося: {student.money} грн")
        print(f"Кредитів набрано: {student.earned_credits} з {student.required_credits}")
