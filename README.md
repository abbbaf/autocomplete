# Autocomplete
A python module for creating a list with autocomplete support

## How to use?

import autocomplete
a = autocomplete()

## Methods:

### addFile(filename,separator)
Adds the content of the filename as list items.
separator - The character separator between the item in the file (default: ,)

### add(item)
Adds a single item

### contains(item)
Checks if the list contains an item

### remove(item)
Removes an item from the list

### search(prefix)
Returns a list of all items starting with prefix

