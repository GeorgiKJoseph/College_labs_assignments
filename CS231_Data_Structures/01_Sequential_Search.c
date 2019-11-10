//Georgi K Joseph
//S3-D
//21

//source code...

#include <stdio.h>

int seqSearch(int arr[], int s, int ele) {
	int i;

	for (i=0; i<s; i++) {
		if (arr[i] == ele) {
			return (i+1);
		}
	}
	return (0);
}
int main() {
	int i=0, found=0, array[100], size, element;

	printf("Enter number of elements : ");
	scanf("%d", &size);

	printf("Enter elements\n");
	for (i=0; i<size; i++) {
		scanf("%d", &array[i]);
	}

	printf("Enter element to search : ");
	scanf("%d", &element);

	found = seqSearch(array, size, element);

	if (found) {
		printf("Element found at position %d\n", found);
	} else {
		printf("Element not found\n");
	}
}
