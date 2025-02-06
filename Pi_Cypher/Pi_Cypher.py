from mpmath import mp

#This is storage of the dictionaries we use 
#This is the dictionary list to randomize numbers (Numbers, letters and symbols seperated because of their frequency to occur)
#These are randomized but pre defined so we can decrypt
NumberList = []
InverseNumberList = []
TempDictionary = {'1': '2','2': '7','3': '9','4': '3','5': '6','6': '4','7': '1','8': '5','9': '0','0': '8',}
NumberList.append(TempDictionary)
TempDictionary = {'2': '1','7': '2','9': '3','3': '4','6': '5','4': '6','1': '7','5': '8','0': '9','8': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '4','2': '6','3': '3','4': '0','5': '5','6': '7','7': '2','8': '1','9': '8','0': '9',}
NumberList.append(TempDictionary)
TempDictionary = {'4': '1','6': '2','3': '3','0': '4','5': '5','7': '6','2': '7','1': '8','8': '9','9': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '3','2': '5','3': '8','4': '6','5': '4','6': '9','7': '2','8': '7','9': '1','0': '0',}
NumberList.append(TempDictionary)
TempDictionary = {'3': '1','5': '2','8': '3','6': '4','4': '5','9': '6','2': '7','7': '8','1': '9','0': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '2','2': '0','3': '6','4': '8','5': '3','6': '4','7': '7','8': '9','9': '5','0': '1',}
NumberList.append(TempDictionary)
TempDictionary = {'2': '1','0': '2','6': '3','8': '4','3': '5','4': '6','7': '7','9': '8','5': '9','1': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '2','2': '7','3': '5','4': '1','5': '4','6': '9','7': '3','8': '0','9': '6','0': '8',}
NumberList.append(TempDictionary)
TempDictionary = {'2': '1','7': '2','5': '3','1': '4','4': '5','9': '6','3': '7','0': '8','6': '9','8': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '8','2': '4','3': '3','4': '9','5': '5','6': '6','7': '0','8': '1','9': '7','0': '2',}
NumberList.append(TempDictionary)
TempDictionary = {'8': '1','4': '2','3': '3','9': '4','5': '5','6': '6','0': '7','1': '8','7': '9','2': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '4','2': '5','3': '6','4': '9','5': '0','6': '2','7': '7','8': '8','9': '3','0': '1',}
NumberList.append(TempDictionary)
TempDictionary = {'4': '1','5': '2','6': '3','9': '4','0': '5','2': '6','7': '7','8': '8','3': '9','1': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '3','2': '9','3': '4','4': '7','5': '0','6': '6','7': '2','8': '1','9': '8','0': '5',}
NumberList.append(TempDictionary)
TempDictionary = {'3': '1','9': '2','4': '3','7': '4','0': '5','6': '6','2': '7','1': '8','8': '9','5': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '5','2': '0','3': '3','4': '4','5': '6','6': '7','7': '2','8': '1','9': '8','0': '9',}
NumberList.append(TempDictionary)
TempDictionary = {'5': '1','0': '2','3': '3','4': '4','6': '5','7': '6','2': '7','1': '8','8': '9','9': '0',}
InverseNumberList.append(TempDictionary)
TempDictionary = {'1': '3','2': '2','3': '5','4': '8','5': '1','6': '9','7': '0','8': '6','9': '7','0': '4',}
NumberList.append(TempDictionary)
TempDictionary = {'3': '1','2': '2','5': '3','8': '4','1': '5','9': '6','0': '7','6': '8','7': '9','4': '0',}
InverseNumberList.append(TempDictionary)

