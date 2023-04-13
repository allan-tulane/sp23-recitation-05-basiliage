import random, time
import tabulate


def qsort(a, pivot_fn=None):
    ## TO DO
  if len(a)<=1:
    return a
  else:
    if pivot_fn != None:
      pivot_fn = a[0]
      
    less = [x for x in a[1:] if x <= pivot_fn]
    greater = [x for x in a[1:] if x > pivot_fn]
    return qsort(less, pivot_fn) + [pivot] + q(greater, pivot_fn)
   
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
  qsort_fixed_pivot = qsort(sizes,"teehee")
  qsort_random_pivot = qsort(sizes)
  result = []
  for size in sizes:
    # create list in ascending order
    mylist = list(range(size))
    # shuffles list if needed
    random.shuffle(mylist)
    result.append([
    len(mylist),
        time_search(qsort_fixed_pivot, mylist),
        time_search(qsort_random_pivot, mylist),
        
        ])
    return result
    ###
def ssort(L):
  for i in range(len(L)):
    print(L)
    m = L.index(min(L[i:]))
    L[i], L[m] = L[m], L[i]
  return L

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
