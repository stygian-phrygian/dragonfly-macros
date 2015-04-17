# -*- coding: utf-8 -*-

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Integer,
                       Key, Text)

chrome_context = AppContext(executable="chrome")
grammar        = Grammar("chrome", context=chrome_context)

chrome_rule = MappingRule(
    name="chrome",
    mapping={
        "dictate <text>"                     : Text("%(text)s"),
        "[open] new (window|page)"           : Key("c-n"),
        "[open] new incognito (window|page)" : Key("cs-n"),
        "[open] new tab"                     : Key("c-t"),
        "reload (window|page|tab)"           : Key("c-r"),
        "[go to] tab [<n>] (left|previous)"  : Key("cs-tab:%(n)d"),
        "[go to] tab [<n>] (right|next)"     : Key("c-tab:%(n)d"),
        "go to tab <tab>"                    : Key("c-%(tab)d"),
        "close (window|page|tab)"            : Key("c-w"),
        "[go] [<n>] back"                    : Key("a-left:%(n)d"),
        "[go] [<n>] forward"                 : Key("a-right:%(n)d"),
        "[go to] address [bar]"              : Key("c-l"),
        "(enter|submit)"                     : Key("enter"),
        "(reopen|unclose) [(window|tab)]"    : Key("cs-t"),
        "save [file]"                        : Key("c-s"),
        "save [file] as <text>"              : Key("cs-s") + Text("%(text)s"),
        "find [in] [the] [page]"             : Key("c-f"),
        "show downloads"                     : Key("c-j"),
        "show history"                       : Key("c-h"),
        "view [page] source"                 : Key("c-u"),
        "zoom out [<n>] [(time|times)]"      : Key("c-minus:%(n)d"),
        "zoom in  [<n>] [(time|times)]"      : Key("c-plus:%(n)d"),
        "refresh"                            : Key("c-r"),
        "view source"                        : Key("c-u"),
        "(show|toggle|open) developer [tools]"  : Key("cs-i"),
        "(show|toggle|open) javascript console" : Key("cs-j"),
    },
    extras=[
        Integer("n", 1, 40),
        Integer('tab', 1, 8),
        Dictation("text")
    ],
    defaults={
            "n": 1
    }
)

grammar.add_rule(chrome_rule)
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