#this is the dictionaries that we will use for lowercase Alphabet things
LowerLetterList = []
InverseLowerLetterList = []
TempDictionary = {'a': 'r','b': 'b','c': 'j','d': 'l','e': 'k','f': 'a','g': 'u','h': 'i','i': 's','j': 'g','k': 'o','l': 'c','m': 'n','n': 'p','o': 'd','p': 'v','q': 'x','r': 't','s': 'q','t': 'f','u': 'm','v': 'w','w': 'y','x': 'e','y': 'z','z': 'h',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'r': 'a','b': 'b','j': 'c','l': 'd','k': 'e','a': 'f','u': 'g','i': 'h','s': 'i','g': 'j','o': 'k','c': 'l','n': 'm','p': 'n','d': 'o','v': 'p','x': 'q','t': 'r','q': 's','f': 't','m': 'u','w': 'v','y': 'w','e': 'x','z': 'y','h': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'f','b': 'c','c': 'a','d': 'z','e': 'i','f': 'v','g': 'x','h': 'b','i': 'h','j': 'n','k': 'j','l': 'g','m': 't','n': 'm','o': 'o','p': 'e','q': 'u','r': 'l','s': 's','t': 'd','u': 'w','v': 'k','w': 'y','x': 'q','y': 'p','z': 'r',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'f': 'a','c': 'b','a': 'c','z': 'd','i': 'e','v': 'f','x': 'g','b': 'h','h': 'i','n': 'j','j': 'k','g': 'l','t': 'm','m': 'n','o': 'o','e': 'p','u': 'q','l': 'r','s': 's','d': 't','w': 'u','k': 'v','y': 'w','q': 'x','p': 'y','r': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'b','b': 'g','c': 'j','d': 'h','e': 'l','f': 'y','g': 'k','h': 'w','i': 'p','j': 'x','k': 'e','l': 'o','m': 'n','n': 's','o': 'i','p': 't','q': 'z','r': 'u','s': 'm','t': 'c','u': 'q','v': 'f','w': 'r','x': 'd','y': 'a','z': 'v',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'b': 'a','g': 'b','j': 'c','h': 'd','l': 'e','y': 'f','k': 'g','w': 'h','p': 'i','x': 'j','e': 'k','o': 'l','n': 'm','s': 'n','i': 'o','t': 'p','z': 'q','u': 'r','m': 's','c': 't','q': 'u','f': 'v','r': 'w','d': 'x','a': 'y','v': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'c','b': 'm','c': 'b','d': 'a','e': 'q','f': 'h','g': 'u','h': 'n','i': 'v','j': 't','k': 'i','l': 'r','m': 'p','n': 'f','o': 's','p': 'x','q': 'w','r': 'd','s': 'e','t': 'o','u': 'l','v': 'g','w': 'y','x': 'z','y': 'k','z': 'j',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'c': 'a','m': 'b','b': 'c','a': 'd','q': 'e','h': 'f','u': 'g','n': 'h','v': 'i','t': 'j','i': 'k','r': 'l','p': 'm','f': 'n','s': 'o','x': 'p','w': 'q','d': 'r','e': 's','o': 't','l': 'u','g': 'v','y': 'w','z': 'x','k': 'y','j': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'c','b': 'j','c': 'd','d': 'o','e': 'v','f': 'h','g': 'u','h': 'i','i': 'g','j': 'q','k': 'b','l': 'k','m': 'f','n': 'm','o': 's','p': 'p','q': 'a','r': 'x','s': 'e','t': 'w','u': 'r','v': 't','w': 'n','x': 'z','y': 'y','z': 'l',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'c': 'a','j': 'b','d': 'c','o': 'd','v': 'e','h': 'f','u': 'g','i': 'h','g': 'i','q': 'j','b': 'k','k': 'l','f': 'm','m': 'n','s': 'o','p': 'p','a': 'q','x': 'r','e': 's','w': 't','r': 'u','t': 'v','n': 'w','z': 'x','y': 'y','l': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'g','b': 'u','c': 'a','d': 'l','e': 'd','f': 'i','g': 'k','h': 'n','i': 'p','j': 'e','k': 's','l': 'h','m': 'v','n': 'w','o': 'r','p': 'c','q': 'x','r': 't','s': 'y','t': 'f','u': 'b','v': 'j','w': 'm','x': 'z','y': 'q','z': 'o',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'g': 'a','u': 'b','a': 'c','l': 'd','d': 'e','i': 'f','k': 'g','n': 'h','p': 'i','e': 'j','s': 'k','h': 'l','v': 'm','w': 'n','r': 'o','c': 'p','x': 'q','t': 'r','y': 's','f': 't','b': 'u','j': 'v','m': 'w','z': 'x','q': 'y','o': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'k','b': 'g','c': 'h','d': 'q','e': 'f','f': 'v','g': 'p','h': 'b','i': 'c','j': 'j','k': 'r','l': 'o','m': 'z','n': 'm','o': 'd','p': 'y','q': 'a','r': 'l','s': 'e','t': 't','u': 'u','v': 'n','w': 'w','x': 'i','y': 'x','z': 's',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'k': 'a','g': 'b','h': 'c','q': 'd','f': 'e','v': 'f','p': 'g','b': 'h','c': 'i','j': 'j','r': 'k','o': 'l','z': 'm','m': 'n','d': 'o','y': 'p','a': 'q','l': 'r','e': 's','t': 't','u': 'u','n': 'v','w': 'w','i': 'x','x': 'y','s': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'z','b': 'b','c': 'j','d': 'o','e': 'c','f': 'q','g': 'r','h': 't','i': 'v','j': 'g','k': 'y','l': 'l','m': 'm','n': 'k','o': 'd','p': 'w','q': 'i','r': 'u','s': 'n','t': 'p','u': 'h','v': 'a','w': 'f','x': 's','y': 'x','z': 'e',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'z': 'a','b': 'b','j': 'c','o': 'd','c': 'e','q': 'f','r': 'g','t': 'h','v': 'i','g': 'j','y': 'k','l': 'l','m': 'm','k': 'n','d': 'o','w': 'p','i': 'q','u': 'r','n': 's','p': 't','h': 'u','a': 'v','f': 'w','s': 'x','x': 'y','e': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'l','b': 'u','c': 't','d': 'p','e': 'y','f': 'r','g': 'q','h': 's','i': 'e','j': 'm','k': 'h','l': 'i','m': 'w','n': 'z','o': 'j','p': 'f','q': 'b','r': 'x','s': 'a','t': 'v','u': 'g','v': 'd','w': 'c','x': 'n','y': 'o','z': 'k',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'l': 'a','u': 'b','t': 'c','p': 'd','y': 'e','r': 'f','q': 'g','s': 'h','e': 'i','m': 'j','h': 'k','i': 'l','w': 'm','z': 'n','j': 'o','f': 'p','b': 'q','x': 'r','a': 's','v': 't','g': 'u','d': 'v','c': 'w','n': 'x','o': 'y','k': 'z',}
InverseLowerLetterList.append(TempDictionary)
TempDictionary = {'a': 'd','b': 'q','c': 'f','d': 'j','e': 't','f': 'y','g': 'i','h': 's','i': 'a','j': 'w','k': 'p','l': 'n','m': 'x','n': 'k','o': 'h','p': 'g','q': 'e','r': 'c','s': 'r','t': 'm','u': 'l','v': 'b','w': 'v','x': 'u','y': 'z','z': 'o',}
LowerLetterList.append(TempDictionary)
TempDictionary = {'d': 'a','q': 'b','f': 'c','j': 'd','t': 'e','y': 'f','i': 'g','s': 'h','a': 'i','w': 'j','p': 'k','n': 'l','x': 'm','k': 'n','h': 'o','g': 'p','e': 'q','c': 'r','r': 's','m': 't','l': 'u','b': 'v','v': 'w','u': 'x','z': 'y','o': 'z',}
InverseLowerLetterList.append(TempDictionary)
#this Code Will be used for the Upper case letters dictionaries (because they are usually after the puncuation)
UpperLetterList = []
InverseUpperLetterList = []
TempDictionary = {'A': 'L','B': 'M','C': 'D','D': 'F','E': 'G','F': 'B','G': 'P','H': 'S','I': 'U','J': 'X','K': 'Q','L': 'W','M': 'R','N': 'I','O': 'E','P': 'Z','Q': 'N','R': 'Y','S': 'C','T': 'A','U': 'T','V': 'K','W': 'J','X': 'V','Y': 'H','Z': 'O',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'L': 'A','M': 'B','D': 'C','F': 'D','G': 'E','B': 'F','P': 'G','S': 'H','U': 'I','X': 'J','Q': 'K','W': 'L','R': 'M','I': 'N','E': 'O','Z': 'P','N': 'Q','Y': 'R','C': 'S','A': 'T','T': 'U','K': 'V','J': 'W','V': 'X','H': 'Y','O': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'H','B': 'F','C': 'O','D': 'U','E': 'C','F': 'P','G': 'X','H': 'J','I': 'S','J': 'G','K': 'D','L': 'Z','M': 'T','N': 'E','O': 'Y','P': 'K','Q': 'M','R': 'I','S': 'Q','T': 'R','U': 'N','V': 'A','W': 'W','X': 'B','Y': 'L','Z': 'V',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'H': 'A','F': 'B','O': 'C','U': 'D','C': 'E','P': 'F','X': 'G','J': 'H','S': 'I','G': 'J','D': 'K','Z': 'L','T': 'M','E': 'N','Y': 'O','K': 'P','M': 'Q','I': 'R','Q': 'S','R': 'T','N': 'U','A': 'V','W': 'W','B': 'X','L': 'Y','V': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'C','B': 'K','C': 'W','D': 'V','E': 'D','F': 'M','G': 'U','H': 'A','I': 'S','J': 'L','K': 'F','L': 'Y','M': 'N','N': 'G','O': 'Q','P': 'R','Q': 'E','R': 'Z','S': 'T','T': 'J','U': 'H','V': 'O','W': 'I','X': 'X','Y': 'P','Z': 'B',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'C': 'A','K': 'B','W': 'C','V': 'D','D': 'E','M': 'F','U': 'G','A': 'H','S': 'I','L': 'J','F': 'K','Y': 'L','N': 'M','G': 'N','Q': 'O','R': 'P','E': 'Q','Z': 'R','T': 'S','J': 'T','H': 'U','O': 'V','I': 'W','X': 'X','P': 'Y','B': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'D','B': 'K','C': 'P','D': 'H','E': 'B','F': 'C','G': 'Z','H': 'R','I': 'O','J': 'F','K': 'J','L': 'V','M': 'L','N': 'Y','O': 'A','P': 'G','Q': 'I','R': 'W','S': 'N','T': 'M','U': 'Q','V': 'E','W': 'U','X': 'X','Y': 'S','Z': 'T',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'D': 'A','K': 'B','P': 'C','H': 'D','B': 'E','C': 'F','Z': 'G','R': 'H','O': 'I','F': 'J','J': 'K','V': 'L','L': 'M','Y': 'N','A': 'O','G': 'P','I': 'Q','W': 'R','N': 'S','M': 'T','Q': 'U','E': 'V','U': 'W','X': 'X','S': 'Y','T': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'I','B': 'V','C': 'E','D': 'K','E': 'S','F': 'W','G': 'Z','H': 'B','I': 'L','J': 'Y','K': 'X','L': 'J','M': 'P','N': 'D','O': 'T','P': 'F','Q': 'G','R': 'U','S': 'N','T': 'A','U': 'C','V': 'Q','W': 'R','X': 'H','Y': 'M','Z': 'O',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'I': 'A','V': 'B','E': 'C','K': 'D','S': 'E','W': 'F','Z': 'G','B': 'H','L': 'I','Y': 'J','X': 'K','J': 'L','P': 'M','D': 'N','T': 'O','F': 'P','G': 'Q','U': 'R','N': 'S','A': 'T','C': 'U','Q': 'V','R': 'W','H': 'X','M': 'Y','O': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'F','B': 'B','C': 'L','D': 'C','E': 'E','F': 'I','G': 'D','H': 'W','I': 'G','J': 'J','K': 'U','L': 'O','M': 'S','N': 'R','O': 'Y','P': 'X','Q': 'V','R': 'K','S': 'T','T': 'P','U': 'A','V': 'Z','W': 'N','X': 'Q','Y': 'M','Z': 'H',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'F': 'A','B': 'B','L': 'C','C': 'D','E': 'E','I': 'F','D': 'G','W': 'H','G': 'I','J': 'J','U': 'K','O': 'L','S': 'M','R': 'N','Y': 'O','X': 'P','V': 'Q','K': 'R','T': 'S','P': 'T','A': 'U','Z': 'V','N': 'W','Q': 'X','M': 'Y','H': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'W','B': 'G','C': 'D','D': 'Z','E': 'B','F': 'L','G': 'V','H': 'O','I': 'S','J': 'N','K': 'X','L': 'J','M': 'M','N': 'F','O': 'U','P': 'E','Q': 'A','R': 'H','S': 'C','T': 'Y','U': 'T','V': 'Q','W': 'I','X': 'P','Y': 'R','Z': 'K',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'W': 'A','G': 'B','D': 'C','Z': 'D','B': 'E','L': 'F','V': 'G','O': 'H','S': 'I','N': 'J','X': 'K','J': 'L','M': 'M','F': 'N','U': 'O','E': 'P','A': 'Q','H': 'R','C': 'S','Y': 'T','T': 'U','Q': 'V','I': 'W','P': 'X','R': 'Y','K': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'H','B': 'L','C': 'V','D': 'K','E': 'D','F': 'I','G': 'C','H': 'U','I': 'B','J': 'J','K': 'T','L': 'Z','M': 'W','N': 'R','O': 'E','P': 'G','Q': 'S','R': 'F','S': 'Q','T': 'N','U': 'A','V': 'P','W': 'Y','X': 'M','Y': 'O','Z': 'X',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'H': 'A','L': 'B','V': 'C','K': 'D','D': 'E','I': 'F','C': 'G','U': 'H','B': 'I','J': 'J','T': 'K','Z': 'L','W': 'M','R': 'N','E': 'O','G': 'P','S': 'Q','F': 'R','Q': 'S','N': 'T','A': 'U','P': 'V','Y': 'W','M': 'X','O': 'Y','X': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'L','B': 'Z','C': 'T','D': 'Y','E': 'O','F': 'X','G': 'D','H': 'K','I': 'H','J': 'J','K': 'I','L': 'R','M': 'C','N': 'N','O': 'P','P': 'V','Q': 'E','R': 'A','S': 'B','T': 'M','U': 'F','V': 'S','W': 'U','X': 'G','Y': 'W','Z': 'Q',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'L': 'A','Z': 'B','T': 'C','Y': 'D','O': 'E','X': 'F','D': 'G','K': 'H','H': 'I','J': 'J','I': 'K','R': 'L','C': 'M','N': 'N','P': 'O','V': 'P','E': 'Q','A': 'R','B': 'S','M': 'T','F': 'U','S': 'V','U': 'W','G': 'X','W': 'Y','Q': 'Z',}
InverseUpperLetterList.append(TempDictionary)
TempDictionary = {'A': 'D','B': 'U','C': 'F','D': 'H','E': 'J','F': 'V','G': 'R','H': 'K','I': 'A','J': 'C','K': 'Q','L': 'X','M': 'B','N': 'L','O': 'S','P': 'P','Q': 'W','R': 'E','S': 'N','T': 'O','U': 'Z','V': 'I','W': 'T','X': 'Y','Y': 'M','Z': 'G',}
UpperLetterList.append(TempDictionary)
TempDictionary = {'D': 'A','U': 'B','F': 'C','H': 'D','J': 'E','V': 'F','R': 'G','K': 'H','A': 'I','C': 'J','Q': 'K','X': 'L','B': 'M','L': 'N','S': 'O','P': 'P','W': 'Q','E': 'R','N': 'S','O': 'T','Z': 'U','I': 'V','T': 'W','Y': 'X','M': 'Y','G': 'Z',}
InverseUpperLetterList.append(TempDictionary)

