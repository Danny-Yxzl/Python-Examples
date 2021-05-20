import difflib
 
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
 
print(string_similar('爱尔眼科沪滨医院', '沪滨爱尔眼科医院'))
print(string_similar('安定区妇幼保健站', '定西市安定区妇幼保健站'))
print(string_similar('广州市医院', '广东省中医院'))
print(string_similar('再见', '你好'))