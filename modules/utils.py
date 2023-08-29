def add_space_around_colons(string):
  
  new_string = ""
  
  for i in range(len(string)):
    if string[i] == ":":
      new_string += " " + string[i] + " "
    else:
      new_string += string[i]

  return new_string