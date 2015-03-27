# -*- coding: utf-8 -*-

from dragonfly import (Grammar, AppContext, MappingRule, CompoundRule, Dictation, Function,
                       Key, Text, RuleRef, Repetition)

gvim_context = AppContext(executable="gvim")
grammar = Grammar("gvim", context=gvim_context)



# variable/function name formatting functions

def snake_case_action(text=""):
    s = "_".join(str(text).lower().split(" "))
    Text(s).execute()

def one_word_case_action(text=""):
    s = "".join(str(text).lower().split(" "))
    Text(s).execute()

def camel_case_action(text=""):
    words = [word.capitalize() for word in str(text).split(" ")]
    s = words[0].lower() + "".join(words[1:])
    Text(s).execute()

def studley_case_action(text=""):
    words = [word.capitalize() for word in str(text).split(" ")]
    s = "".join(words)
    Text(s).execute()


# SeriesMappingRule adapted from here:
# https://github.com/barrysims/dragonfly/blob/master/utils/series_mapping_rule.py 
# This class allows us to do CCR (continuous command recognition).
# CCR lets us combine commands seamlessly together in one utterance.

class SeriesMappingRule(CompoundRule):

    def __init__(self, mapping_rule):
        single = RuleRef(rule=mapping_rule)
        series = Repetition(single, min=1, max=16, name="series")

        compound_spec = "<series>"
        compound_extras = [series]
        CompoundRule.__init__(self, spec=compound_spec,
                              extras=compound_extras, exported=True)

    def _process_recognition(self, node, extras):  # @UnusedVariable
        series = extras["series"]
        for action in series:
            action.execute()

# gvim rules adapted from here:
# https://github.com/davitenio/dragonfly-macros/blob/master/gvim.py

mapping_rule = MappingRule(
    name="gvim",      
    exported=False,
    mapping={          

        "say <text>": Text("text"),
        
        "alpha": Key("a", static=True),
        "bravo": Key("b", static=True),
        "charlie": Key("c", static=True),
        "delta": Key("d", static=True),
        "echo": Key("e", static=True),
        "foxtrot": Key("f", static=True),
        "golf": Key("g", static=True),
        "hotel": Key("h", static=True),
        "india": Key("i", static=True),
        "(juliet|julia)": Key("j", static=True),
        "kilo": Key("k", static=True),
        "lima": Key("l", static=True),
        "mike": Key("m", static=True),
        "november": Key("n", static=True),
        "oscar": Key("o", static=True),
        "papa": Key("p", static=True),
        "(quebec|queen)": Key("q", static=True),
        "romeo": Key("r", static=True),
        "sierra": Key("s", static=True),
        "tango": Key("t", static=True),
        "uniform": Key("u", static=True),
        "victor": Key("v", static=True),
        "whiskey": Key("w", static=True),
        "x-ray": Key("x", static=True),
        "yankee": Key("y", static=True),
        "zulu": Key("z", static=True),

        "upper alpha": Key("A", static=True),
        "upper bravo": Key("B", static=True),
        "upper charlie": Key("C", static=True),
        "upper delta": Key("D", static=True),
        "upper echo": Key("E", static=True),
        "upper foxtrot": Key("F", static=True),
        "upper golf": Key("G", static=True),
        "upper hotel": Key("H", static=True),
        "upper india": Key("I", static=True),
        "upper (juliet|julia)": Key("J", static=True),
        "upper kilo": Key("K", static=True),
        "upper lima": Key("L", static=True),
        "upper mike": Key("M", static=True),
        "upper november": Key("N", static=True),
        "upper oscar": Key("O", static=True),
        "upper papa": Key("P", static=True),
        "upper (quebec|queen)": Key("Q", static=True),
        "upper romeo": Key("R", static=True),
        "upper sierra": Key("S", static=True),
        "upper tango": Key("T", static=True),
        "upper uniform": Key("U", static=True),
        "upper victor": Key("V", static=True),
        "upper whiskey": Key("W", static=True),
        "upper x-ray": Key("X", static=True),
        "upper yankee": Key("Y", static=True),
        "upper zulu": Key("Z", static=True),

        "zero": Key("0"),
        "one": Key("1"),
        "two": Key("2"),
        "three": Key("3"),
        "four": Key("4"),
        "five": Key("5"),
        "six": Key("6"),
        "seven": Key("7"),
        "eight": Key("8"),
        "nine": Key("9"),

        "space": Key("space", static=True),
        "tab": Key("tab"),
        "(newline|enter|slap)": Key("enter"),
        "percent [sign]": Key("percent"),
        "(asterisk|star|splat)": Key("asterisk"),
        "plus [sign]": Key("plus"),
        "(hyphen|tack)": Key("hyphen"),
        "(equal|equals)": Key("equal"),
        "bang": Key("exclamation"),
        "[single] quote": Key("squote"),
        "double (quote|quotes)": Key("dquote"),
        "(hash|hashtag)": Key("hash"),
        "dollar [sign]": Key("dollar"),
        "comma": Key("comma"),
        "(dot|period)": Key("dot"),
        "slash": Key("slash"),
        "colon": Key("colon"),
        # this doesn't work for some reason 
        #"semicolon": Key("semicolon"),
        "semicolon": Text(";"),
        "(escape|scape)": Key("escape"),
        "ampersand": Key("ampersand"),
        "apostrophe": Key("apostrophe"),
        "at [sign]": Key("at"),
        "backslash": Key("backslash"),
        "backtick": Key("backtick"),
        "(pipe|bar)": Key("bar"),
        "caret": Key("caret"),
        "question [mark]": Key("question"),
        "tilde": Key("tilde"),
        "(underscore|score)": Key("underscore"),

        #open paren
        #close paren

        # programming aids
        # -- variable/function naming 
        "snake <text>": Function(snake_case_action, extra={"text"}),
        "camel <text>": Function(camel_case_action, extra={"text"}),
        "studley <text>": Function(studley_case_action, extra={"text"}),
        "one word <text>": Function(one_word_case_action, extra={"text"}),
        # - function definition
        #"deaf": Text("def ():") + Key("left:2"),               # python
        "function": Text("function () {}") + Key("left:4"),     # javascript
        # -- code block deliniation 
        "cuddle": Text("()") + Key("left"),
        "twinkle": Text("''") + Key("left"), 
        "(bunny|bunnies)": Text('""') + Key("left"), 
        "curly [block]": Text("{}") + Key("left"),
        # -- helpful shortcuts''
        "punk": Text(";") + Key("enter"),
        # -- common phrases
        "aargh": Text("arg"),
        "aarghz": Text("args"),
        "aargh (v|b)": Text("arg v"),

        # vim specific



        },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ]
    )

# Add the action rule to the grammar instance.

gvim_rule = SeriesMappingRule(mapping_rule)
grammar.add_rule(gvim_rule)
#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None


