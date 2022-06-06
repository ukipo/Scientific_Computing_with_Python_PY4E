def add_time(start, duration, day=None):
  # Divide the start time to number and am/pm
  start = start.split()
  start_time = start[0]
  start_period = start[1]

  # Divide start time to hours and minutes and convert to integer
  start_time = start_time.split(':')
  start_hour = int(start_time[0])
  start_min = int(start_time[1])

  # Convert hours to 24 hour format
  if start_period=='PM':
    start_hour = start_hour + 12

  # Divide duration to hours and minutes and convert to integer
  duration = duration.split(':')
  dur_hour = int(duration[0])
  dur_min = int(duration[1])

  # Optional day
  # Dictionary of days
  daydict = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
  # Get day
  if day!=None:
    day = day.capitalize()
    day_val = daydict[day]

  # Add minutes
  end_min = start_min + dur_min

  # Convert minutes into hours if necessary and add to duration hours
  if 60 <= end_min:
    add_hours = int(end_min/60) # to hours, int rounds down
    end_min = end_min - (60 * add_hours)
    dur_hour = dur_hour + add_hours

  # Add hours
  end_hour = start_hour + dur_hour

  # Convert hours into days if necessary
  if end_hour > 24:
    add_day = int(end_hour/24) # to days, int rounds down
    end_hour = end_hour - (24 * add_day)
  else:
    add_day = 0

  # Add day comment
  if add_day == 0:
    day_comment = ''
  elif add_day == 1:
    day_comment = ' (next day)'
  else:
    day_comment = ' (' + str(add_day) + ' days later)'

  # Figure out if AM or PM and convert time
  if end_hour == 0: # mindnight
    end_period = 'AM'
    end_hour = 12
  elif 0 < end_hour < 12: # morning
    end_period = 'AM'
  elif 12 == end_hour: # noon
    end_period = 'PM'
  elif 12 < end_hour < 24: # afternoon
    end_period = 'PM'
    end_hour = end_hour - 12

  # Get end time
  # If minutes are one digit, add 0
  end_min = str(end_min)
  if len(end_min)==1:
    end_min = "0" + end_min

  end_time = [end_hour, ':', end_min, " ", end_period]
  end_time = [str(item) for item in end_time] # convert all to strings
  end_time = ''.join(end_time)

  # Get optional end day
  if day != None:
    end_val = day_val + add_day
    if end_val > 7:
      end_val = end_val - (7 * int(end_val/7)) # int rounds down
    for dayname, dayval in daydict.items():
      if dayval==end_val:
        end_day = dayname
    end_day = ', ' + end_day
  else:
    end_day = ''

  # Return
  new_time = end_time + end_day + day_comment

  return new_time
