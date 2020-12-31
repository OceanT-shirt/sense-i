import sqlite3
from nltk.stem import WordNetLemmatizer

#初回だけ必要なので、コメントを外して実行してください
#import nltk
#nltk.download('wordnet')




def transword(word):
    lemmatizer = WordNetLemmatizer()

    # 辞書データベースに接続
    conn = sqlite3.connect("database/ejdict.sqlite3")
    c = conn.cursor()

    word = word.lower() #小文字に直す


    #データベースから呼び出しする関数
    def lem_dict(word, p): #pは見出語化する時に品詞を指定する引数('v'なら動詞、'n'なら名詞、'a'なら形容詞、'r'なら副詞)
        word_lm = (lemmatizer.lemmatize(word, pos=p),)
        c.execute('SELECT word, mean FROM items WHERE word=?',word_lm)
        return(c.fetchall())


    if lem_dict(word, 'v'):out = lem_dict(word, 'v')

    elif lem_dict(word, 'n'):out = lem_dict(word, 'n')

    elif lem_dict(word, 'a'):out = lem_dict(word, 'a')

    elif lem_dict(word, 'r'):out = lem_dict(word, 'r')
    
    # request が正しいか処理するのが面倒なので、もうエラーとして辞書登録する
    else:out = [('ERROR','誤り')]

    return out



# app.pyで呼び出す関数
def transdict(words):
    dic = {}

    for word in words:
        tmp = transword(word)
        dic[tmp[0][0]] = tmp[0][1]

    return dic

