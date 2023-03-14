# #Task 1: Alarm Clock
# class AlarmClock:
#     def __init__(self, current_time, alarm_time, alarm_on):
#         self.current_time = " "
#         self.alarm_time = " "
#         self.alarm_on = True if alarm_on == True else False
#     def set_current_time(self, current_time):
#         self.time = current_time(8)
#         print(self.current_time)
#     def set_alarm_time(self, alarm_time):
#         self.alarm_time = alarm_time()
#         print(self.alarm_time)
#     def set_alarm_on(self, alarm_on):
#         self.alarm_on = alarm_on(True)
#         print(self.alarm_on)
#     def check_alarm(self):
#         if self.alarm_on == True:
#             print("Alarm is on")
#         else:
#             print("Alarm is off")
#     def check_time(self):
#         if self.current_time == self.alarm_time:
#             print("Alarm is ringing")
#         else:
#             print("Alarm is not ringing")

# alarm = AlarmClock(8, 8, True)
# alarm.set_current_time(8)
# alarm.set_alarm_time(8)
# alarm.set_alarm_on(True)
# alarm.check_alarm()
# alarm.check_time()
class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
    def __init__(self, name, marks):
            self.name = name
            self.marks = marks
student_1 = student("Raj", 90)


