import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)
    yield -1


def KnuthMorrisPratt(text, pattern):
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
                matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos
    else:
        yield -1
            

txt1 = """ANZ535-292000-
Tidal Potomac from Key Bridge to Indian Head-
1038 AM EDT Tue Jun 29 2021

REST OF TODAY
SW winds 5 to 10 kt. Waves 1 ft.

TONIGHT
S winds 5 to 10 kt. Waves 1 ft.

WED
SW winds 5 to 10 kt. Waves 1 ft.

WED NIGHT
SW winds around 5 kt. Waves 1 ft. A chance of showers
and tstms.

THU
SW winds around 5 kt. Waves 1 ft. Showers with a chance of
tstms.

THU NIGHT
SW winds 5 kt. Waves less than 1 ft. Showers with tstms
likely.

FRI
W winds around 5 kt. Waves 1 ft. Showers. A chance of tstms
through the night, then a chance of showers after midnight.

SAT
N winds around 5 kt. Waves 1 ft. A chance of showers. 

Winds and waves higher and visibilities lower in and near tstms.
"""


@timer
def test_findall(txt1):
    f = findall( "winds", txt1)
    pos = next(f)
    while ( pos > 0 ):
        print("pos: ", pos )
        pos = next(f)
        
@timer 
def test_findkmp(txt1):
    f = KnuthMorrisPratt( txt1, "winds")
    pos = next(f)
    while ( pos > 0 ):
        print("pos: ", pos )
        pos = next(f) 
        
findall1 = findall("advisory", txt1)

print(next(findall1))

knp1 = KnuthMorrisPratt(txt1, "advisory")

print(knp1)
print(next(knp1))

test_findall(txt1)

test_findkmp(txt1)


findall1 = findall("winds", txt1)

print(next(findall1))

knp1 = KnuthMorrisPratt(txt1, "winds")

print(knp1)
print(next(knp1))

test_findall(txt1)

test_findkmp(txt1)