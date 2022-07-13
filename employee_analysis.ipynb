# Open the file in read mode

file = open("/employee_revenue.txt", "r")
data = file.read()


# Print the data

print(data)


# Create empty lists again

names = []
call_numbers = []
average_deal_sizes = []
revenues = []


# Define a function to clean and extract the data

def clean_extraction(lines):
# Loop over the whole data
  for employee in lines:
    #Clean the string
    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()

    # Split the clean string
    split_employee = employee.split(" ")
    
    # Extract the name
    name = split_employee[0]
    call_number = split_employee[2]

    # Extract the average deal size
    for i in split_employee:
      if "$" in i:
        average_deal_size = i
        average_deal_size = average_deal_size.split("$")[0]
  
    # Extract the revenue
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index - 1
    revenue = split_employee[revenue_index]

    # Convert to the correct data types
    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)

    # Append the information to the lists
    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)

  return names, call_numbers, average_deal_sizes, revenues


# Assign returned values to variables

names, call_numbers, average_deal_sizes, revenues = clean_extraction(lines)


# Print out the information

print("Name:", names)
print("Number of calls:", call_numbers)
print("Average deal size:", average_deal_sizes)
print("Revenue:", revenues)


# Generate IDs for each employee

IDs = list(range(0,11))
print(IDs)


# Pair the employee names with the IDs in a dictionary

dictionary1 = dict(zip(IDs, names))
dictionary1


# Pair the names with the revenues

dictionary2 = dict(zip(revenues,names))
dictionary2


# Find the lowest and the best performing employees (ascending & descending order)

sorted_dictionary = sorted(dictionary2)[0:3]
for i in sorted_dictionary:
  print(dictionary2[i])

sorted_dictionary = sorted(dictionary2, reverse = True)[0:3]
for i in sorted_dictionary:
  print(dictionary2[i])
