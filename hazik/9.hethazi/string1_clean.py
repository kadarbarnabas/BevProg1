def donuts(count):
    # TODO...
    return
def both_ends(s):
    # TODO...
    return
def fix_start(s):
    # TODO...
    return
def mix_up(a, b):
    # TODO...
    return
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))
def main():
    print('donuts')
    # Minden egyes sor megh�vja a donuts() fv.-t s �sszehasonl�tja a visszaadott
    # �rt�ket a v�rt eredm�nnyel.
    test(donuts(4), 'F�nkok sz�ma: 4')
    test(donuts(9), 'F�nkok sz�ma: 9')
    test(donuts(10), 'F�nkok sz�ma: sok')
    test(donuts(99), 'F�nkok sz�ma: sok')
    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')
    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')
    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
if __name__ == '__main__':
    main()