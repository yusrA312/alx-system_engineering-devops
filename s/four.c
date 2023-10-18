#include "main.h"
/**
 * _strncmp - This program compares the first n characters of two strings.
 * @s1: First string to be compared.
 * @s2: Second string to be compared.
 * @n: Number of characters to compare.
 * Return: Negative, positive, or zero integer.
 */
int _strncmp(char *s1, char *s2, size_t n)
{
	size_t u;
	int diff;

	for (u = 0; u < n; u++)
	{
		diff = s1[u] - s2[u];
		if (diff > 0 || diff < 0)
			return (diff);
	}
	return (0);
}

/** 
 * _strchr - Entry point 
 * @s: input 
 * @c: input 
 * Return: Always 0 (Success) 
 */ 
char *_strchr(char *s, char c) 
{ 
	int i = 0; 

	for (; s[i] >= '\0'; i++) 
	{ 
		if (s[i] == c) 
			return (&s[i]); 
	} 
	return (0); 
}
