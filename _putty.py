
"""
    This module is a simple example of Dragonfly use.

    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

putty_context = AppContext(executable="putty")
cmd_context   = AppContext(executable="cmd")
grammar = Grammar("putty", context=putty_context | cmd_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

putty_rule = MappingRule(
    name="putty",      # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             # shell
             "(slap|newline|enter)": Key("enter"),
             "(splat|asterisk)": Key("asterisk"),
             "(hash|hashtag)": Key("hash"), 
             "(minus|dash|tack|hyphen)": Key("hyphen"),
             # shell commands
             "(cd|change directory)": Text("cd "),
             "(l s|ellis|ls|list files)": Text("ls "),
             "(pwd|print working directory)": Text("pwd "),
             "(vi|v i|vim)": Text("vim ") + Key("enter"),
             "make": Text("make "),
             "make install": Text("make install "),
             "get init": Text("git init ") + Key("enter"),
             "get status": Text("git status ") + Key("enter"),
             "get push": Text("git push "),
             "get add": Text("git add "),
             "get commit": Text('git commit -m ""') + Key("left"),
             "get clone": Text("git clone "),
             "get check out": Text("git checkout ") + Key("tab"),
             "get fetch": Text("git fetch ") + Key("tab"),
             "get merge": Text("git merge ") + Key("tab"),
             "get stash save": Text("git stash save") + Key("enter"),
             "get stash pop": Text("git stash pop") + Key("enter"),

             "interupt": Key("c-c"), # ctrl-c sends SIGINT
             "end of file": Key("c-d"), # ctrl-d send EOF
             "htop": Text("htop") + Key("enter"),

            },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ],
    )

# Add the action rule to the grammar instance.
grammar.add_rule(putty_rule)
#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None