#Current Version of the Code doesnt encrypt symbols

def EncodeLetter(Letter,Number):
    #first we find what kind of character we are dealing with by using ascii values
    order = ord(Letter)
    if(order>=48 and order<=57):
        #we are dealing with a Number
        return(NumberList[int(Number)].get(str(Letter)))
    if(order>=65 and order<=90):
        #we are dealing with a Number
        return(UpperLetterList[int(Number)].get(str(Letter)))
    if(order>=97 and order<=122):
        #we are dealing with a Number
        return(LowerLetterList[int(Number)].get(str(Letter)))
    else:
        return(Letter)

def DecodeLetter(Letter,Number):
    #first we find what kind of character we are dealing with by using ascii values
    order = ord(Letter)
    if(order>=48 and order<=57):
        #we are dealing with a Number
        return(InverseNumberList[int(Number)].get(str(Letter)))
    if(order>=65 and order<=90):
        #we are dealing with a Number
        return(InverseUpperLetterList[int(Number)].get(str(Letter)))
    if(order>=97 and order<=122):
        #we are dealing with a Number
        return(InverseLowerLetterList[int(Number)].get(str(Letter)))
    else:
        return(Letter)


done=1
while(done!=0):
    if(done==1):
        questionAnswer = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
        done=2
    else:
        questionAnswer = input("Please enter either (E)ncrypt or (D)ecrypt?: ")
    questionAnswer = questionAnswer.lower()
    if(questionAnswer == "e" or questionAnswer == "encrypt" or questionAnswer == "(e)ncrypt"):
        #this means we are encrypting
        WhatToDo = "encrypt"
        done=0
    if(questionAnswer == "d" or questionAnswer == "decrypt" or questionAnswer == "(d)ecrypt"):
        #this means we are Decrypting
        WhatToDo = "decrypt"
        done=0
