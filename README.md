# Search algorithms

## Task 1

Add a `delete` method for removing key-value pairs in the `HashTable` implemented in the lecture notes.

## Task 2

Implement binary search for a sorted array of floating-point numbers. The function for binary search should return a tuple where the first element is the number of iterations needed to find the element. The second element should be the "upper bound" — the smallest element that is greater than or equal to the given value.

## Task 3

Compare the efficiency of the substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files ([article 1](./article_1.txt), [article 2](./article_2.txt)). Using `timeit`, measure the execution time of each algorithm for two types of substrings: one that actually exists in the text, and another — invented (substring selection at your discretion). Based on the obtained data, determine the fastest algorithm for each text separately and overall.

| Підрядок                           | Алгоритм          |   Стаття 1       |   Стаття 2       |
|-----------------------------------:|------------------:|------------------|------------------|
| алгоритмів                         | Boyer-Moore       | 0.004926 seconds | 0.010501 seconds |
| алгоритмів                         | Knuth-Morris-Pratt| 0.041216 seconds | 0.076980 seconds |
| алгоритмів                         | Rabin-Karp        | 0.070307 seconds | 0.125616 seconds |
| неіснуючий підрядок для тестування | Boyer-Moore       | 0.005779 seconds | 0.008686 seconds |
| неіснуючий підрядок для тестування | Knuth-Morris-Pratt| 0.051333 seconds | 0.091194 seconds |
| неіснуючий підрядок для тестування | Rabin-Karp        | 0.092191 seconds | 0.189415 seconds |

## Висновки:

**Boyer-Moore** є найефективнішим алгоритмом для пошуку коротких і довгих підрядків у великих текстах. Він має найменші часи виконання у всіх тестах.

**Knuth-Morris-Pratt** повільніший за **Boyer-Moore**. Він показав добрі результати для коротких підрядків, але значно повільніший для довгих підрядків.

**Rabin-Karp** є найменш ефективним алгоритмом у даних тестах. Його час виконання значно перевищує **Boyer-Moore** і **Knuth-Morris-Pratt** у всіх випадках.