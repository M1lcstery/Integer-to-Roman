class Solution(object):

    def intToRoman(self, s):
        """
        :type num: int
        :rtype: str
        """
        
        romanDictionary = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        result = ''

        for value in sorted(romanDictionary.keys(), reverse=True):
            
            while s >= value:
                result += romanDictionary[value]
                s -= value

        return result
