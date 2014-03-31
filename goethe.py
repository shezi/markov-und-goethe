from markov import markov_matrix, simulate

# get the following files from Project Gutenberg (numbers are IDs)
# preprocess them to be clean and nice!
files = [
    'p-g-2229.txt',
    'p-g-2230.txt',
    'p-g2403.txt',
    'p-g2404.txt',
    'p-g2407.txt',
    'p-g2408.txt',
    'p-g5325.txt',
]

lines = []

for filename in files:
    with open(filename, 'r') as f:
        lines.extend(map(lambda s: s.strip(), f.readlines()))

m = markov_matrix(lines, n=4)
for i in range(50):
    print(simulate(m))