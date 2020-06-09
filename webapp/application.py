from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)


def isstring(string):
    '''Checks if entry is a valid string'''
    for i in range(len(string)):
        if string[i].isalpha():
            pass
        else:
            return False


def encrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Encrypts the normal text as per the key'''
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        return "Invalid Text, please remove numbers,symbols or spaces"
    else:
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_text = ""
        key_list = list(key)
        normal_list = list(normal)
        new_plain = text.upper()

        for i in range(len(new_plain)):
            if new_plain[i].isalpha():
                index = normal_list.index(new_plain[i])
                cipher_text = cipher_text + key_list[index]
            else:
                cipher_text = cipher_text + new_plain[i]
        return cipher_text


def decrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Decrypts the encrypted text as per the key'''

    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = ""
    key_list = list(key)
    normal_list = list(normal)
    new_plain = text.upper()
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        print("KeyError: Key is not valid")
        return
    else:
        for i in range(len(text)):
            if new_plain[i].isalpha():
                index = key_list.index(new_plain[i])
                plain_text = plain_text + normal_list[index]
            else:
                plain_text = plain_text + new_plain[i]
        return plain_text


@app.route("/enkrypt")
def homeencry():
    return render_template("en-home.html")


@app.route("/enkrypt_details", methods=["GET", "POST"])
def detencry():
    if request.method == "POST":
        text = request.form.get("text")
        radio = request.form.get("gridRadios")
        print(text, radio)
        if radio == "encrypt":
            fin = encrypt(text)
            return render_template("en-result.html", result=fin)
        else:
            fin = decrypt(text)
            return render_template("en-result.html", result=fin)
    return render_template("en-home.html")

'''
if __name__ == "__main__":
    app.run(debug=True)
'''