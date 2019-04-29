import unittest
from modules import IterationModule as IM
from modules import ParsingModule as PM

class MarkovTest(unittest.TestCase):

    def test_ruleStrToList(self):
        arg = ["a|->b","a->b","ab","a->bd",""]
        res = [["a","b",True],["a","b",False],[],["a","bd",False],[]]
        msg = ["Should be" + str(i) for i in res]
        for i in range(0,len(arg)):
            self.assertEqual(PM.ruleStrToList(arg[i]),res[i],msg[i])


    def test_validateRuleList(self):
        arg = [["a","b",True],["a","b",False],["ad","b",True]]
        arg += [["a","bd",False],["a","bd",True]]
        res = [[],[],[1,'d'],[4,'d'],[5,'d']]
        msg = ["Should be" + str(i) for i in res]
        for i in range(0,len(arg)):
            self.assertEqual(PM.validateRuleList(arg[i]),res[i],msg[i])


    def test_doIteration(self):
        rules = [["a","b", False],["b","c",True]]
        sinput = ["aaa","bbb","ccc"]
        res = [["baa",False,0],["cbb",True,1],["ccc",True,2]]
        msg = ["Should be" + str(i) for i in res]
        for i in range(0,len(sinput)):
            self.assertEqual(IM.doIteration(rules,sinput[i]),res[i],msg[i])


if __name__ == '__main__':
    unittest.main()
