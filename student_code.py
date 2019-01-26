import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """

        print("Asserting {!r}".format(fact))

        for each_fact in self.facts:
            if fact == each_fact:
                print("This fact exists in KnowledgeBase")
        else:
            self.facts.append(fact)


    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """


        print("Asking {!r}".format(fact))
        binding_list = ListOfBindings()
        for each_f in self.facts:
            match1 = match(fact.statement, each_f.statement)
            if match1 != False:
                binding_list.add_bindings(match1)
        if len(binding_list) == 0:
            return False
        else:
            return binding_list
