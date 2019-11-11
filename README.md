# R-tree-implementation-python-

The program builds an R-tree in memory from the dataset. 

Query efficiency as follows:  

• First, the program displays the time of reading the entire dataset once. This time serves as the sequential-scan benchmark to be compared with the cost of your query
algorithms that leverage the R-tree.

• [Range Query Testing] Given a set of 100 range queries in a text file whose format is:

x 1 x’ 1 y 1 y’ 1

x 2 x’ 2 y 2 y’ 2

...

x 100 x’ 100 y 100 y’ 100

That is, each line specifies a query whose rectangle is [x, x0] × [y, y0]. 

The program outputs

– to a disk file the number of points returned by each query-note: we need only the number of points retrieved, instead of the details of those points.

– the total running time of answering all the 100 queries, and the average time of each query (i.e., divide the total running time by 100).
