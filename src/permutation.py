# from itertools import permutations;

# my_list = [1]*3

# list_of_permutations = permutations(my_list);
# cnt = 0;
# for p in list_of_permutations:
#     cnt += 1;
# print(cnt);
import cProfile;

def factorial(n):
    if n <= 1:
        return n;
    else:
        return factorial(n-1)*n;

def counter(n):
    cnt = 0;
    for i in range(n):
        cnt += 1;
    return cnt;



print(factorial(26))
print(counter(403291461126605635584000000))
# cProfile.run("counter(factorial(26))");

# this poses the complexity of O 2^n
