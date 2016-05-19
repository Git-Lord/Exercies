#include <iostream>
#include <stdlib.h>
extern "C" int calculateMinimum(int len, int* array);

int main(int argc, char **argv) {
	int *array = new int[argc];
	//There is no checking for errors, just for sake of my lovely time:
	for (int i = 1; i < argc; i++) {
		array[i] = atoi(argv[i]);
	}
	if (argc > 1) {
		std::cout << "The sum: " << calculateMinimum(argc, array) << std::endl; 
	}
	else {
		std::cout << "No numbers were inputed :(" << std::endl;
	}
	
}

//Compite: g++ main.cpp -o main -l:lib.so