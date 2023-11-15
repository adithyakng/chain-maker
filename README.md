# Example Usage:

> Go to https://vanya.jp.net/vtree/ and copy paste the output to visualize the chain
> As expected, we get the following chains:
* attack1->attack2->attack3
* attack1->attack4

#### This is because:
1) The initState passed to the makeChain method is the same as the initState of attack1. 
2) The initState for attack2 and attack4 are the same as the endSate of attack1.