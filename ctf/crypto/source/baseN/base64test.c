#include <stdio.h>
#include <string.h>
#include "base64.h"

void usage()
{
	printf("Usage: base64 [-e(encrypt)|-d(decrypt)]\n");
}

void crypt(int is_decrypt)
{
  unsigned char input[1024];
  unsigned char output[1024];
  int i;
  
  memset(input, 0, sizeof(input));
  printf("\ninput %s text:", is_decrypt ? "cipher" : "plain");
	scanf("%s", input);
  
  if (is_decrypt)
    base64_decode(input, strlen(input), output);
  else
    base64_encode(input, strlen(input), output);
    
  printf("\n%s text:%s", is_decrypt ? "plain" : "cipher", output);
}

int main(int argc, char **argv) 
{
  int is_decrypt;
  
  if(argc < 2 || argv[1][0] != '-')
	{
		usage();
		return 1;
	}
  
	switch(argv[1][1])
	{
		case 'e':
		case 'E':
      is_decrypt = 0;
			break;
    case 'd':
		case 'D':
      is_decrypt = 1;
			break;
		default:
			usage();
			return 1;
	}
  crypt(is_decrypt);
  
  return 0;
} 
