import pypff
import pandas as pd
import re

def getKey(datastr):
    rtnStr=''
    # (\(|\[)?\s*CHTI TT:\s*\d{8}_\d{3}
    pattern1='CHTI TT:\s*\d{8}_\d{3}'
    pattern2=''
    rtnStr=re.findall(pattern1,datastr)
    if len(rtnStr) > 0:
        rtnStr = rtnStr[0].replace(' ','')
    else:
        rtnStr=''
    
    return rtnStr

# def modifySTR(datastr):
#     datastr = datastr.replace('[外部郵件]','').replace('RE:','').replace('回复: ','').replace('( ','(').replace(' )',')').strip()
#     return datastr

pst = pypff.file()
pst.open(".\\01_tempIC.pst")

root = pst.get_root_folder()
def parse_folder(base):
    messages = []
    for folder in base.sub_folders:
        if folder.number_of_sub_folders:
             messages += parse_folder(folder)
                   
        for message in folder.sub_messages:
            messages.append({
                "subject": message.subject,
                "sender": message.sender_name,
                "header": message.transport_headers,
                "body": message.plain_text_body.decode(),
                "client_submit_time": message.client_submit_time,
                "delivery_time": message.delivery_time,
                "attachments": message.attachments,
                "key": getKey(message.conversation_topic),
                "conversation_topic": message.conversation_topic,
                "number_of_attachments": message.number_of_attachments
                })
    return messages

messages = parse_folder(root)
# df = pd.DataFrame(messages)
# prin``t(df['conversation_topic'])
# df.to_excel(".\\01_tempRSP.xls")

for message in messages:
    #  print(message['delivery_time']," <--> ",message['key']," <--> ",message['body'])
    print(message)
