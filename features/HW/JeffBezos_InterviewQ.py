# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?


############ NO IDEA! I'm way off

jeff = ['google', 'amazon']
bezos = 0


while bezos < 2:
    i = 0
    while i < 6:
        stored_letter = jeff[bezos][i]
        x = 1
        i += 1
        while x < 6:
            stored_letter2 = jeff[bezos][x]
            x = x+1

            if stored_letter == stored_letter2:
                print("Non unique letters are found " + stored_letter + " is the same as " + stored_letter2)
                break
    bezos += 1



