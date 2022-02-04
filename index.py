# Python program to find Index
# of B to be replaced with A to get
# longest continuous sequence
# of As in a binary array

# Returns index of B to be
# replaced with A to get longest
# continuous sequence of As.
# If there is no B in array, then
# it returns -1.

# B
def max_A_index(arr,n):
	
	# for maximum number of A around B
	max_count = 0

	# for storing result
	max_index =0

	# index of previous B
	prev_b = -1

	# index of previous to previous B
	prev_prev_b = -1

	# Traverse the input array
	for curr in range(n):
	
		# If current element is B,
		# then calculate the difference
		# between curr and prev_prev_b
		if (arr[curr] == 'B'):
		
			# Update result if count of
			# 1s around prev_b is more
			if (curr - prev_prev_b > max_count):
			
				max_count = curr - prev_prev_b
				max_index = prev_b
			

			# Update for next iteration
			prev_prev_b = prev_b
			prev_b = curr

	# Check for the last encountered B
	if (n-prev_prev_b > max_count):
		max_index = prev_b

	return max_index

# Driver program

arr = ['A','A','B','B','A','B','A','A','A','B','A','A','A','A']
n = len(arr)
print("The string is : ")
for i in arr :
    print(i ,end = " ")

print("\n\nIndex of B to be replaced is ",
	max_A_index(arr, n))