OurInput = input("What would you like to " + WhatToDo + "?")
Digits = len(OurInput)+2
mp.dps = Digits
print(Digits)
OurPi = str(mp.pi)
done =0
if(WhatToDo == "encrypt"):
    numberOfRuns = input("How many layers of encryption do you want to run through?: ")
    while(done==0):
        if(numberOfRuns.isnumeric() and int(numberOfRuns)>0):
            for x in range(int(numberOfRuns)):
                CurrentDigit = 0
                output = ""
                output += EncodeLetter(OurInput[CurrentDigit],OurPi[CurrentDigit])
                CurrentDigit =2
                while(CurrentDigit <= len(OurInput)):
                    output += EncodeLetter(OurInput[CurrentDigit-1],OurPi[CurrentDigit])
                    CurrentDigit +=1
                OurInput = output
                

            done=1
        else:
            numberOfRuns = input("Please enter a Positive Integer for the number of Encryptions: ")
if(WhatToDo == "decrypt"):
    numberOfRuns = input("How many layers of encryption was used for this?: ")
    while(done==0):
        if(numberOfRuns.isnumeric() and int(numberOfRuns)>0):
            for x in range(int(numberOfRuns)):
                CurrentDigit = 0
                output = ""
                output += DecodeLetter(OurInput[CurrentDigit],OurPi[CurrentDigit])
                CurrentDigit =2
                while(CurrentDigit <= len(OurInput)):
                    output += DecodeLetter(OurInput[CurrentDigit-1],OurPi[CurrentDigit])
                    CurrentDigit +=1
                OurInput = output

            done=1
        else:
            numberOfRuns = input("Please enter a Positive Integer for the number of Encryptions used: ")
print()
#We place the ------- to show clearly the start and end of the encrypted text
print("-------" + output + "-------")

