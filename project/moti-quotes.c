#include "Quotes.h"

#define NUM_QUOTES 5

/**
 * motivate - A function that contains 5 motivational quotes
 * Description - Contains 5 motivational quotes
 * Return: 0 Success (Always)
 */

const char *motivate(void)
{
	const char *quotes[NUM_QUOTES] = {
    "\"It takes courage to grow up and become who you really are.\" — E.E. Cummings",
    "\"Nothing is impossible. The word itself says 'I'm possible!'\" — Audrey Hepburn",
    "\"Believe you can and you're halfway there.\" — Theodore Roosevelt",
    "\"There is no better compass than compassion.\" — Amanda Gorman", 
    "\"You can’t turn back the clock. But you can wind it up again.\" — Bonnie Prudden"
	};
	int index;

	srand(time(NULL));
	index = rand() % NUM_QUOTES;

	return quotes[index];
}
