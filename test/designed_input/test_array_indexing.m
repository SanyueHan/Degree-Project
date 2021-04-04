a = [1 2 3 4;
     5 6 7 8;
     9 10 11 12;
     13 14 15 16]

% single argument indexing
b = a(:)
c = a([1 4 5 6 6 6 6])
d = a([1 2 3 4]')
e = a([1 2; 3 4])

% double arguments indexing
f = a(3, 4)
g = a(:, :)
h = a([1 2 3 3], [2 4 4])
i = a([1 2; 3 4], [1 2; 3 4])
