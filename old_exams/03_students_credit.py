def students_credits(*args):

    courses = {}

    for arg in args:
        course, credits, max_points, diyans_points = arg.split("-")

        current_points = int(credits) * (int(diyans_points)/int(max_points))

        if course not in courses.keys():
            courses[course] = current_points

    sorted_courses = sorted(courses.items(), key=lambda x:-x[1])
    total_points = sum(courses.values())
    if total_points >= 240:
        result = f"Diyan gets a diploma with {total_points:.1f} credits."
    else:
        result = f"Diyan needs {abs(total_points - 240):.1f} credits more for a diploma."

    for course, points in sorted_courses:
        result += f"\n{course} - {points:.1f}"

    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print("------------------------------------------------------------------")
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print("------------------------------------------------------------------")

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
