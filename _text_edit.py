# -*- coding: utf-8 -*-
from series_mapping_rule import SeriesMappingRule
from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Function,
                        Key, Text)

atom_context = AppContext(executable="atom")
gvim_context = AppContext(executable="gvim")
atom_grammar       = Grammar("atom", context=atom_context)
# gvim_grammar TODO
text_edit_grammar  = Grammar("text_edit", context=(gvim_context|atom_context))


# variable/function name formatting functions

def snake_case_action(text=""):
    s = "_".join(str(text).lower().split(" "))
    Text(s).execute()

def spinal_case_action(text=""): # could also use kebab case?
    s = "-".join(str(text).lower().split(" "))
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


# Gvim rules adapted from here:
# https://github.com/davitenio/dragonfly-macros/blob/master/gvim.py

text_edit_mapping_rule = MappingRule(
    name="text_edit",
    exported=False,
    mapping={

        "dictate <text>" : Text("%(text)s"),

        "alpha"          : Key("a"),
        "bravo"          : Key("b"),
        "charlie"        : Key("c"),
        "delta"          : Key("d"),
        "echo"           : Key("e"),
        "foxtrot"        : Key("f"),
        "golf"           : Key("g"),
        "hotel"          : Key("h"),
        "india"          : Key("i"),
        "(juliet|julia)" : Key("j"),
        "kilo"           : Key("k"),
        "lima"           : Key("l"),
        "mike"           : Key("m"),
        "november"       : Key("n"),
        "oscar"          : Key("o"),
        "papa"           : Key("p"),
        "(quebec|queen)" : Key("q"),
        "romeo"          : Key("r"),
        "sierra"         : Key("s"),
        "tango"          : Key("t"),
        "uniform"        : Key("u"),
        "victor"         : Key("v"),
        "whiskey"        : Key("w"),
        "x-ray"          : Key("x"),
        "yankee"         : Key("y"),
        "zulu"           : Key("z"),

        "upper alpha"          : Key("A"),
        "upper bravo"          : Key("B"),
        "upper charlie"        : Key("C"),
        "upper delta"          : Key("D"),
        "upper echo"           : Key("E"),
        "upper foxtrot"        : Key("F"),
        "upper golf"           : Key("G"),
        "upper hotel"          : Key("H"),
        "upper india"          : Key("I"),
        "upper (juliet|julia)" : Key("J"),
        "upper kilo"           : Key("K"),
        "upper lima"           : Key("L"),
        "upper mike"           : Key("M"),
        "upper november"       : Key("N"),
        "upper oscar"          : Key("O"),
        "upper papa"           : Key("P"),
        "upper (quebec|queen)" : Key("Q"),
        "upper romeo"          : Key("R"),
        "upper sierra"         : Key("S"),
        "upper tango"          : Key("T"),
        "upper uniform"        : Key("U"),
        "upper victor"         : Key("V"),
        "upper whiskey"        : Key("W"),
        "upper x-ray"          : Key("X"),
        "upper yankee"         : Key("Y"),
        "upper zulu"           : Key("Z"),

        "zero"  : Key("0"),
        "one"   : Key("1"),
        "two"   : Key("2"),
        "three" : Key("3"),
        "four"  : Key("4"),
        "five"  : Key("5"),
        "six"   : Key("6"),
        "seven" : Key("7"),
        "eight" : Key("8"),
        "nine"  : Key("9"),

        # Dragon already includes the macros
        # "go (up|down|left|right) <n>"
        # hence we don't need to implement them

        # Bugs?
        # The space, equals, and comma characters do not work so well
        # with CCR.  The same behavior persisted with the dot character,
        # until I proffered the hack below.  There must be a better way?


        "(space|spy|spine)"       : Key("space"),
        "(tab|tabby|Debbie)"      : Key("tab"),
        "(newline|enter|slap)"    : Key("enter"),
        "(mod|percent) [sign]"    : Key("percent"),
        "(asterisk|star)"         : Key("asterisk"),
        "plus [sign]"             : Key("plus"),
        "(hyphen|minus|tack)"     : Key("hyphen"),
        "(equal|equals) [to]"     : Key("equal"),
        "bang"                    : Key("exclamation"),
        "(hash|hashtag)"          : Key("hash"),
        "dollar [sign]"           : Key("dollar"),
        "comma"                   : Key("comma"),
        "[<text_left>] (dot|point) [<text_right>]" : Text("%(text_left)s") + Key("dot") + Text("%(text_right)s"),
        "slash"                   : Key("slash"),
        "colon"                   : Key("colon"),
        # This doesn't work for some reason.
        #"semicolon": Key("semicolon"),
        "semicolon"               : Text(";"),
        "(escape|scape)"          : Key("escape"),
        "ampersand"               : Key("ampersand"),
        "apostrophe"              : Key("apostrophe"),
        "at [sign]"               : Key("at"),
        "backslash"               : Key("backslash"),
        "backtick"                : Key("backtick"),
        "pipe"                    : Key("bar"),
        "caret"                   : Key("caret"),
        "question [mark]"         : Key("question"),
        "tilde"                   : Key("tilde"),
        "(underscore|score)"      : Key("underscore"),

        # open and close code delimiters
        "L paren"                     : Key("lparen"),   # (
        "(or|our|are|R) paren"        : Key("rparen"),   # )
        "L brace"                     : Key("lbrace"),   # {
        "(or|our|are|R) brace"        : Key("rbrace"),   # }
        "L bracket"                   : Key("lbracket"), # [
        "(or|our|are|R) bracket"      : Key("rbracket"), # ]
        "L angle"                     : Key("langle"),   # <
        "(or|our|are|R) angle"        : Key("rangle"),   # >
        "[(single|S)] (quote|quotes)" : Key("squote"),   # '
        "(double|D) (quote|quotes)"   : Key("dquote"),   # "

        # programming aids

        # -- variable/function naming
        "snake <text>"    : Function(snake_case_action,    extra={"text"}),
        "camel <text>"    : Function(camel_case_action,    extra={"text"}),
        "studley <text>"  : Function(studley_case_action,  extra={"text"}),
        "one word <text>" : Function(one_word_case_action, extra={"text"}),
        # Might conflict with 'spine' macro above (for the space character).
        #"spinal <text>"  : Function(spinal_case_action,   extra={"text"}),

        # -- code block deliniation
        "cuddle [<inner_text>]"          : Text("(%(inner_text)s)") + Key("left"),
        "twinkle [<inner_text>]"         : Text("'%(inner_text)s'") + Key("left"),
        "tag [<inner_text>]"             : Text("<%(inner_text)s>") + Key("left"),
        "(parcel|carton) [<inner_text>]" : Text("[%(inner_text)s]") + Key("left"),
        "(bunny|bunnies) [<inner_text>]" : Text('"%(inner_text)s"') + Key("left"),
        "curly [block] [<inner_text>]"   : Text("{%(inner_text)s}") + Key("left"),

        # -- comparison
        # Implementing "<=" & ">=" has caused somewhat unpredictable
        # conflicts with the other macros.
        "double (equal|equals)"          : Text("=="),
        "(strict|double) not equals"     : Text("!=="),
        "(triple|strict) (equal|equals)" : Text("==="),


        ###################################################
        # Everything below is language specific
        # We need to factor this out into separate rules
        ###################################################


        # -- function definition
        # "deaf": Text("def ():") + Key("left:2"),               # python
        "function" : Text("function () {}") + Key("left:5"),   # javascript

        # -- loop definition
        "for loop"   : Text("for() {};")   + Key("left:5"),
        "for each"   : Text("forEach();")  + Key("left:2"),
        "while loop" : Text("while() {};") + Key("left:5"),

        # -- helpful shortcuts''
        #"punk" : Text(";") + Key("enter"),

        # -- common phrases

        # -------- javascript specific
        "variable [<text>]" : Text("var %(text)s"),
        "require [<text>]"  : Text("require()") + Key("left") + Text("%(text)s"),
        "aargh"             : Text("arg"),
        "aarghz"            : Text("args"),
        "FS"                : Text("fs"),
        "sink"              : Text("Sync"),
        "2 string"          : Text("toString"),
        "(error|air)"       : Text("err"),
        "consul"            : Text("console"),
        "you (till|tell)"   : Text("util"),
        "HTTP"              : Text("http"),
        "(ex|ext) name"     : Text("extname")
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


atom_mapping_rule = MappingRule(
    name="atom",
    exported=False,
    mapping={

        # atom ide specific
        "Go to line" : Key("c-g"),
        "Toggle comment" : Key("c-slash"),
        "Toggle tree [view]" : Key("c-backslash"),
        "Fuzzy find" : Key("c-t"),
        "Close tab" : Key("c-t"),
        "(Find|Finding) [in current] file" : Key("c-f"),
        "(Find|Finding) [in] project" : Key("cs-f"),
        "New line above" : Key("cs-enter"),
        "New line below" : Key("c-enter"),

        # -- helpful shortcuts
        # I have this mapped to add a semicolon at the end of the line
        # for some reason Key("c-semicolon") doesn't work
        "punk" : Key("ctrl:down") + Text(";") + Key("ctrl:up")
        
        },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ],
    defaults={
            "text" : "",
             }
    )


text_edit_rule = SeriesMappingRule(text_edit_mapping_rule)
text_edit_grammar.add_rule(text_edit_rule)
text_edit_grammar.load()

atom_rule = SeriesMappingRule(atom_mapping_rule)
atom_grammar.add_rule(atom_rule)
atom_grammar.load()

def unload():
    global text_edit_grammar, atom_grammar

    if text_edit_grammar: text_edit_grammar.unload()
    text_edit_grammar = None

    if atom_grammar: atom_grammar.unload()
    atom_grammar      = None