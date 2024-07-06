


def remove_common_chars(name1, name2):
 

  name1_lower = name1.lower() 
  name2_lower = name2.lower()
  for char in name1_lower:
    if char in name2_lower:
      name1_lower = name1_lower.replace(char, '', 1) 
      name2_lower = name2_lower.replace(char, '', 1)
  return name1_lower, name2_lower

def flames(name1, name2):
 
  name1, name2 = remove_common_chars(name1, name2)
  combined_length = len(name1) + len(name2)
  flames = "FLAMES"

  index = 0
  while len(flames) > 1:
    step = combined_length % len(flames)
    index = (index + step) % len(flames)
    flames = flames[:index] + flames[index + 1:] 

  return flames

# Get user input for names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Play the game
relationship = flames(name1, name2)
print(f"{name1} and {name2} are destined to be {relationship.title()}.")
