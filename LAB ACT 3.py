#LAB 2-1

def classify_age(age):
    #Child
    if age <= 12:
        print("You are a Child.")
    #Teen
    elif age <= 19:
        print("You are a Teen.")
    #Adult
    elif age <= 64:
        print("You are an Adult.")    
    #Invalid
    elif age < 0:
        print("Invalid age.")
    #Senior
    else:
        print("You are a Senior.")

#put your age inside the parenthesis '.'
classify_age()
