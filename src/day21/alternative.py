G = {i + j * 1j: c for i, r in enumerate(open('input.txt'))
     for j, c in enumerate(r) if c in '.S'}

N = 131

done = []
reachable_nodes = {x for x in G if G[x] == 'S'}

# We want to obtain 3 values,
# - f(0) = edge of the original graph
# - f(1) = edge of the second graph
# - f(2) = edge of the third graph
# Moving from 1 graph to the next requires N steps and moving th the edge requires N // 2 steps
for s in range(int(2.5 * N) + 1):
    if s % N == N // 2:
        done.append(len(reachable_nodes))

    reachable_nodes = {
        p + d
        for d in {1, -1, 1j, -1j} # Move 1 step in every direction
        for p in reachable_nodes
        if (p + d).real % N + (p + d).imag % N * 1j in G # Check that new position is not a rock and we can use the repetition of the graph
    }

# Use Newton polynomial on f(0) = a, f(1) = b, f(2) = c
f = lambda n, a, b, c: a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))
print(f(26501365 // N, *done))
