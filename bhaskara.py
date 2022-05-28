def bhaskara(a, b, c):
    delta = b**2 -4*a*c

    r_1 = (-b + (delta)**(1/2))/(2*a)
    r_2 = (-b - (delta)**(1/2))/(2*a)

    return [delta, r_1, r_2]


root1 = bhaskara(-.1, .53, -.592)
root2 = bhaskara(-.01, -.126, .6031)

print(root1, root2)
