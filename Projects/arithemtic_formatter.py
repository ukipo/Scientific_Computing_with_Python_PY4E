def arithmetic_arranger(problems, results=False):
  # Check if 5 or less items have been entered
  if len(problems)>5:
    return 'Error: Too many problems.'
  # Create empty list of items, first and second
  first_num = list()
  second_num = list()
  separators = list()
  res_num = list()
  for item in problems:
    # Split strings into numbers and operators
    item_sep = item.split()
    # Check if operators are + or -
    if item_sep[1]!='+' and item_sep[1]!='-' :
      return "Error: Operator must be '+' or '-'."
    # Sanity check if number
    try:
      frst = int(item_sep[0])
      scnd = int(item_sep[2])
    except:
      return 'Error: Numbers must only contain digits.'
    # Calculate result of operations
    if item_sep[1]=="+":
      rslt = frst + scnd
    elif item_sep[1]=="-":
      rslt = frst - scnd
    # Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    if len(item_sep[0]) > 4 or len(item_sep[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    # Difference between first and second number and chunk size
    dif_fs = abs(len(item_sep[0]) - len(item_sep[2]))
    chunksize = (max(len(item_sep[0]), len(item_sep[2]))+2)
    # Which is bigger - extend items to lists of first and second number rows
    if len(item_sep[0]) > len(item_sep[2]):
      first_num.extend(["  ", frst, " "*4])
      second_num.extend([item_sep[1], " "*(dif_fs+1), scnd, " "*4])
      separators.extend(["-"*chunksize, " "*4])
      res_num.extend([" "*(chunksize-(len(str(rslt)))), rslt, " "*4])
    elif len(item_sep[0]) < len(item_sep[2]):
      # Difference between first and second number
      first_num.extend(["  ", " "*dif_fs, frst, " "*4])
      second_num.extend([item_sep[1], " ", scnd, " "*4])
      separators.extend(["-"*chunksize, " "*4])
      res_num.extend([" "*(chunksize-(len(str(rslt)))), rslt, " "*4])
    else:
      first_num.extend(["  ", frst, " "*4])
      second_num.extend([item_sep[1], " ", scnd, " "*4])
      separators.extend(["-"*chunksize, " "*4])
      res_num.extend([" "*(chunksize-(len(str(rslt)))), rslt, " "*4])

  # Clean up and convert to strings
  first_num = ''.join([str(item) for item in first_num]).rstrip()
  second_num = ''.join([str(item) for item in second_num]).rstrip()
  separators = ''.join([str(item) for item in separators]).rstrip()
  res_num = ''.join([str(item) for item in res_num]).rstrip()

#   # Were the results chosen?
  if results==True:
    arranged_problems = f"{first_num}\n{second_num}\n{separators}\n{res_num}"
  else:
    arranged_problems = f"{first_num}\n{second_num}\n{separators}"

  return arranged_problems
