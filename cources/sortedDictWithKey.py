# Function calling
def dictionairy():
    # Declare hash function
    key_value = {}
 
# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
    print(f"Task 1:-\n How to sort dictionary by keys")
    # way 1

    sorted_keys = sorted(key_value.keys())
    sorted_dict = {key:key_value[key] for key in sorted_keys}

    # way 2

    # sorted_dict = dict(sorted(key_value.items()))
    # print(sorted_dict)


def main():
    # function calling
    dictionairy()
 
 
# Main function calling
if __name__ == "__main__":
    main()