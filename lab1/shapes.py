def triangle(size):
    """ This function must print a triangle using the # character on the screen.

    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """
    for i in range(size+1):
        for j in range(i):
            print('#', end='')
        print()
    print()


def rectangle(width, height):
    """ This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)
    
    >>> rectangle(1, 1)
    #
    
    >>> rectangle(3, 1)
    ###
    
    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """

    if (width < 1 or height < 1):
        print('bruh')
        return 0

    for i in range(width):
        print('#', end='')
    print()

    for i in range(height-2):
        print('#', end='')
        for i in range(width-2):
            print(' ', end='')
        if width > 1:
            print('#')
    
    if height > 1:
        for i in range(width):
            print('#', end='')
        print()
    print()

if __name__ == "__main__":
    triangle(0)
    triangle(10)

    rectangle(6, 6)
    rectangle(-1, -1)
