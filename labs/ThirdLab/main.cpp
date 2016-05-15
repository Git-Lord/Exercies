#include <stdlib.h>
#include <limits.h>

extern "C" int calculateMinimum(int len, int* array) {
	// Calculates the sum of the absolute values of array elements
	int sum = 0;
	for (int i = 0; i < len; i++) {
		sum += abs(array[i]);
	}

	// Builds the array of sums, which realizability we will test:
	int *available = new int[sum+1];
	for (int i = 0; i < sum+1; i++) {
		available[i] = false;
	}
	available[0] = true;

	// Checks the realizability of subsets sums:
	for (int i = 0; i < len; i++) {
		for (int j = sum - abs(array[i]); j >= 0; j--) {
			if (available[j]) {
				available[j + abs(array[i])] = true;
			}
		}
	}

	int minimum = INT_MAX;

	// Fo all sums:
	for (int i = 0; i < sum; i++) {
		// If sum is realizabile
		if (available[i]) {
			if (abs(sum - 2*i) < minimum) {
                minimum = abs(sum - 2*i);
			}
		}
	}

	return minimum;

}