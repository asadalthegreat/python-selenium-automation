# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?


############ NO IDEA! I'm way off

def unique_letter_optimal(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    d = {}

    for l in string:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for k, v in d.items():
        if v == 1:
            return k

    return ""

print(unique_letter_optimal("viojklejf08j0fmvioewjf sjfkasldjfasl;kd jfasdofjsaidfjpas i"))