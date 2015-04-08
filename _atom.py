# -*- coding: utf-8 -*-
from series_mapping_rule import SeriesMappingRule
from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Function,
                        Key, Text)

atom_context = AppContext(executable="atom")
grammar      = Grammar("atom", context=atom_context)

mapping_rule = MappingRule(
    name="atom",
    exported=False,
    mapping={

        # atom ide specific
        "Go to line" : Key("c-g"),
        "Toggle comment" : Key("c-/"),
        "Toggle tree [view]" : Key("c-\\"),
        "Fuzzy find" : Key("c-t"),
        "Close tab" : Key("c-t"),
        "(Find|Finding) [in current] file" : Key("c-f"),
        "(Find|Finding) [in] project" : Key("cs-f"),

        # -- helpful shortcuts
        # I have this mapped to add a semicolon at the end of the line
        "punk" : Key("c-semicolon"),
        

        },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ],
    defaults={
            "text" : "",
             }
    )


# Add the action rule to the grammar instance.

atom_rule = SeriesMappingRule(mapping_rule)
grammar.add_rule(atom_rule)
#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
