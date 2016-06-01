/*
	required:
		https://developer.nvidia.com/cuda-downloads
	compile:
		nvcc -shared -o bitonic.dll bitonic.cu
*/

#include <stdlib.h>
#include <stdio.h>

__device__ inline void swap(float &a, float &b)
{
	float temp = a;
	a = b;
	b = temp;
}

__global__ void bitonic_sort_core(float *device_array, int length)
{
	// Gets the if of thread and its index in array:
	int i = threadIdx.x + blockDim.x * blockIdx.x;
	// The number of iterations = log_2(length)
	for (int iteration = 2; iteration <= length; iteration <<= 1) {
		for (int shift = iteration >> 1; shift > 0; shift >>= 1) {
			// The little hack. The shift is always equals 2^n, so there are two situations:
			// 1) i       = xxxx0xxx 
			//    shift   = 00001000
			//    i^shift = xxxx1xxx = i + shift, just like add shift
			//
			// 2) i       = xxxx1xxx 
			//    shift   = 00001000
			//    i^shift = xxxx0xxx = i - shift, i.e. i = j + shift, and then j was processed
			int i_shifted = i ^ shift;
			// i_shifted > i is corresponding to the first case:
			if (i_shifted > i) {
				// Sets the direction of bitonus subsequence:
				// 1) for a first iteration the direction is changing every 2th element
				// 2) for a second iteration the directions is changing every 4th element
				// ...
				if ((i & iteration) != 0) {
					if (device_array[i] < device_array[i_shifted]) {
						swap(device_array[i], device_array[i_shifted]);
					}
				}
				else {
					if (device_array[i] > device_array[i_shifted]) {
						swap(device_array[i], device_array[i_shifted]);
					}
				}
			}
			__syncthreads();
		}
	}
}

extern "C" __declspec ( dllexport ) void bitonic_sort(float *memory_array, int length)
{
	float *device_array;
	size_t size = length * sizeof(float);

	cudaMalloc((void**) &device_array, size);
	cudaMemcpy(device_array, memory_array, size, cudaMemcpyHostToDevice);

	// Calculates the number of threads:
	int count_threads = min(length, 1024);
	int count_blocks = length / count_threads;

	// Inits the dimensions of threads and blocks
	dim3 blocks(count_blocks,1); 
	dim3 threads(count_threads,1);

	// Call the device function
	bitonic_sort_core<<<blocks, threads>>>(device_array, length);

	cudaMemcpy(memory_array, device_array, size, cudaMemcpyDeviceToHost);
	cudaFree(device_array);
}