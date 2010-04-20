import os, cPickle

class POS:
        noun, verb, adj, adv, det, null = range(6)

def outOfDate(product,deps):
        if not os.path.exists(product):
                return True
        for dep in deps:
                if os.stat(product)[8] < os.stat(dep)[8]:
                        return True
        return False

def loadFile(fname):
        tmp=open(fname, "rb")
        ret=cPickle.load(tmp)
        tmp.close()
        return ret
