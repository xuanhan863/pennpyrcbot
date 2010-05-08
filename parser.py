import lex, yacc, res
from  Global import *
from Types import *
from semantics import *

#--------------------
#lexer definitions
#--------------------

tokens = (
    'TO', #for infinitives
    'WH', #wh question words
    'AUX', #auxiliary verbs not including forms of "to be"
    'COP', #the copula "to be"
    'DET',
    'NOUN',
    'ADJ',
    'ADV',
    'VERB',
    )

literals = ['.', '?']

t_TO = r'to'

def t_WH(t):
    r'@wh_[a-zA-Z]+'
    t.value = t.value[4:]
    return t

def t_AUX(t):
    r'@aux_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_COP(t):
    r'@cop_[a-zA-Z]+'
    t.value = t.value[5:]
    return t

def t_DET(t):
    r'@det_[a-zA-Z]+'
    t.value = t.value[5:]
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


lexer = lex.lex()

#--------------------
#lexer testing --->this part already works!<---
#--------------------

#lexer.input("@det_a @adj_happy @noun_cook @adv_rapidly @verb_sliced @det_the @noun_radishes .")
#while True:
#    token = lexer.token()
#    if not token: break
#    print token.type, token.value


#--------------------
#parser definitions
#--------------------

#These consist of assigning to p[0], which represents the nonterminal on the left, a value generated from the values of the terminals and nonterminals on the right (p[1]...p[n]).  The value of a terminal is just the string representing its word (not a Word object yet!); the value of a nonterminal should be a semantic class object with the same name as the nonterminal symbol. 

#See grammar.txt for an easier to read version of the grammar (note that in grammar.txt nonterminals are capitalized and terminals are not, whereas here nonterminals are all lowercase and terminals are allcaps).

#See semantics.py for definitions of the classes I keep assigning to p[0]'s.

#Hopefully I remembered to call lookup() whenever I create semantic class objects from terminals.

def p_sentence(p):
    '''sentence : statement '.'
                | question '?' '''
    p[0] = p[1]

def p_statement(p):
    'statement : dp vprime'
    # ^p[0]     ^p[1] ^p[2]
    p[0] = Statement(Agent(p[1]), Action(p[2]), p[2].predicate)

def p_question(p):
    '''question : AUX dp vprime
                | WH AUX dp vprime
                | WH COP dp predp'''
    if len(p) == 4: p[0] = Question(Agent(p[2]), Action(p[3]), p[3].predicate, "tf")
    elif p[2].type == 'AUX': p[0] = Question(Agent(p[3]), Action(p[4]), p[4].predicate, p[1])
    else:
#        first = Question(Agent(p[3]))
        p[0] = Question(Agent(p[3]), Action(VPrime(VP(None, VNaught(lookup(p[2])), p[4])), p[4], p[1]))

def p_dp(p):
    '''dp : DET np
          | np'''
    if len(p) == 3: p[0] = DP(lookup(p[1]), p[2])
    else: p[0] = DP(None, p[2])

def p_np(p):
    '''np : NOUN
          | ADJ NOUN'''
    if len(p) == 2: p[0] = NP(None, lookup(p[1]))
    else: p[0] = NP(lookup(p[1]), lookup(p[2]))

def p_vnaught(p):
    '''vnaught : VERB
               | COP'''
    p[0] = VNaught(lookup(p[1]))

def p_vp(p):
    '''vp : ADV vnaught
          | vnaught'''
    if len(p) == 3: p[0] = VP(lookup(p[1]), p[2])
    else: p[0] = VP(None, p[1])

def p_vprime(p):
    '''vprime : vp predp
              | vp'''
    if len(p) == 3: p[0] = VPrime(p[1], p[2])
    else: p[0] = VPrime(p[1], None)

def p_predp(p):
    ''' predp : TO VERB
              | ADJ
              | dp'''
    if len(p) == 3: p[0] = Predicate("infinitive", lookup(p[2]))
    else:
        try: 
            if p[1].type == 'ADJ': p[0] = Predicate("linked", lookup(p[1]))
        except AttributeError: p[0] = Predicate("theme", p[1])

def p_error(p): print "Syntax error at '%s'" % p.value 


#--------------------
#parser testing
#--------------------
parser = yacc.yacc(debug=True)
sentence = parser.parse("@det_a @adj_happy @noun_cook @adv_rapidly @verb_sliced @det_the @noun_radishes .")
print res.main(sentence)


