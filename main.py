class morsecode:
    def __init__(self):
        self.chars =  {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': '/'
        }
        self.nums = {
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.'
        }
        self.special = {
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            "'": '.----.',
            '!': '-.-.--',
            '/': '-..-.',
            '"': '.-..-.',
            '(': '-.--.-',
            ')': '-.--.-',
            '&': '.-...',
            ':': '---...',
            ';': '-.-.-.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            '_': '..--.-',
            '$': '...-..-',
            '@': '.--.-.',
            '#': '-.-.-.'
        }

    def convert_char(self, my_char):
        for key,value in self.chars.items():
            if key.lower() == my_char.lower():
                return value
        for key, value in self.nums.items():
            if key == my_char:
                return value
        for key, value in self.special.items():
            if key == my_char:
                return value
        raise ValueError('This character is not standardized in the list of the Morse Codes')



morsec = morsecode()
sentence = input('Convert to Morse Code : ')
try:
    result = []
    for x in sentence:
        code = morsec.convert_char(x)
        result.append(code)
    print("Here is your Morse Code : ")
    print('/'.join(result))
except ValueError as ve:
    print(ve)
