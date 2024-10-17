#include "Quotes.h"

#define NUM_QUOTES 5
/**
 * love - A function that contains 5 love quotes
 * Description - Contains 5 love quotes
 * Return: 0 Success (Always)
 */

const char *love(void)
{
        const char *quotes[NUM_QUOTES] = {
		"\"If you find someone you love in your life, then hang on to that love.\" — Princess Diana",
		"\"Love is our true destiny. We do not find the meaning of life by ourselves alone — we find it with another.\" — Thomas Merton",
		"\"A flower cannot blossom without sunshine, and man cannot live without love.\" — Max Müller",
		"\"Who, being loved, is poor? Oh, no one. I hate my riches. They are a burden...\" ― Oscar Wilde",
		"\"Nobody has ever measured, even poets, how much a heart can hold.\" — Zelda Fitzgerald"
	};
	int index;

        srand(time(NULL));
        index = rand() % NUM_QUOTES;

        return quotes[index];
}
