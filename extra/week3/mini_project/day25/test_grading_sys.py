import pytest
from grading_sys import Student, Student_list

@pytest.fixture
def student():
    return Student("Riaz")

def test_average_normal(student):
    student.score = [80, 90, 70]
    assert student.average() == 80.0

def test_average_empty(student):
    assert student.average() == 0

def test_average_single(student):
    student.score = [100]
    assert student.average() == 100

def test_grade_A(student):
    assert student.grade(93) == "4.0(A)"

def test_grade_F(student):
    assert student.grade(50) == "0.0(F)"

def test_status_pass(student):
    assert student.status(60) == "Pass"

def test_status_fail(student):
    assert student.status(59.99) == "Fail"

def test_valid_name_good():
    assert Student.valid_name("Riaz Ahmad") == True

def test_valid_name_bad():
    assert Student.valid_name("Riaz123") == False

def test_valid_name_hyphen():
    assert Student.valid_name("Riaz-Ahmad") == True

def test_valid_name_empty():
    assert Student.valid_name("") == False

def test_valid_name_spaces_only():
    assert Student.valid_name("   ") == False

@pytest.fixture
def student_list():
    return Student_list()

def test_add_student(student_list):
    s = student_list.add_student("Riaz")
    assert len(student_list.student) == 1
    assert student_list.student[0].name == "Riaz"

def test_view_report_found(student_list):
    student_list.add_student("Riaz")
    result = student_list.view_report("Riaz")
    assert result is not None
    assert result.name == "Riaz"

def test_view_report_not_found(student_list):
    result = student_list.view_report("Nobody")
    assert result is None

def test_view_report_case_insensitive(student_list):
    student_list.add_student("Riaz")
    result = student_list.view_report("riaz")
    assert result is not None

def test_delete_student(student_list):
    student_list.add_student("Riaz")
    student_list.delete_student("Riaz")
    assert len(student_list.student) == 0

def test_delete_student_not_found(student_list, capsys):
    student_list.delete_student("Nobody")
    captured = capsys.readouterr()
    assert "not found" in captured.out.lower()