#Import string module to use for quickest way to get all lowercase alphabetical characters
import string

usersentence = input("Input a sentence to see if it's a pangram: ")

# Function to find missing characters from sentence input by user
def getMissingLetters(usersentence):
    #Get all lowercase alphabetical characters 
    characters = string.ascii_lowercase
    #Make a set of lowercase alphabetical characters
    charset = set(characters)
    # Convert sentence to lowercase sorted set
    usersentenceset = sorted(set(usersentence.lower()))
    # Character set and sentence set are compared, characters not found in sentence set are returned
    notchar = {x for x in charset if x not in usersentenceset}
    if len(notchar) == 0:
        return " "
    else:
        notcharstr = ''.join(list(sorted(notchar)))
        return notcharstr
        
print(getMissingLetters(usersentence))