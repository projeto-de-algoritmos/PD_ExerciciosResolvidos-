class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Cria o array de subsequencia e inicializa com 1
        long_sub = [1]*len(nums)

        # Começa a iteração a partir do segundo elemento
        for i in range(1, len(nums)):
            # compara o valor o de long_sub[i] com seus anteriores
            for j in range(i):
                if nums[i] > nums[j]:
                    long_sub[i] = max(long_sub[j] + 1, long_sub[i])

        # Retorna o tamanho da maior subsequencia
        return max(long_sub)