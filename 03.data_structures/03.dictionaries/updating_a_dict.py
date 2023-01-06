students_dict = dict()
students_dict["X1001"] = "Anitha"
students_dict["X1002"] = "Bindhu"
students_dict["X1003"] = "Dia"

print(students_dict)

new_person = {"X1001": "Amrutha"}
students_dict.update(new_person)

print(students_dict)

new_person = {"X1004" : "Sindhu"}
students_dict.update(new_person)

print(students_dict)