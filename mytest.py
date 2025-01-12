def myfunc():
    if not hasattr(myfunc,'anynum'):
        myfunc.anynum = 0
    myfunc.anynum += 1
    print(hasattr(myfunc,'anynum'), myfunc.anynum)

    global w
    w = 10
    print(w)


myfunc()    # output: True 1