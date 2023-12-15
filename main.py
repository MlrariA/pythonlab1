import pandas as pd
import os
def convert_symbols_to_string(symbols):
    return ', '.join(map(str, symbols))
pathname = './lab_pi_101.xlsx'
if os.path.isfile(pathname):
    data = pd.read_excel(pathname)
else:
    data = pd.read_excel("https://drive.google.com/uc?export=download&id=1Bo5Oili5dAvWDSzAZXjzgjS71IrmLWun")
groups = data["Группа"]
while(True):
    group_name = input ("Введите номер группы ")
    if group_name in groups.values:
        break
    print("Данные по группе отсутствуют")
all_marks = data["Оценка"]
group_marks = data[groups == group_name].shape[0]
students_count = data[groups == group_name]["Личный номер студента"]
unique_student_count = students_count.unique()
unique_control_level = data["Уровень контроля"].unique()
unique_years = sorted(data["Год"].unique())
output_string = (f"В исходном датасете содержалось {all_marks.size} оценок, из них {group_marks} относятся к группе {group_name}\n"
f"В датасете находятся оценки {unique_student_count.size} студентов со следующими личными номерами {group_name}: {convert_symbols_to_string(unique_student_count)}\n"
f"Используемые формы контроля: {convert_symbols_to_string(unique_control_level)}\n"
f"Данные представлены по следующим учебным годам: {convert_symbols_to_string(sorted(unique_years))}")
print(output_string)