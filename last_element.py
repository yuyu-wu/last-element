# last_element
# Write a function called last_element. This function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.


# First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

def last_element(l):
    if l:
        return l[-1]
    return None