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

        "dictate <text>": Text("%(text)s"),
        
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

        "zero": Key("0", static=True),
        "one": Key("1", static=True),
        "two": Key("2", static=True),
        "three": Key("3", static=True),
        "four": Key("4", static=True),
        "five": Key("5", static=True),
        "six": Key("6", static=True),
        "seven": Key("7", static=True),
        "eight": Key("8", static=True),
        "nine": Key("9", static=True),

        # BUG?
        # saying "space something" produces 
        #"space something" rather than " something"
        "space": Key("space", static=False),
        "tab": Key("tab", static=True),
        "(newline|enter|slap)": Key("enter", static=True),
        "percent [sign]": Key("percent", static=True),
        "(asterisk|star|splat)": Key("asterisk", static=True),
        "plus [sign]": Key("plus", static=True),
        "(hyphen|minus|tack)": Key("hyphen", static=True),
        "(equal|equals)": Key("equal", static=True),
        "bang": Key("exclamation", static=True),
        "[single] (quote|quotes)": Key("squote", static=True),
        "double (quote|quotes)": Key("dquote", static=True),
        "(hash|hashtag)": Key("hash", static=True),
        "dollar [sign]": Key("dollar", static=True),
        "comma": Key("comma", static=True), # BUG: "alpha comma alpha" -> "alpha, alpha"
        "[<text_left>] (dot|point) [<text_right>]": Text("%(text_left)s") + Key("dot") + Text("%(text_right)s"),
        "slash": Key("slash", static=True),
        "colon": Key("colon", static=True),
        # this doesn't work for some reason 
        #"semicolon": Key("semicolon"),
        "semicolon": Text(";", static=True),
        "(escape|scape)": Key("escape", static=True),
        "ampersand": Key("ampersand", static=True),
        "apostrophe": Key("apostrophe", static=True),
        "at [sign]": Key("at", static=True),
        "backslash": Key("backslash", static=True),
        "backtick": Key("backtick", static=True),
        "pipe": Key("bar", static=True),
        "caret": Key("caret", static=True),
        "question [mark]": Key("question", static=True),
        "tilde": Key("tilde", static=True),
        "(underscore|score)": Key("underscore", static=True),

        #open paren
        #close paren

        # programming aids

        # -- variable/function naming 
        "snake <text>"      : Function(snake_case_action,    extra={"text"}),
        "camel <text>"      : Function(camel_case_action,    extra={"text"}),
        "studley <text>"    : Function(studley_case_action,  extra={"text"}),
        "one word <text>"   : Function(one_word_case_action, extra={"text"}),

        # -- code block deliniation 
        "cuddle [<inner_text>]"             : Text("(%(inner_text)s)") + Key("left"),
        "twinkle [<inner_text>]"            : Text("'%(inner_text)s'") + Key("left"), 
        "tag [<inner_text>]"                : Text("<%(inner_text)s>") + Key("left"),
        "(parcel|carton) [<inner_text>]"    : Text("[%(inner_text)s]") + Key("left"),
        "(bunny|bunnies) [<inner_text>]"    : Text('"%(inner_text)s"') + Key("left"), 
        "curly [block] [<inner_text>]"      : Text("{%(inner_text)s}") + Key("left"),

        # - function definition
        #"deaf": Text("def ():") + Key("left:2"),               # python
        "function": Text("function () {}") + Key("left:4"),     # javascript
        # loop definition
        "for loop": Text("for(;;) {}") + Key("left:6"),

        # -- helpful shortcuts''
        "punk": Text(";") + Key("enter"),
        # -- common phrases
        "variable": Text("var ", static=True),
        "aargh": Text("arg", static=True),
        "aarghz": Text("args", static=True),
        #doesn't work, dragon can't hear the 'v' or 'b'
        #"aargh (v|b)": Text("arg v"),
        "consul": Text("console", static=True),

        # vim specific
        # TODO



        },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
            Dictation("inner_text"),
            Dictation("text_left"),
            Dictation("text_right")
           ],
    defaults={
            "text"          : "",
            "inner_text"    : "",
            "text_left"     : "",
            "text_right"    : ""
             }
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


