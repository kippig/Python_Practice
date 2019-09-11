def hourglassSum(arr):
    """Calculates the maximum of a given shape
        :rtype Int representing the maximum of the sum of numbers in all arrangements of the shape"""

    def accumulate_shape(field, shape_mask, reducer, accumulator):
        """This function takes in a field containing a shape and applies the shape mask
            With these values, it then applies the accumulator"""

        for row in range(len(field)):
            for col in range(len(field)):
                if shape_mask[row][col]:
                    accumulator = reducer(accumulator, field[row][col])
        return accumulator

    # These could be passed in as arguments
    shape = [[True, True, True],
             [False, True, False],
             [True, True, True]]
    reducer = lambda x, y: x+y


    maximum = float('-inf')
    height = len(arr)
    width = len(arr[0])
    shape_width = len(shape[0])
    shape_height = len(shape)

    # The last shape can at most start shape width away from the edge
    # This iterates through all the shapes
    for i in range(width-shape_width+1):
        for j in range(height-shape_height+1):

            # The field is the possible space the shape takes up
            shape_value = accumulate_shape(field=[arr[l][i:i+shape_width] for l in range(j, j+shape_height)],
                                           shape_mask=shape,
                                           reducer=reducer,
                                           accumulator=0)

            if shape_value > maximum:
                maximum = shape_value

    return maximum


print(hourglassSum([[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]]))
