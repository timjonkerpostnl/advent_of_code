G = {i + j * 1j: c for i, r in enumerate(open('input.txt'))
     for j, c in enumerate(r) if c in '.S'}

N = 131

done = []
todo = {x for x in G if G[x] == 'S'}

for s in range(int(2.5 * N) + 1):
    if s % N == N // 2:
        done.append(len(todo))

    todo = {
        p + d
        for d in {1, -1, 1j, -1j} # Move 1 step in every direction
        for p in todo
        if (p + d).real % N + (p + d).imag % N * 1j in G # Check that new position is not a rock and we can use the repetition of the graph
    }

f = lambda n, a, b, c: a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))
print(f(26501365 // N, *done))
