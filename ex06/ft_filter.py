# def checkAdult(age):
#     if age >= 18:
#         return True
#     else:
#         return False

def ft_filter(function_to_apply, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function_to_apply is None:
        return [function_to_apply(filtered_item) for filtered_item in iterable]
    return [filtered_item for filtered_item in iterable if (function_to_apply(filtered_item))]


# print(ft_filter.__doc__)
# print(ft_filter(checkAdult, [15, 18]))

# print(list(filter(checkAdult, [15, 18])))

