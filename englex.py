import lex

tokens = (
    'AND',
    'BUT',
    'TO',
    'AUX',
    'WH',
    'COP',
    'DET',
    'NUM',
    'NOUN',
    'ADJ',
    'ADV',
    'VERB'
    )

literals = ['.', '!', '?']

t_AND = r'and'

t_BUT = r'but'

t_TO = r'to'

def t_AUX(t):
    r'@aux_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_WH(t):
    r'@wh_[a-zA-Z]+'
    t.value = t.value[4:]
    return t

def t_COP(t):
    r'@cop_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_DET(t):
    r'@det_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NOUN(t):
    r'@noun_[a-zA-Z]+'
    t.value = t.value[6:]
    return t

def t_ADJ(t):
    r'@adj_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_ADV(t):
    r'@adv_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_VERB(t):
    r'@verb_[a-zA-Z]+'
    t.value = t.value[6:]
    return t    

t_ignore = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


#--------------------
#testing
#--------------------

#lexer = lex.lex()
#lexer.input("1 @adj_happy @noun_cook @adv_rapidly @verb_sliced @det_the @noun_radishes .")
#while True:
#    token = lexer.token()
#    if not token: break
#    print token.type, token.value
