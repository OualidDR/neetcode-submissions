class Solution:


    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
           s.append(f'{len(i)}#{i}')
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
        # Trouve la position du délimiteur '#'
            j = i
            while s[j] != '#':
                j += 1
        # La longueur de la chaîne est donnée avant le '#'
            length = int(s[i:j])
        # La chaîne commence juste après le '#' et a une longueur 'length'
            str_part = s[j + 1 : j + 1 + length]
            res.append(str_part)
        # Déplace l'index après cette partie traitée
            i = j + 1 + length
        return res