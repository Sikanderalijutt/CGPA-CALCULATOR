def grade_point_from_marks(marks):
    """
    Convert marks (e.g. 0–100) to a grade point on a scale (e.g. 0–4 or 0–5).
    Adjust this function based on your grading scheme.
    """
    if marks >= 90:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 70:
        return 3.3
    elif marks >= 60:
        return 3.0
    elif marks >= 50:
        return 2.0
    else:
        return 0.0

def calculate_semester_gpa(marks_list, credits_list):
    """
    marks_list: list of marks for each course in that semester
    credits_list: list of credit hours for each course
    Returns: semester GPA
    """
    total_weighted = 0.0
    total_credits = 0.0
    for marks, cr in zip(marks_list, credits_list):
        gp = grade_point_from_marks(marks)
        total_weighted += gp * cr
        total_credits += cr
    if total_credits == 0:
        return 0
    return total_weighted / total_credits

def calculate_cgpa(semester_gpas, semester_credits):
    """
    semester_gpas: list of semester GPAs
    semester_credits: list of total credits of each semester
    Returns: cumulative GPA (CGPA)
    """
    total_weighted = 0.0
    total_credits = 0.0
    for gpa, cr in zip(semester_gpas, semester_credits):
        total_weighted += gpa * cr
        total_credits += cr
    if total_credits == 0:
        return 0
    return total_weighted / total_credits

def main():
    n_sem = int(input("How many semesters completed? "))
    semester_gpas = []
    semester_credits = []
    for sem in range(1, n_sem + 1):
        print(f"\n--- Semester {sem} ---")
        n_courses = int(input("Number of courses in this semester: "))
        marks_list = []
        credits_list = []
        for i in range(1, n_courses + 1):
            m = float(input(f"Enter marks for course {i}: "))
            c = float(input(f"Enter credit hours for course {i}: "))
            marks_list.append(m)
            credits_list.append(c)
        gpa = calculate_semester_gpa(marks_list, credits_list)
        print(f"GPA for semester {sem}: {gpa:.2f}")
        semester_gpas.append(gpa)
        semester_credits.append(sum(credits_list))
    cgpa = calculate_cgpa(semester_gpas, semester_credits)
    print(f"\nYour overall CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    main()
