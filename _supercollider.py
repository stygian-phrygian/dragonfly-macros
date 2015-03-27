
"""
    This module is a simple example of Dragonfly use.

    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Integer,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

supercollider_context = AppContext(executable="supercollider")
grammar = Grammar("supercollider", context=supercollider_context)


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
    mapping={          # The mapping dict: spec -> action.


            ################################
        
            # common variable names
            "(freak|frequency)": Text("freq"),
            "(aargh|argument)" : Text("arg"),
            # synthdefs
            "(synth|sin) (death|deaf|definition)": Text("SynthDef"),    
            # ugens
            #----"(sine|sign) (oscillator|us)":    Text("SinOsc"),
            "(sine|sign)"                     Text("Sin"),
            "(oscillator|us)":                Text("Osc"),
            "(envelope|and) (generator|jen)": Text("EnvGen"),
            "clang":                          Text("Klang"),
            #----"delay":                          Text("Delay"),                  
            "play (buffer|buff)":             Text("PlayBuf"),
            "record (buffer|buff)":           Text("RecordBuf"),
            "(buffer|buff) write":            Text("BufWr"),
            "(buffer|buff) read":             Text("BufRd"),
            

            ################################
            "[open] new (window|page)"              :Key("c-n"),
            "[open] new incognito (window|page)"    :Key("cs-n"),
            "[open] new tab"                        :Key("c-t"),
            "reload (window|page|tab)"              :Key("c-r"),
            "[go to] tab (right|next)"              :Key("c-tab"),
            "[go to] tab (left|previous)"           :Key("cs-tab"),
            "go to tab <tab>"                       :Key("c-%(tab)d"),
            "close (window|page|tab)"               :Key("c-w"),
            "[go] forward"              :Key("a-right"),
            "[go] back"                 :Key("a-left"),
            "[go to] address [bar]"     :Key("c-l"),
            "(enter|submit)"            :Key("enter"),
            "reopen [closed tab]"       :Key("cs-t"),
            "save [file]"               :Key("c-s"),
            "save [file] as <text>"     :Key("c-s") + Text("%(text)s"),
            "find [in the page]"        :Key("c-f"),
            "show downloads"            :Key("c-j"),
            "show history"              :Key("c-h"),
            "view [page] source"        :Key("c-u"),
            "zoom in"                   :Key("c-plus"),
            "zoom out"                  :Key("c-minus")
            },
    extras=[           # Special elements in the specs of the mapping.
            Integer('tab', 1, 8),
            Dictation("text"),
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


