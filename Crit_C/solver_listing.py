def possible_timetables(students: List[List[Subject]], periods_per_week: int) ->\
    Iterator[Dict[Subject, List[int]]]:

    solver = pywrapcp.Solver("timetable")

    # Flatten the list that contains each student's subjects and remove duplicates
    subjects = set(itertools.chain(*students))

    # Get the list of all the periods for all subjects
    period_names = itertools.chain(*[subject.period_names for subject in subjects])

    # Generate a dict of period_name:period_variable
    # We need a dict to be able to access each period's variable by name
    period_variables = {
        period_name: solver.IntVar(0, periods_per_week - 1, period_name)
        for period_name in period_names}

    for student in students:
        # Get the list of all the periods for the student's subjects
        student_period_names = list(
            itertools.chain(*[subject.period_names for subject in student])
        )

        # Filter the list of all periods to get only those that the student 
        # is a part of
        student_period_variables = [
            period_var
            for period_name, period_var in period_variables.items()
            if period_name in student_period_names
            ]

        # All of the student's periods must be scheduled at different times
        solver.AddConstraint(solver.AllDifferent(student_period_variables))

    db = solver.Phase(list(period_variables.values()),
                      solver.CHOOSE_MIN_SIZE_LOWEST_MAX,
                      solver.ASSIGN_CENTER_VALUE)
    solver.NewSearch(db)

    while solver.NextSolution():
        subject_map = defaultdict(list)
        for period_name, period_variable in period_variables.items():
            for subject in subjects:
                if period_name in subject.period_names:
                    subject_map[subject].append(period_variable.Value())

        yield subject_map
