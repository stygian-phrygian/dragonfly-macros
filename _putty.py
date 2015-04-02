# -*- coding: utf-8 -*-

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

putty_context       = AppContext(executable="putty")
cmd_context         = AppContext(executable="cmd")
powershell_context  = AppContext(executable="powershell")
grammar = Grammar("putty", context=(putty_context|cmd_context|powershell_context))


putty_rule = MappingRule(
    name="putty",      # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             # characters
             "(slap|newline|enter)": Key("enter"),
             "(splat|star|asterisk)": Key("asterisk"),
             "(hash|hashtag)": Key("hash"),
             "(minus|dash|tack|hyphen)": Key("hyphen"),
             "(dashdash|tacktack)": Key("hyphen,hyphen"),
             "interupt": Key("c-c"), # ctrl-c sends SIGINT
             "end of file": Key("c-d"), # ctrl-d send EOF
             # shell commands
             "(cd|change directory)": Text("cd "),
             "(l s|ellis|ls|list files)": Text("ls "),
             "(pwd|print working directory)": Text("pwd ") + Key("enter"),
             "(vi|v i|vim)": Text("vim "),
             "configure": Text("./configure"),
             "make": Text("make "),
             "make install": Text("make install "),
             "get init": Text("git init "),
             "get clone": Text("git clone "),
             "get add": Text("git add "),
             "get commit": Text('git commit -m ""') + Key("left"),
             "get status": Text("git status ") + Key("enter"),
             "get push": Text("git push "),
             "get pull": Text("git pull "),
             "get check out": Text("git checkout ") + Key("tab"),
             "get fetch": Text("git fetch ") + Key("tab"),
             "get merge": Text("git merge ") + Key("tab"),
             "get log": Text("git log ") + Key("enter"),
             "get log pretty": Text("git log --pretty=oneline") + Key("enter"),
             "get log author": Text('git log --author=""') + Key("left"),
             "get stash save": Text("git stash save") + Key("enter"),
             "get stash pop": Text("git stash pop") + Key("enter"),

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
