from employee import employee_details

def test_employee_details():
    result = employee_details(
        "Rahul", 101, "IT", 30000
    )

    expected = (
        "Name: Rahul, ID: 101, "
        "Department: IT, Salary: 30000"
    )

    assert result == expected