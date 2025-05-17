# Distributed Computing

In this project, I implement distributed algorithms leveraging different parallel computing libraries, which have a very wide variety of important applications, such as machine learning, data science, and scientific computing.

The parallelization of those algorithms, helped by the ubiquity of multicore/massively parallel processors, the infrastructure of distributed computing, and optimally efficient task scheduling, has made them feasible for those applications at a large scale, advancing humanity's innovation.

So far, I use Python's [Dask](https://www.dask.org/) distributed computing library, which is super efficient. I previously used Dask for [image processing](https://github.com/WilliamZhang20/Object-Detection) to process multiple images at once.

## Parallel Paradigms

One feature of Dask that I use frequently is lazy evaluation, which brings major performance benefits.

1. It reduces unecessary computation, by invoking it only when needed
2. Improves memmory efficiency, by avoiding heavy occupancy of memory when the task is not needed yet.
3. The decoupling of the lazy task from the main thread can allow for more fine-grained control over the workflow.

I hope to also implement the algorithms again from scratch in C++, and redo it again leveraging Go's multiprocessing paradigms. 

## List of Algorithms

The list of algorithms is below.
- [x] Fibonacci
- [x] Merge sort
- [x] Stencil algorithm
- [x] Map Reduce
- [ ] Page Rank
- [ ] Barnes-Hut Algorithm
- [ ] Knapsack Problem
- [ ] Viterbi Algorithm
- [ ] Fast Fourier Transform
- [ ] Finite-Element Analysis