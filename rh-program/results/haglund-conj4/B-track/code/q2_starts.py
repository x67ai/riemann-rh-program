"""starts for the Q2 tracking: non-real zeros of Xi_N in q2-zeros.json with Re in [a, b]"""
import sys, json
N = int(sys.argv[1]); a = float(sys.argv[2]); b = float(sys.argv[3])
Z = json.load(open('../data/q2-zeros.json'))
s = [z for z in Z['N%d' % N]['zeros'] if a <= float(z[0]) <= b]
json.dump(s, open('../data/q2-starts-k%d.json' % N, 'w'))
print(len(s), s)
