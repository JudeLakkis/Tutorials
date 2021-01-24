<h1 align="center">Selection Sort</h1>

## How does it work?

Selection sort is sorting algorithm which repeatedly search for the smallest item in the array, and moving it to the beginning. By doing this you are essentially creating two sub arrays inside your main array, the first being the sorted smaller values, and the other being the unsorted values.

Each iteration of selection sort the algorithm moves a single new value to into the sorted sub array.

So how would you go about coding this out?

## Selective Coding

Selection sort can look a little messy so I'm going to write out the variables to be as clear as possible to hopefully make it somewhat clearer.

```python
array = [6, 5, 3, 1, 8, 7, 2, 4]

def selection_sort(array):
	N = len(array)
	for i in range(N):
		minimum_index = i

		for unsorted in range(i+1, N):
			if array[minimum_index] > array[unsorted]:
				minimum_index = unsorted

		array[minimum_index], array[i] = array[i], array[minimum_index]
	return array
```

So what exactly is going on here?

Our first for loop iterates through every item in the array a single time, as we don't need to loop over our sorted values again once we are done with them. This is also why our second for loop starts from one position ahead of the first and goes to the end of the list. We need to compare the up coming items not our sorted ones.

We then use our comparator to check if the minimum value is currently greater than our current unsorted item, and if it is we store that index.

When we have looped through all our unsorted values, we swap the smallest value with the value closest to our sorted sub array, and repeat the process.

## Time Complexity

| Complexity   | Comparisons | Swaps |
|--------------|-------------|-------|
| Worst Case   | O(n^2)      | O(n)  |
| Average Case | O(n^2)      | O(n)  |
| Best Case    | O(n^2)      | O(1)  |

## Final Thoughts

Selection sort isn't a bad sorting algorithm, it is kind of comparable to bubble sort if not pretty much identical when it comes to time complexity. Overall it looks somewhat more impressive than bubble sort but doesn't stack up too well against the other sorting algorithms.

You'll run into this during exams quite often as a way to throw you off because it isn't bubble sort and isn't all that difficult to understand, so be wary of that.
