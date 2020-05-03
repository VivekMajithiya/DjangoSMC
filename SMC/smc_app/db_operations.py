from smc_app.models import ChatData

def insertChatData(name='M',text='Dummy text',ctype='T'):
    chatdata = ChatData(name=name,text=text,ctyp=ctype)
    chatdata.save()

if __name__ == "__main__":
    insertChatData('M','This is new data inserted','T')
