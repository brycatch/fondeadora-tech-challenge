# Fondeadora Tech challenge

Hello! I'm Bryan an this is my approach for the tech challenge of Fondeadora.

## Directories

In the project, we have some files

### src

It has a file `index` with three methods:

- `get_flat_array`: returns a flat array of a nested array input.
- `find_number_in_array`: recursive function to find and nest an item if this one is a number
- `validate_type_element`: make a validation if an item is either number or array. If isn't, raise an exception
- `item_is_array`: return if an element is an array

### test

I created this to make a unittest of my code. My approach was testing functionality and performance

### Other files

- `.gitignore`: template given by toptal
- `makefile`: for running commands in terminal (only for Linux based systems)
  - `test`: run tests in project
