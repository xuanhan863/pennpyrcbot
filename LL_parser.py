from Global import POS

class parser:

    #context-free grammar (simple version)
    grammar = {"S": [["VP"], ["NP", "VP"]],
               "NP": [[POS.det, POS.noun], [POS.noun], [POS.adj, "NP"]],
               "VP": [[POS.verb], [POS.adv, "VP"]]
               }

    #parse table for above CFG
    parse_table = {POS.det: ("NP", grammar["NP"][0]),
                   POS.noun: ("NP", grammar["NP"][1]),
                   POS.adj: ("NP", grammar["NP"][2]),
                   POS.verb: ("VP", grammar["VP"][1]),
                   POS.adv: ("VP", grammar["VP"][2])
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
    def parse(str):
        stack, input = ["#EOS#"], str.split()
        output = {}

        firstPOS = POS.getPOS(input[0])
        if POS.verb in firstPOS: 
            stack.append("#EOV#")
            stack.extend(grammar["S"][0])
            output["agent"] = "You"
            output["type"] = "command"
        elif POS.det in firstPOS or POS.noun in firstPOS: 
            stack.append("#EON#")
            stack.extend(grammar["S"][1].split())
        else: return {}
        
        i, startmark = 0, 0
        while i < len(input):
            word, peek = input[i], stack.pop()
            pos = POS.getPOS(word)

            if peek == pos: i++ 

            elif peek in meta_to_nonterm:
                nonterm = meta_to_nonterm[peek]

                if nonterm == "NP": output["agent"] = input[startmark: i]
                elif nonterm == "VP": output["action"] = input[startmark:i]
                else: output["type"] = punc_map[input[i]]
                startmark = i

            else:
                production = parse_table[pos]
                if production[0] == peek: 
                    stack.append(nonterm_to_meta[peek])
                    stack.extend(production[1])
                else: return {}
                
            
