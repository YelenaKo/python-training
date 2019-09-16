hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

extra_hours = int((hour+dura) / 60)
end_hour = str((hour+extra_hours) % 24)
end_mins = str((mins+dura) % 60)
end_time = end_hour + ":" + end_mins

print("extra_hours: " + str(extra_hours))
print("event end at: " + end_time)
