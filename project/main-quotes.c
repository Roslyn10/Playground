#include "Quotes.h"

/**
 * main - The main entry point of the porject
 * Description - Entry point of the project
 * Return: 0 Success (Always)
 */

int main(void)
{
    const char* m1 = motivate();
    const char* l1 = love();
    printf("Motivation: %s\n", m1);
    printf("Love: %s\n", l1);
    return (0);
}
