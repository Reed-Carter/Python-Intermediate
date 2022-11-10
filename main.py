short_list_of_mountains = ["Verstovia", "Bear", "South Sister"]
def fourth_place(list_one: str ) -> str:
    """This is a function that returns the fourth item in a list.

    Args:
        list_one (str): a list with an index of 3 or greater

    Returns:
        str: the fourth item in the list or an error message for an index error if the list has an index less than 3
    """
    try:
        return list_one[3]
    except IndexError as E:
        print(E)

fourth_place(short_list_of_mountains)