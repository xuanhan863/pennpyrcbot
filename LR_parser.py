import defs, Global

grammar = {1: ("S", ["VP"]),
           2: ("S", ["NP", "VP"]),
           3: ("NP", [POS.noun]),
           4: ("NP", [POS.det, "NP"]),
           5: ("NP", [POS.adj, "NP"]),
           6: ("VP", [POS.verb]),
           7: ("VP", ["VP", "NP"]),
           8: ("VP", [POS.adv, "VP"]),
           9: ("VP", ["VP", POS.adv])
           }

actions = {POS.verb: {0: ("shift", 3),
                      3: ("reduce", [6]),
                      5: ("reduce", [3]),
                      8: ("reduce", [4, 5, 7]),
                      9: ("reduce", [9]),
                      10: ("reduce", [2, 8])
                      },
           POS.adv: {0: ("shift", 4),
                     1: ("shift", 10),
                     3: ("reduce", [6]),
                     5: ("reduce", [3]),
                     8: ("reduce", [4, 5, 7]),
                     9: ("reduce", [9]),
                     10: ("reduce", [2, 8])
                     },
           POS.noun: {0: ("shift", 5),
                      3: ("reduce", [6]),
                      5: ("reduce", [3]),
                      8: ("reduce", [4, 5, 7]),
                      9: ("reduce", [9]),
                      10: ("reduce", [2, 8])
                      },
           POS.det: {0: ("shift", 6),
                     3: ("reduce", [6]),
                     5: ("reduce", [3]),
                     8: ("reduce", [4, 5, 7]),
                     9: ("reduce", [9]),
                     10: ("reduce", [2, 8])
                     },
           POS.adj: {0: ("shift", 7),
                     3: ("reduce", [6]),
                     5: ("reduce", [3]),
                     8: ("reduce", [4, 5, 7]),
                     9: ("reduce", [9]),
                     10: ("reduce", [2, 8])
                     }
           }
    
goto = {"VP": {0: 1,
               2: 10,
               4: 10
               },
        "NP": {0: 2,
               1: 8,
               6: 8,
               7: 8
               }
        }

endofinput = [".", "!", "?"]


def parse(str)
    stack, outbuff = [0], []
    output = {}
    str = str.split()

    for substr in str:
        if substr in endofinput:
            if substr == "." or substr == "!": output["type"] = "statement"
            else: output["type"] = "question"
            return output

        state = stack.pop()
        word = lookup(substr)
        pos = word.POS

        try:
            todo = actions[state][pos]

            if todo[0] == "shift": 
                outbuff.append(word)
                reducebuff.append(word)
                stack.push(state)
                stack.push(todo[1])
                continue

            else:
                rules = todo[1]
                if len(rules) == 1: nonterm, term = grammar[rules[0]]
                else: 
                    if POS.adj in outbuff: nonterm, term = grammar[5]
                    elif POS.det in outbuff: nonterm, term = grammar[4]
                    elif POS.adv in outbuff: nonterm, term = grammar[8]
                    else: nonterm, term = grammar[7]
                        

                    else: return {}
        
        except KeyError: print "Ungrammatical input"
        
            
        
    

 
