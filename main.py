def available_periods(start_times, durations, begin_working_time, end_working_time, consultation_time):
    actualT = int(begin_working_time[0:2]) * 60 + int(begin_working_time[3:5])
    startT = int(start_times[0][0:2]) * 60 + int(start_times[0][3:5])
    print(actualT)
    result = []
    while actualT < startT:
        hS = (actualT) // 60
        mS = (actualT) % 60
        actualT += consultation_time
        hE = (actualT) // 60
        mE = (actualT) % 60
        result.append(f'{hS}:{mS}-{hE}:{mE}')
    for time in range(len(start_times)):
        work_point = int(start_times[time][0:2]) * 60 + int(start_times[time][3:5])
        if (work_point > actualT):
            actualT += int(durations[time][3:5])
        print(work_point)
    print(result)


start = ["10:00", "11:00", "15:00", "15:30", "16:50"]
duration = [60, 30, 10, 10, 40]
Consultation_Time = 30
begin_working_time = "08:00"
end_working_time = "18:00"

if __name__ == '__main__':
    available_periods(start_times=start,
                      durations=duration,
                      begin_working_time=begin_working_time,
                      end_working_time=end_working_time,
                      consultation_time=Consultation_Time)



