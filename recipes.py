# compose
var=10
compose_parameters = [ str, float, var]
reduce(lambda x, y: y(x), reversed(compose_parameters))

# First element in the list 
l = [1,2,3,4,5,6,7,8,9]
isinstance(l, collections.abc.Iterable) and next(iter(l), Flase)

# merge any clase of iteretor
itertools.chain(map(lambda x: x**2,l), map(lambda x: x**2, l), l, tuple(l))

# variables global on the map function
h = lambda x,y,z:x+y+z
a =1
b=2
map(partial(h, a,b),l)

