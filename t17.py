class Solution:
    def letterCombinations(self, digits: str):
        digit_alpha_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        combinations = []
        combination = []

        def backtracking(index: int):
            if len(combination) == len(digits):
                combinations.append(''.join(combination))
                return
            digit = digits[index]
            for letter in digit_alpha_map[digit]:
                combination.append(letter)
                backtracking(index + 1)
                combination.pop()

        if digits == '':
            return []
        else:
            backtracking(0)
            return combinations


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
