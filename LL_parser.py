from Global import POS

class parser:
    #context-free grammar (simple version)
    grammar = {"S": [["VP"], ["VP", "NP"]],
               "NP": [[POS.noun, POS.det], [POS.noun], ["NP", POS.adj]],
               "VP": [[POS.verb], ["VP", POS.adv]]
               }

    #parse table for above CFG
    parse_table = {POS.det: ("NP", grammar["NP"][0]),
                   POS.noun: ("NP", grammar["NP"][1]),
                   POS.adj: ("NP", grammar["NP"][2]),
                   POS.verb: ("VP", grammar["VP"][0]),
                   POS.adv: ("VP", grammar["VP"][1])
                   }
    
    #punctuation map
    punc_map = {".": "statement",
                "!": "statement",
                "?": "question"
                }
    

    #stack metasymbols
    meta_to_nonterm = {"#EOS#": "S",
                       "#EON#": "NP",
                       "#EOV#": "VP"
                       }
    nonterm_to_meta = {"S": "#EOS#",
                       "NP": "#EON#",
                       "VP": "#EOV"
                       }

    #outputs the parsed sentence as a dictionary
    #identifying agent, action, theme, sentence type (question/statement/command
    @staticmethod
    def parse(str):
        grammar = parser.grammar
        parse_table= parser.parse_table
        punc_map = parser.punc_map
        meta_to_nonterm=parser.meta_to_nonterm
        nonterm_to_meta = parser.nonterm_to_meta
        stack, input = ["#EOS#"], str.split()
        output = {}

        firstPOS = POS.getPOS(input[0])
        if POS.verb in firstPOS: 
            stack.append("#EOV#")
            stack.extend(grammar["S"][0])
            output["agent"] = "You"
            output["type"] = "command"
        elif POS.det in firstPOS or POS.noun in firstPOS or POS.adj in firstPOS: 
            stack.append("#EON#")
            stack.extend(grammar["S"][1])
        else: 
            print "POS of first word:",firstPOS
            return {}
        
        i, startmark = 0, 0
        while i < len(input):
            word, peek = input[i], stack.pop()
            pos = POS.getPOS(word)[0]

            if peek == pos: i+=1 

            elif peek in meta_to_nonterm:
                nonterm = meta_to_nonterm[peek]

                if nonterm == "NP": output["agent"] = input[startmark: i]
                elif nonterm == "VP": output["action"] = input[startmark:i]
                else: output["type"] = punc_map[input[i]]
                startmark = i

            else:
                try: 
                    production = parse_table[pos]
                except KeyError:
                    print "Word we just failed on: '%s'."%(word,)
                    exit(1)
                if production[0] == peek: 
                    stack.append(nonterm_to_meta[peek])
                    stack.extend(production[1])
                else: 
                    print "Word is '%s', peek is '%s', pos is '%s'."%(word,peek,pos)
                    print "Production is '%s'"%(production,)
                    return {}
        return output
