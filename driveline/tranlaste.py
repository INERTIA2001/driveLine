import requests as r

class Translate:
    def __init__(self,target,string,source):
        self.target = target
        self.string = string
        string = string.replace(" ","%20")
        self.response = r.get("https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate?source={}&target={}&input={}".format(source,target,string),
                              headers={"X-RapidAPI-Host": "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
                              "X-RapidAPI-Key": "c4648c305dmsh6584a65ddde721fp1a2753jsn42dd3fb7a27b"})
    def json(self):
        json = self.response.json()
        output = json["outputs"]
        return output
    def getOutput(self):
        output = self.json()
        detect = output[0]
        res = detect["output"]
        return res
