i#include "main.h" 
/** 
 * _strcmp - compare string values 
 * @s1: input value 
 * @s2: input value 
 * 
 * Return: s1[i] - s2[i] 
 */ 
int _strcmp(char *s1, char *s2) 
{ 
	int i; 

	i = 0; 
	while (s1[i] != '\0' && s2[i] != '\0') 
	{ 
		if (s1[i] != s2[i]) 
		{ 
			return (s1[i] - s2[i]); } 
		i++; 
	} 
	return (0); 
}
/**
 * _strlen - returns the length of a string
 * @s: string
 * Return: length
 */
int _strlen(char *s)
{
	int longi = 0;

	while (*s != '\0')
	{
		longi++;
		s++;
	}

	return (longi);
}

char *simulate_getenv(const char *varname, char *envp[]) 
{
	int i;
	char *env_var, *value;

	if (varname == NULL || envp == NULL) 
		return (NULL);

	for (i = 0; envp[i] != NULL; i++) 
	{
		env_var = envp[i];

		if (strncmp(env_var, varname, strlen(varname)) == 0)
		{
			value = strchr(env_var, '=');
			if (value != NULL) 
				return (value + 1);
		}
	}

	return (NULL);
}
