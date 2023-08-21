# 4. --------------------------------------------
def majority_element(nums: list) -> int:
    counter = {}
    for item in nums:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 0
    for major, count in counter.items():
        if count >= len(nums) // 2:
            return major


def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result1 == 2


test_majority_element()


# 5. --------------------------------------------
def get_subjects_not_passed_by_all_students(student_exams):
    return {n[2] for n in student_exams if n[1] < 60}


exams = [
    ("Alice", 85, "Math"),
    ("Bob", 59, "Math"),
    ("Charlie", 65, "Math"),
    ("Alice", 90, "Science"),
    ("Bob", 80, "Science"),
    ("Charlie", 32, "Science"),
    ("Alice", 95, "History"),
    ("Bob", 85, "History"),
    ("Charlie", 90, "History"),
]


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 85, "Math"),
        ("Bob", 59, "Math"),
        ("Charlie", 65, "Math"),
        ("Alice", 90, "Science"),
        ("Bob", 80, "Science"),
        ("Charlie", 32, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert get_subjects_not_passed_by_all_students(exams) == {
        "Science",
        "Math",
    }


test_get_subjects_not_passed_by_all_students()
