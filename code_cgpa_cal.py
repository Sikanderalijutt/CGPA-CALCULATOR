import streamlit as st

# ---------------------- GRADE CONVERSION ---------------------- #
def grade_point_from_marks(marks: float) -> float:
    """
    Convert marks (0–100) to grade points on a 4.0 scale.

    Parameters:
        marks (float): Marks obtained in a subject.

    Returns:
        float: Corresponding grade point.
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


# ---------------------- GPA CALCULATION ---------------------- #
def calculate_semester_gpa(marks_list, credits_list) -> float:
    """
    Calculate GPA for a single semester.

    Parameters:
        marks_list (list[float]): Marks for each course.
        credits_list (list[float]): Credit hours for each course.

    Returns:
        float: Semester GPA.
    """
    if not marks_list or not credits_list or len(marks_list) != len(credits_list):
        return 0.0

    total_weighted = sum(grade_point_from_marks(m) * c for m, c in zip(marks_list, credits_list))
    total_credits = sum(credits_list)

    return round(total_weighted / total_credits, 2) if total_credits > 0 else 0.0


def calculate_cgpa(semester_gpas, semester_credits) -> float:
    """
    Calculate overall CGPA.

    Parameters:
        semester_gpas (list[float]): GPA for each semester.
        semester_credits (list[float]): Total credits for each semester.

    Returns:
        float: Cumulative GPA (CGPA).
    """
    if not semester_gpas or not semester_credits or len(semester_gpas) != len(semester_credits):
        return 0.0

    total_weighted = sum(g * c for g, c in zip(semester_gpas, semester_credits))
    total_credits = sum(semester_credits)

    return round(total_weighted / total_credits, 2) if total_credits > 0 else 0.0


# ---------------------- STREAMLIT UI ---------------------- #
def main():
    st.set_page_config(page_title="CGPA Calculator", page_icon="🎓", layout="centered")

    st.title("🎓 CGPA Calculator")
    st.write("A simple and professional tool to calculate your semester GPA and overall CGPA.")

    n_semesters = st.number_input("How many semesters have you completed?", min_value=1, step=1)

    semester_gpas = []
    semester_credits = []

    for sem in range(1, n_semesters + 1):
        st.subheader(f"📘 Semester {sem}")

        n_courses = st.number_input(
            f"Number of courses in Semester {sem}",
            min_value=1,
            step=1,
            key=f"courses_{sem}"
        )

        marks_list = []
        credits_list = []

        for i in range(1, int(n_courses) + 1):
            col1, col2 = st.columns(2)
            with col1:
                marks = st.number_input(f"Marks for Course {i}", min_value=0.0, max_value=100.0, key=f"marks_{sem}_{i}")
            with col2:
                credits = st.number_input(f"Credit Hours for Course {i}", min_value=1.0, max_value=5.0, key=f"credits_{sem}_{i}")

            marks_list.append(marks)
            credits_list.append(credits)

        if st.button(f"Calculate GPA for Semester {sem}", key=f"btn_{sem}"):
            gpa = calculate_semester_gpa(marks_list, credits_list)
            semester_gpas.append(gpa)
            semester_credits.append(sum(credits_list))
            st.success(f"✅ GPA for Semester {sem}: **{gpa}**")

    if len(semester_gpas) == n_semesters and semester_gpas:
        if st.button("📊 Calculate Overall CGPA"):
            cgpa = calculate_cgpa(semester_gpas, semester_credits)
            st.balloons()
            st.success(f"🎉 Your Overall CGPA is: **{cgpa}**")


# ---------------------- ENTRY POINT ---------------------- #
if __name__ == "__main__":
    main()
