def get_students(self, include_teachers: bool = False) -> Dict[str, List['Subject']]:
    subjects = list(self.get_subjects())

    student_names = list(
        set(itertools.chain(*(sub.student_names for sub in subjects)))
    )
    if include_teachers:
        for sub in subjects:
            if sub.teacher_name not in student_names:
                student_names.append(sub.teacher_name)

    students = defaultdict(list)
    for subject in subjects:
        for student_name in student_names:
            if (student_name in subject.student_names or 
                    student_name == subject.teacher_name):
                students[student_name].append(subject)

    return students

