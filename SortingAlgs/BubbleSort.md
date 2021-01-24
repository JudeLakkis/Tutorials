<h1 align="center">Bubble Sort</h1>

## Humble Beginnings

Ah bubble sort, everyones first sorting algorithm...

Bubble sort is a simple algorithm used for sorting linear data structures such as arrays. It works by repeatedly swapping neighboring elements until all the elements have been sorted.

If you don't quite get it, here is a nice gif showing you how it works:

![https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif](https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif)

Ok so that's simple enough, but how would you code this up?

## Bubble Code

So we will take the same array of numbers as the gif above and work with that for our example

```python
array = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(array):
<<<<<<< HEAD
	n = len(array)
	for i in range(n):
		for j in range(0, n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1 = array[j+1], array[j]
	return array
=======
    n = len(array)
    for i in range(n):
    	for j in range(0, n-i-1):
		if array[j] > array[j+1]:
			array[j], array[j+1 = array[j+1], array[j]
>>>>>>> cc2372dde2a739658b977c02e7e0db9e162ca851
```

Ok so incase some of that isn't very clear, let's breakdown a couple of the lines.

For the line `for j in range(0, n-i-1):` we are subtracting `i` as we know that the final value after each iteration will be the largest and therefore doesn't need the extra comparison. We also subtract a 1 as to not try and swap the value next to said fixed value.

Then the final line of code is just a nice feature that Python has built in which allows us to swap two variables without the need of a third. It's ugly, slow, and rather stupid, but if you wanted to do it that way here you go:

```python
var1 = value1
var2 = value2
var3 = value1

var1 = var2
var2 = var3
var3 = None
```

### Time Complexity
| Complexity   | Comparisons | Swaps  |
|--------------|-------------|--------|
| Worst Case   | O(n^2)      | O(n^2) |
| Average Case | O(n^2)      | O(n^2) |
| Best Case    | O(n)        | O(1)   |

## Final Thoughts

Bubble sort is a great place to start when learning about sorting algorithms and because of its simplicity can be very quickly implemented. It is however incredibly slow, and I wouldn't recommend using it as a main form of sorting.
