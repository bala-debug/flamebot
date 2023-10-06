from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "BOT_TOKEN"
app = Flask(__name__)
#command code
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt


def remove_match_char(list1, list2):
 

    for i in range(len(list1)):

        for j in range(len(list2)):
 

            

            if list1[i] == list2[j]:

                c = list1[i]
 

                
                list1.remove(c)

                list2.remove(c)
 


                list3 = list1 + ["*"] + list2
 

                

                return [list3, True]
 

    

    list3 = list1 + ["*"] + list2

    return [list3, False]

def flames(txt):
    a,b=txt.split(",")
    a=a.lower()
    b=b.lower()
    a.replace(" ", "")
    b.replace(" ", "")
    a_list=list(a)
    b_list=list(b)
    proceed = True
    while proceed:
        ret_list = remove_match_char(a_list, b_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        a_list = con_list[: star_index]
        b_list= con_list[star_index + 1:]
    count = len(a_list) + len(b_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left
        else:
            result = result[: len(result) - 1]
    return result[0]
 
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       msg = request.get_json()
      
       chat_id,txt = parse_message(msg)
       if txt == "/start":
            tel_send_message(chat_id,"Send the names separated by comma to calculate")
       elif txt =="Dhamo":
           tel_send_message(chat_id,"Aavan oru pottA")

       elif txt =="vetri":
           tel_send_message(chat_id,"Body Uhhh!!!!!")

       else:
          telmsg="Your relationship is : "+flames(txt)
          print(telmsg)
          tel_send_message(chat_id,telmsg)

       return Response('OK',status=200)
    else:
       return "<h1>Vannakam</h1>"
    
if __name__ == '__main__': 
  app.run(debug=True) 
