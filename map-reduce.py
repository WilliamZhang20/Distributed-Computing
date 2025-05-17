import dask.bag as db

"""
Here, we do map-reduce using a dask bag
It is a parallel data structure with map & reduce methods
"""
def lazyMapReduce():
    # Sample data: list of sentences
    data = [
        "foo bar foo",
        "bar baz foo",
        "baz foo bar"
    ]

    bag = db.from_sequence(data, npartitions=2)

    # Map: split sentences into words
    words = bag.map(lambda x: x.split())

    # Flatten list of lists to words stream
    flat_words = words.flatten()

    # Map: (word, 1)
    word_ones = flat_words.map(lambda w: (w, 1))

    # Reduce: count word occurrences by summing 1's
    word_counts = word_ones.foldby(
        key=lambda x: x[0],         # key = word
        binop=lambda acc, x: acc + x[1],  # sum counts
        initial=0,
        combine=lambda a, b: a + b
    )

    print(word_counts.compute())

from dask import delayed, compute
from collections import defaultdict

"""
More low-level, direct simulation of the MapReduce pipeline
Controls task execution using dask.delayed
"""

@delayed
def read_data():
    return [
        "foo bar foo",
        "bar baz foo",
        "baz foo bar"
    ]

@delayed
def map_words(lines):
    mapped = []
    for line in lines:
        for word in line.split():
            mapped.append((word, 1))
    return mapped

@delayed
def shuffle_and_group(mapped):
    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)
    return grouped

@delayed
def reduce_counts(grouped):
    return {word: sum(counts) for word, counts in grouped.items()}

def fullMapReduce():
    lines = read_data()
    mapped = map_words(lines)
    grouped = shuffle_and_group(mapped)
    result = reduce_counts(grouped)
    print(result.compute())

if __name__ == "__main__":
    # To keep main module well-defined, we have this guard
    # This avoids recursive process spawning...which would break the scheduler
    lazyMapReduce()
    fullMapReduce()