
# Complete the solve function below.
def solve(s):
    string_list = s.split(" ")
    new_string = ""
    for word in string_list:
        new_string += word.capitalize() + " "
    return new_string
        