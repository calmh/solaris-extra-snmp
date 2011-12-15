#!/usr/bin/python

def decompose_oid(oid):
    return [ int(o) for o in oid.split('.')[1:] ]

def oid_compare(a, b):
    ad = decompose_oid(a)
    bd = decompose_oid(b)
    return cmp(ad, bd)

def printValue(value, oid):
    # If it's a function, call it.
    if type(value).__name__ == 'function':
        value = value(oid)
    # Otherwise assume it's a two-tuple of type and value.
    print value[0]
    print value[1]

def respond_to(operation, req_oid, result):
    result = sorted(result, key=lambda row: decompose_oid(row[0]))

    if operation == '-g':
        for oid, value in result:
            if oid == req_oid:
                print oid
                printValue(value, oid)
    elif operation == '-n':
        for oid, value in result:
            if oid_compare(oid, req_oid) == 1:
                print oid
                printValue(value, oid)
                break

