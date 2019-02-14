"""
dijkstras
-shortest path from one vertex to every other vertex

visited vertices
unvisited vertices

start @ starting vertex (A)
dist from A to A = 0
dist from A to every other = INF

while unvisited vertices:
1) visit unvisited vertex w/ smallest known dist
2) visit said vertices' UNVISITED neighbors and calc dist
3) if calculated dist is lower than update said distances
    -b/c of this, it is maintained that final results are the shortest distances

what we are storing is the dist from starting vertex to every other vertex
so calculating distance means dist from start to curr + from curr to neighbor
"""