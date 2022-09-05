import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #Cria uma lista com as 3 variaveis
        tarefas = list(zip(startTime,endTime ,profit ))
		
		  # Faz a ordenação pelo hoario de inicio das tarefas
        tarefas.sort(key=lambda x:x[0])
        n = len(tarefas)
        
		  # Cria uma matriz com as tarefas
        inicio = [tarefas[i][0] for i in range(n) ]
        
        pontucaoTotal = [0 for _ in range(n)]
		
		  # Pega a matriz e lê ela de cima para baixo, bottom up
        pontucaoTotal[n-1] = tarefas[n-1][2]
        
			# Encontra o primeiro indice da matriz onde a tarefa termina
        for i in range(n-2,-1,-1):
            idx = bisect.bisect_left(inicio, tarefas[i][1], i, n)
			
			# O pontuacaoTotal recebe o valor maximo do idx
            pontucaoTotal[i] = max(pontucaoTotal[i+1], tarefas[i][2]+ (pontucaoTotal[idx] if idx < n else 0) )
        
        return pontucaoTotal[0]