from os import system
from time import sleep
from typing import Any, Hashable, Iterable


def get_input(field: str, error_msg: str = "Error!", is_empty: bool = True, valid_range: Iterable = ()) -> str:
    """ Get input from user

    Args:
        field (str): Get wahat you want to enter.
        error_msg (str): Defaults to "Error!".
        is_empty (bool): Determine if you are allowed to enter nothing or not. Defaults to True.
        valid_range (Iterable): Determine if what you enter should be in a defined range or not. Defaults to ().

    Returns:
        str: What the user enter
    """
    while True:
        error_list = []

        if field in ("age", "new age"):
            data = int(input(f"Enter the {field}\n\U0001F449"))
        else:
            data = input(f"Enter the {field}\n\U0001F449")
        system("cls")

        if not is_empty and data == "":
            error_list.append(
                f"{error_msg}The field cannot remain empty. \U0001F644")

        if valid_range and data not in valid_range:
            error_list.append(
                f"{error_msg} What you entered is not in valid range. \U0001F612")

        if not error_list:
            return data

        print(*error_list, sep="\n")


def show_list_of_dict(data_list: list[dict], *keys: Hashable, heading: bool = True, line_number: bool = True, size: int = 20) -> None:
    """Show students

    Args:
        data_list (list[dict]): List of students' specifications
        heading (bool): Determine if you want to see headings or not. Defaults to True.
        line_number (bool): Detrmine if you want to see the number of each student. Defaults to True.
        size (int, optional): What the size of each cell in students' table should be. Defaults to 20.
    """
    print()
    if heading:
        print("_" * (len(keys) * size))

        if line_number:
            print("#    ", end="")

        for key in keys:
            print(str(key).ljust(size), end="")

    print()
    print("_" * (len(keys) * size))

    for index, data in enumerate(data_list, 1):

        if line_number:
            print(str(index).ljust(5), end="")

        for key in keys:
            print(str(data.get(key, "")).ljust(size), end="")

        print()
        print("_" * (len(keys) * size))
    print()


def search(data_list: list[dict], key: Hashable, val: Any) -> list[dict]:
    """Find student

    Args:
        data_list (list[dict]): List of students
        key (Hashable): Fields needed to enter students to the list
        val (Any): Student's specifications

    Returns:
        list[dict]: Give students you searched
    """
    res = []

    for data in data_list:

        if data.get(key) == val:
            res.append(data)

    return res


student_list = [
    {"name": "meisam", "family_name": "ilka", "age": 20, "gender": "Male",
        "national_code": "2222222", "student_code": "2222222"},
    {"name": "parsa", "family_name": "bokaei", "age": 23, "gender": "Male",
        "national_code": "3333333", "student_code": "3333333"},
    {"name": "mehrsa", "family_name": "bokaei", "age": 30, "gender": "Female",
        "national_code": "4444444", "student_code": "4444444"},
    {"name": "hadis", "family_name": "taheri", "age": 45, "gender": "Female",
        "national_code": "5555555", "student_code": "5555555"},
    {"name": "meisam", "family_name": "negari", "age": 14, "gender": "Male",
        "national_code": "6666666", "student_code": "6666666"}
]


