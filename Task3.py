def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    intervals_ = []
    for pup_idx in range(0, len(pupil), 2):
        pup_inter_start = pupil[pup_idx]
        pup_inter_end = pupil[pup_idx + 1]

        for tut_idx in range(0, len(tutor), 2):
            tut_inter_start = tutor[tut_idx]
            tut_inter_end = tutor[tut_idx + 1]
            if pup_inter_start > tut_inter_end:
                continue
            if pup_inter_end < tut_inter_start:
                break
            if pup_inter_start < tut_inter_start:
                res_int_start = tut_inter_start
                res_int_end = tut_inter_end if pup_inter_end > tut_inter_end else pup_inter_end
            else:
                res_int_start = pup_inter_start
                res_int_end = tut_inter_end if pup_inter_end > tut_inter_end else pup_inter_end
            if res_int_start < lesson[0]:
                res_int_start = lesson[0]
            if res_int_end > lesson[1]:
                res_int_end = lesson[1]
            if res_int_start > res_int_end:
                continue
            intervals_.append([res_int_start, res_int_end])

    appearance_ = 0
    for interval in intervals_:
        appearance_ += interval[1] - interval[0] + 1

    return appearance_
