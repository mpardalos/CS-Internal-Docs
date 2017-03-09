def get_subjects(self) -> Iterator['Subject']:
    subject_name_row = list(self.worksheet.rows)[0][1:]  # type: List[Cell]
    columns = list(self.worksheet.columns)

    for cell in subject_name_row:
        column = columns[cell.col_idx - 1]

        name = column[0].value
        if name in ('', None):
            break

        teacher_name = column[1].value.strip()
        sl_periods_per_week = column[2].value
        extra_hl_periods_per_week = column[3].value or 0
        hl_marker_index = _find_in_cells(column, 'HL')
        # Index of the first empty cell after the students
        ending_marker_index = _find_in_cells(column[4:], '') + 4  
        # occurs if the empty cell is not in the cells returned by the library
        if ending_marker_index <= 4:  
            ending_marker_index = len(column)

        # If there is only one group in the subject
        if hl_marker_index == -1:
            students = [cell.value for cell in column[4:ending_marker_index]]
            yield Subject(name, sl_periods_per_week, teacher_name, students)
        # If there are both sl and hl students in the subject
        else:
            sl_students = [cell.value.strip() for cell in column[4:hl_marker_index]]
            hl_students = [cell.value.strip() for cell 
                           in column[hl_marker_index + 1:ending_marker_index]]
            # common periods
            yield Subject(name + ' SL+HL', sl_periods_per_week, teacher_name, 
                    sl_students + hl_students)
            # extra hl periods
            yield Subject(name + ' HL', extra_hl_periods_per_week, teacher_name, 
                    hl_students)