while True:

    # get choice
    choice = get_input(
        field="""\n\n1. [A]dd student
2. [S]how students
3. [R]emove Student
4. [E]dit student
5. [F]ind student
6. [EX]it""", is_empty=False, valid_range=("1", "2", "3", "4", "5", "6", "A", "S", "R", "E", "F", "EX")
    )

    match choice:
        case "1" | "A":

            while True:
                system("cls")

                answer = input(
                    "Are you sure you want to add student(s) to the student list? 1. Yes or 2. No\n\U0001F449")
                system("cls")

                # region get answer
                match answer:
                    case "Yes" | "yes" | "1":

                        # get name
                        name = get_input(field="name", is_empty=False)

                        # get family name
                        family_name = get_input(
                            field="family name", is_empty=False)

                        # get age
                        age = get_input(field="age", is_empty=False,
                                        valid_range=tuple(range(1, 121)))

                        # get gender
                        gender = get_input(field="gender", is_empty=False,
                                           valid_range=("Male", "Female", "Other"))

                        # get national code
                        while True:
                            n_code = get_input(
                                field="national code", is_empty=False)

                            search_res = search(
                                student_list, key="national_code", val=n_code)

                            if search_res:
                                print(
                                    n_code, "is already registered in the system as a student's national code. \U0001F9D0")
                            else:
                                break

                        # get student code
                        while True:
                            std_code = get_input(
                                field="student code", is_empty=False)

                            search_res = search(
                                student_list, key="student_code", val=std_code)

                            if search_res:
                                print(
                                    std_code, "is already registered in the system as a student's national code. \U0001F9D0")
                            else:
                                break

                        student = {
                            "name": name,
                            "family_name": family_name,
                            "age": age,
                            "gender": gender,
                            "national_code": n_code,
                            "student_code": std_code
                        }
                        student_list.append(student)

                        # region showing added student
                        see_student = input(
                            "Do you want to see the profile of the student you entered? 1. Yes or 2. No \n\U0001F449")
                        system("cls")

                        if see_student in ("Yes", "yes", "1"):
                            show_list_of_dict(
                                student_list, "name", "family_name", "age", "gender", "national_code", "student_code")
                        # endregion
                    case "No" | "no" | "2":
                        break
                    case _:
                        print(
                            "You did not choose one of the options. Wait 3 seconds. \U0001F621")
                        sleep(3)
                        continue
                # endregion

                if input("Do you want to add another student? 1. Yes or 2. No\n\U0001F449") not in ("Yes", "yes", "1"):
                    system("cls")
                    break

        case "2" | "S":

            # region get answer about which column the user want to see
            answer = input(
                "Do you want to see all columns? 1. Yes or 2. No \n\U0001F449")
            system("cls")

            if answer in ("Yes", "yes", "1"):
                display_key = ("name", "family_name",
                               "age", "gender", "national_code", "student_code")
            else:
                display_key = []

                for key in ("name", "family_name",
                            "age", "gender", "national_code", "student_code"):
                    while True:
                        print("Do you want to see student's",
                              key, "column? 1. Yes or 2. No \n\U0001F447", end="")
                        answer_ = input("\n")
                        system("cls")

                        match answer_:
                            case "Yes" | "yes" | "1":
                                display_key.append(key)
                                break
                            case "No" | "no" | "2":
                                break
                            case _:
                                print(
                                    "You did not choose one of the options. \U0001F624")
            # endregion

            # show students' profile
            show_list_of_dict(student_list, *display_key)

        case "3" | "R":
            while True:
                system("cls")

                # show all students
                show_list_of_dict(student_list, "name", "family_name",
                                  "age", "gender", "national_code", "student_code")

                # region get which option the user want to remove a student according to
                remove_option = get_input(field="\n1. [N]ame\n2. [F]amily name\
                        \n3. [A]ge\n4. [G]ender\n5. [NA]tional Code\n6. [S]tudent Code\n7. [E]xit", is_empty=False, valid_range=("1", "2", "3", "4", "5", "6", "7", "N", "F", "A", "G", "NA", "S", "E"))

                match remove_option:

                    case "1" | "N":
                        key = "name"
                    case "2" | "F":
                        key = "family_name"
                    case "3" | "A":
                        key = "age"
                    case "4" | "G":
                        key = "gender"
                    case "5" | "NA":
                        key = "national_code"
                    case "6" | "S":
                        key = "student_code"
                    case _:
                        break
                    # endregion

                # region get the value of the option the user chose
                if remove_option in ("A", "3"):
                    val = get_input(field="age", is_empty=False,
                                    valid_range=range(1, 121))
                elif remove_option in ("G", "4"):
                    val = get_input(field="gender", is_empty=False,
                                    valid_range=("Male", "Female", "Other"))
                else:
                    val = get_input(field=key, is_empty=False)

                search_res = search(student_list, key=key, val=val)

                if not search_res:
                    print(
                        "The value you entered does not exist in student list.\nWait 3 seconds. \U0001F62A")
                    sleep(3)
                    continue

                for student in student_list[:]:
                    if student[key] == val:
                        print(*student.values(), sep="\t")
                        remove_confirm = input(
                            "Are you sure you want to remove this student? 1. Yes or 2. No\n\U0001F449")
                        system("cls")

                        if remove_confirm in ("Yes", "yes", "1"):
                            student_list.remove(student)
                            print("The student is deleted successfully. \U0001F929")
                        else:
                            print(
                                "The student remained in the student list. \U0001F642")
                # endregion

                if input("Do you want to remove another student? 1. Yes or 2. No\n\U0001F449") not in ("Yes", "yes", "1"):
                    system("cls")
                    break

        case "4" | "E":
            flag = False
            while not flag:
                # show all students
                show_list_of_dict(student_list, "name", "family_name",
                                  "age", "gender", "national_code", "student_code")

                edit_option = get_input(field="\n1. [NA]tional Code\n2. [S]tudent Code\n3. [EX]it", is_empty=False, valid_range=(
                    "1", "2", "3", "NA", "S", "EX"))

                match edit_option:
                    case "EX" | "3":
                        break

                    case "NA" | "1":
                        edit_option = "national_code"

                    case "S" | "2":
                        edit_option = "student_code"

                flag = True
                while flag:

                    edit_value = input(
                        "What is the value of the option you chose?\n\U0001F449")
                    system("cls")

                    search_res = search(student_list, edit_option, edit_value)

                    if not search_res:
                        print(
                            "There is not any student with the", edit_value, "you entered. \U0001F621")
                        continue

                    student = search_res[0]

                    while flag:

                        print("Which one do you want to edit?")

                        edit_field = get_input(field="\n1. [N]ame\n2. [F]amily name\n3. [A]ge \n4. [G]ender\n5. [NA]tional Code\n6. [S]tudent Code\n7. [EX]it", is_empty=False, valid_range=(
                            "1", "2", "3", "4", "5", "6", "7", "N", "F", "A", "G", "NA", "S", "EX"))

                        match edit_field:
                            case "1" | "N":
                                # get new name
                                student["name"] = get_input(
                                    field="new name", is_empty=False)

                            case "2" | "F":
                                # get new family
                                student["family_name"] = get_input(
                                    field="new family name", is_empty=False)

                            case "3" | "A":
                                # get new age
                                student["age"] = get_input(field="new age", is_empty=False,
                                                           valid_range=range(1, 121))

                            case "4" | "G":
                                # get new gender
                                student["gender"] = get_input(field="new gender", is_empty=False,
                                                              valid_range=("Male", "Female", "Other"))

                            case "5" | "NA":
                                # get new national code
                                while True:
                                    new_ncode = get_input(
                                        field=" new national code", is_empty=False)

                                    search_n_res = search(
                                        student_list, "national_code", new_ncode)

                                    if search_n_res:
                                        print(
                                            new_ncode, "exists in the system. The national code you enter should be unique. \U0001F621")
                                    else:
                                        break

                                student["national_code"] = new_ncode

                            case "6" | "S":
                                # get new student code
                                while True:
                                    new_stdcode = get_input(
                                        field=" new student code", is_empty=False)

                                    search_s_res = search(
                                        student_list, "student_code", new_stdcode)

                                    if search_s_res:
                                        print(
                                            new_stdcode, "exists in the system. The student code you enter should be unique. \U0001F621")
                                    else:
                                        break

                                student["student_code"] = new_stdcode

                            case "7" | "EX":
                                flag = False
                                break
        case "5" | "F":
            while True:
                # region get which option the user want to find a student according to
                find_option = get_input(field="\n1. [N]ame\n2. [F]amily name\n3. [A]ge\n4. [G]ender\n5. [NA]tional Code\n6. [S]tudent Code\n7. [EX]it", is_empty=False, valid_range=(
                    "1", "2", "3", "4", "5", "6", "7", "N", "F", "A", "G", "NA", "S", "EX"))

                match find_option:

                    case "1" | "N":
                        key = "name"
                    case "2" | "F":
                        key = "family_name"
                    case "3" | "A":
                        key = "age"
                    case "4" | "G":
                        key = "gender"
                    case "5" | "NA":
                        key = "national_code"
                    case "6" | "S":
                        key = "student_code"
                    case _:
                        break
                # endregion

                # region get value of the option the user chose
                if find_option in ("A", "3"):
                    val = get_input(field="age", is_empty=False,
                                    valid_range=range(1, 121))
                elif find_option in ("G", "4"):
                    val = get_input(field="gender", is_empty=False,
                                    valid_range=("Male", "Female", "Other"))
                else:
                    val = get_input(field=key, is_empty=False)
                # endregion

                # region show the student the user wanted to find
                search_res = search(student_list, key, val)
                show_list_of_dict(search_res, "name", "family_name",
                                  "age", "gender", "national_code", "student_code")
                # endregion
        case _:
            break
