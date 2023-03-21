"""
4. Extract data

record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]

date_of_birth = (8, 12, 1928)
display list

"""

# record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
date_of_birth = (8, 12, 1928)
print(f"Last name: {record[1]}")
print(f"Born: {record[2]}")
print(f"{record[0]} was born in {date_of_birth[2]} and was a great {record[3]} player.")