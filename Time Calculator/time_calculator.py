def add_time(start, duration, day="0"):
  strPar = start.split(":")
  durPar = duration.split(":")

  morning = "AM" in start

  if day != '0':
    capDay = day.capitalize()
  else:
    capDay = "0"

  startHour = int(strPar[0])
  startMin = int(strPar[1].split()[0])

  durHour = int(durPar[0])
  durnMin = int(durPar[1].split()[0])

  quo, rem = divmod(startMin + durnMin, 60)

  if morning:
    totalHrs = startHour + durHour + quo

  else:
    totalHrs = startHour + durHour + quo + 12

  daysLater, newhr = divmod(totalHrs, 24)

  if newhr < 12 and newhr != 0:
    am_pm = "AM"
    newMin = rem
    newHr = newhr

  elif newhr > 12:
    am_pm = "PM"
    newMin = rem
    newHr = newhr - 12

  elif newhr == 0:
    am_pm = "AM"
    newMin = rem
    newHr =  12

  else:
    am_pm = "PM"
    newMin = rem
    newHr = 12

  new_time = f"{newHr:02d}:{newMin:02d} {am_pm}".lstrip('0')

  if capDay != "0":
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = (days.index(capDay) + daysLater) % 7
    new_time += f", {days[index]}"
  
  if daysLater > 1:
    new_time += f" ({daysLater} days later)"
  elif daysLater == 1:
    new_time += " (next day)"

  return new_time
