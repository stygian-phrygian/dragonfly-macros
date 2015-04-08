# -*- coding: utf-8 -*-
from dragonfly import CompoundRule, MappingRule, RuleRef, Repetition

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
