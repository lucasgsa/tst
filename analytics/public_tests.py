import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
conta_votos = getattr(undertest, 'conta_votos', None)

class PublicTests(unittest.TestCase):

    def test_simples(self):
        votacao = []
        votacao.append('uma,sim,543,joao,PPPP')
        assert conta_votos(votacao, 543) == [1,0]

    def test_exemplo(self):
        votacao = []
        votacao.append('uma,sim,543,joao,PPPP')
        votacao.append('uma,nao,543,marina,PPPP')
        votacao.append('uma,sim,5,joao,PPPP')
        votacao.append('uma,nao,543,julio,P')
        votacao.append('uma,sim,543,carlos,PBBBB')
        votacao.append('uma,sim,543,juliana,PP')
        votacao.append('uma,sim,99,joao,PPPP')

        assert conta_votos(votacao, 543) == [3,2]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
