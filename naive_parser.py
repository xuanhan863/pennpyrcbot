import defs, Global, thematic_roles

lookup = Global.lookup
agent = thematic_roles.agent
action = thematic_roles.action
theme = thematic_roles.theme
POS = Global.POS
punc_map = {".": "statement",
            "!": "emphatic",
            "?": "query"
            }

def parse(str):
    
    output = {}
    agent_found, action_found, theme_found = False, False, False

    buffer = []
    for substr in str.split():

        if substr in punc_map:
            output["theme"] = theme(buffer)
            output["type"] = punc_map[substr]
            return output

        word = lookup(substr)
        pos = word.POS
        buffer.append(word)
        
        if not agent_found and pos == POS.noun:
            output["agent"] = agent(buffer)
            agent_found = True
            buffer = []
        elif not action_found and pos == POS.verb:
            output["action"] = action(buffer)
            action_found == True
            buffer = []


        
