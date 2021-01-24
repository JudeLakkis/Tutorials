<h1 align="center">Insertion Sort</h1>

## Go back to where you belong!

Insertion sort is a lovely algorithm for people to understand when it comes to sorting algorithms, as it works almost exactly like how we would sort a list of numbers. Similar to selection sort, insertion sort separates the our values into two sub arrays (sorted, unsorted).

I understand that it can be a little confusing to grasp initially so here are the steps broken down:

### Steps

**Note:** *The key value is the current value being looked at*

- Start at the beginning of the list and iterate through
- Compare the key index's value to the previous item
- If the key value is smaller than the previous item move the bigger number in front
- Repeat until the array is sorted

Here it is in a nice little GIF:
![Insertion Sort GIF](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

As I said, it is pretty much how we would sort a deck of cards or a bunch or random numbers in real life. That's all fine and dandy but how would you go about coding this up for an exam/interview question?

## Inserting your code

Once again the code is a little complicated to understand so let's break it down into its most important components.

```python
array = [6, 5, 3, 1, 8, 7, 2, 4]

def insertion_sort(array):
	N = len(array)
	for i in range(1, N):
		pass # More Code
```

Our first loop starts at the second item rather than the first, and this is because we need to compare values to the previous item. If we start at our first item and try to compare backwards we would be comparing outside of the array, leading to an indexing error.

```python
array = [6, 5, 3, 1, 8, 7, 2, 4]

def insertion_sort(array):
	N = len(array)
	for i in range(1, N):
		key = array[i]
		previous = i - 1
```

We have `key` set to our current array item, and `previous` to the previous item. Now for the back looping.

```python
while previous >= 0 and key < array[previous]:
			array[previous+1] = array[previous]
			previous -= 1
```

I personally have a hatred towards while loops, but here it is very useful to continue looping with a conditional. As long as our previous index is greater than or equal to 0 and our key is smaller than the previous item we want to continue our back looping. This is the loop that keeps up moving backwards until the item is either at the beginning of the array or has been slotted in.

Finally put it all together and swap the item into it's new position and we have our insertion sort algorithm finalized!

### Final Code

```python
array = [6, 5, 3, 1, 8, 7, 2, 4]

def insertion_sort(array):
	N = len(array)
	for i in range(1, N):
		key = array[i]
		previous = i - 1

		while previous >= 0 and key < array[previous]:
			array[previous+1] = array[previous]
			previous -= 1

		array[previous+1] = key
	return array
```

## Time Complexity

| Complexity   | Comparisons | Swaps  |
|--------------|-------------|--------|
| Worst Case   | O(n^2)      | O(n^2) |
| Average Case | O(n^2)      | O(n^2) |
| Best Case    | O(n)        | O(1)   |

## Final Thoughts

Selection sort is a great algorithm to learn as it functions so similarly to how we sort things in real life, which really lets us get a deeper understanding of sorting algorithms. When it comes to time complexity, it's honestly not all that fast and is comparable to the likes of bubble and selection sort.

When it comes to exams/interview questions feel free to use this as your example sorting algorithm if you want to spice things up a little but want to keep it simple. It's not a super common algorithms that I have run into but it does the job and you can't fault it for that.
