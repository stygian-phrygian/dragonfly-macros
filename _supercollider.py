# -*- coding: utf-8 -*-

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Integer,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

supercollider_context = AppContext(executable="supercollider")
grammar               = Grammar("supercollider", context=supercollider_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

supercollider_rule = MappingRule(
    name="supercollider",     # The name of the rule.
    mapping={                 # The mapping dict: spec -> action.

            # common variable names
            "(freak|frequency)": Text("freq"),
            "(aargh|argument)" : Text("arg"),
            # synthdefs
            "(synth|sin) (death|deaf|definition)": Text("SynthDef"),
            # ugens TODO (there's a lot of ugens)
            #----"(sine|sign) (oscillator|us)":    Text("SinOsc"),
            "(sine|sign)"                    : Text("Sin"),
            "(oscillator|us)"                : Text("Osc"),
            "(envelope|and) (generator|jen)" : Text("EnvGen"),
            "clang"                          : Text("Klang"),
            #----"delay"                     : Text("Delay"),
            "play (buffer|buff)"             : Text("PlayBuf"),
            "record (buffer|buff)"           : Text("RecordBuf"),
            "(buffer|buff) write"            : Text("BufWr"),
            "(buffer|buff) read"             : Text("BufRd")
            },
    extras=[           # Special elements in the specs of the mapping.
            # Integer('n', 1, 40),
            # Dictation("text"),
           ],
    )

# Add the action rule to the grammar instance.
grammar.add_rule(chrome_rule)
#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
