"""
  Tech challenge
  Write a code in Python that it flat an integer array with multiple nested arrays.

  Input  -> [1, [2, [3, [4, 5]]]]
  Output -> [1, 2, 3, 4, 5]

  Approach
  We have an array, and this one can be filled with two defined elements: an integer or another array.
  Maybe the elements can be another type but starting with this premise, we can create a recursive function like this:
  "Take an element, if is an array, reutilize the element sending an element, else, is an integer and you need to return it"

  Pseudocode

  1. Get array
  2. Declare an output array with []
  3. Iterate in each item in array
    3.1 Send `item` to get number or array and output to send a mem reference array
      3.1.1 if `item` is a number
        3.1.1.1 append `item` in output
      3.1.2 else, send `item to get number or array` and output
    3.2 output is sended by reference and this is the result
  4. return output array
  
"""


def get_flat_array(array) -> list:
    output = []
    for item in array:
        find_number_in_array(output, item)
    return output


def find_number_in_array(output, item) -> None:
    is_array = item_is_array(item)
    if is_array:
        for items in item:
            find_number_in_array(output, items)
    else:
        output.append(item)


def item_is_array(item) -> bool:
    return isinstance(item, list)


if __name__ == "__main__":
    print(get_flat_array([1, [2, [3, [4, 5]]]]))
    print(get_flat_array([1, 2, 3, [1, [2, 3], 4, [2, 3, 4]]]))
