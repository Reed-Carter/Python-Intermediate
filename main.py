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


subtracter_lambda = (lambda a, b: b - a)
print(subtracter_lambda(2, 4))


class Shoe:
    """The shoe object contains the size color and smell of a shoe

    Parameters
    ----------
    US_size: int
        The US size of a shoe
    color: str
        The color of the shoe
    smelly: bool
        If the shoe is smelly or not
    """
    def __init__(self, US_size: int, color: str, smelly: bool) -> str:
        self.US_size = US_size
        self.color = color
        self.smelly = smelly

    def euro_size(self):
        """The function converts the US shoe size to a European shoe size

        returns
        -------
        European shoe size: str
        """
        print(str(self.US_size + 33))

Altra = Shoe(9,"blue", smelly=True)
Altra.euro_size()
Addidas = Shoe(11, "white", smelly=False)
Addidas.euro_size()
