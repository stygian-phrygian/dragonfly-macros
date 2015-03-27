
"""
put me in Natlink\MacroSystem folder 

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Integer,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

chrome_context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=chrome_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

chrome_rule = MappingRule(
    name="chrome",     # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
            "[open] new (window|page)"              :Key("c-n"),
            "[open] new incognito (window|page)"    :Key("cs-n"),
            "[open] new tab"                        :Key("c-t"),
            "reload (window|page|tab)"              :Key("c-r"),
            "[go to] tab [<n>] (left|previous)"     :Key("cs-tab:%(n)d"),
            "[go to] tab [<n>] (right|next)"        :Key("c-tab:%(n)d"),
            "go to tab <tab>"                       :Key("c-%(tab)d"),
            "close (window|page|tab)"               :Key("c-w"),
            "[go] [<n>] back"                 :Key("a-left:%(n)d"),
            "[go] [<n>] forward"              :Key("a-right:%(n)d"),
            "[go to] address [bar]"     :Key("c-l"),
            "(enter|submit)"            :Key("enter"),
            "reopen [closed tab]"       :Key("cs-t"),
            "save [file]"               :Key("c-s"),
            "save [file] as <text>"     :Key("c-s") + Text("%(text)s"),
            "find [in] [the] [page]"    :Key("c-f"),
            "show downloads"            :Key("c-j"),
            "show history"              :Key("c-h"),
            "view [page] source"        :Key("c-u"),
            "zoom out [<n>] [(time|times)]"      :Key("c-minus:%(n)d"),
            "zoom in  [<n>] [(time|times)]"      :Key("c-plus:%(n)d")
            },
    extras=[           # Special elements in the specs of the mapping.
            Integer("n", 1, 40),
            Integer('tab', 1, 8),
            Dictation("text")
           ],
    defaults={
            "n": 1
             }
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


