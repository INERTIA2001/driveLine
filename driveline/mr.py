morseDict = {"a":["._","a.mp3"],"b":["_...","b.mp3"],"c":["_._.","c.mp3"],"d":["_..","d.mp3"],"e":[".","e.mp3"],
            "f":[".._.","f.mp3"],"g":["__.","g.mp3"],"h":["....","h.mp3"],"i":["..","i.mp3"],"j":[".---","j.mp3"],
            "k":["_._","k.mp3"],"l":["._..","l.mp3"],"m":["__","m.mp3"],"n":["_.","n.mp3"],"o":["___","o.mp3"],
            "p":[".__.","p.mp3"],"q":["__._","q.mp3"],"r":["._.","r.mp3"],"s":["...","s.mp3"],"t":["_","t.mp3"],
            "u":[".._","u.mp3"],"v":["..._","v.mp3"],"w":[".__","w.mp3"],"x":["_.._","x.mp3"],"y":["_.__","y.mp3"],"z":["__..","z.mp3"],
            "1":[".____","1.mp3"],"2":["..___","2.mp3"],"3":["...__","3.mp3"],"4":["...._","4.mp3"],"5":[".....","5.mp3"],
            "6":["_....","6.mp3"],"7":["__...","7.mp3"],"8":["___..","8.mp3"],"9":["____.","9.mp3"],"0":["_____","0.mp3"]," ":"/"}

class Morse:
    def __init__(self,string):
        self.string = string.lower()
    def translate(self,string):
        result = ""
        for character in string:
            translateResult = morseDict[character][0]
            result+=translateResult+" "
        return result
    def translateFromMorse(self,string):
        result = ""
        stringList = string.split(" ")
        for character in stringList:
            for key,value in morseDict.items():
                if value[0] == character:
                    result+=key
                else:  
                    pass
        return result
    def showDictionary(self):
        num = 1
        for key, value in morseDict.items():
            print("{}.) {} = {}".format(num,key,value[0]))
            num += 1  