#include "Quotes.h"

#define NUM_QUOTES 5

/**
 * success - A function that contains 5 success quotes
 * Description - Contains 5 success quotes
 * Return: 0 Success (Always)
 */

const char *success(void)
{
	const char *quotes[NUM_QUOTES] = {
	       "\"The question isn’t who is going to let me, it’s who is going to stop me\". – Ayn Rand"
	};
	int index;

	srand(time(NULL));
	index = rand() % NUM_QUOTES;

	return index[quotes];
}
