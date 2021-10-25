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

# for i in range(1,10):
#     print(factorial(i));

def counter(n):
    cnt = 0;
    for i in range(n):
        cnt += 1;
    return cnt;


cProfile.run("counter(factorial(13))")


# cProfile.run();
