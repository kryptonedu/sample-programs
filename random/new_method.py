class A(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print "EXISTS"
            return A._dict['key']
        else:
            print "NEW"
            return super(A, cls).__new__(cls)

    def __init__(self):
        print "INIT"
        A._dict['key'] = self
        print ""
A()
A()
A()
