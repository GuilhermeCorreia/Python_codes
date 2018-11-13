import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os
import getpass


import win32com.client


def email_sender(email_from, email_to, email_subject, email_body, attachment_pathlist=[]):
    msg = MIMEMultipart()
    msg['FROM'] = email_from
    msg['To'] = email_to
    msg['Subject'] = email_subject

    body = email_body
    msg.attach(MIMEText(body, 'plain'))

    if len(attachment_pathlist)>0:
        for file in attachment_pathlist:
            name = os.path.basename(file)
            part = MIMEBase('application', 'octet-stream')

            with open(file, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % name)

            msg.attach(part)

    text = msg.as_string()
    
    server = smtplib.SMTP('srvmail-sp.pactual.net')
    server.sendmail(email_from, email_to.split(';') , text)
    server.quit()


# In[3]:

def email_confirmation(cliente, search_string, data, email_sender,folders_search = [], main_folder='Inbox', total = 1000):
    #path=r'\\DRIOC0231PFS\Apoio_SB\Geral\BD\Confirmations\confirmacoes_pdf'
    path = r'C:\Users\correigu\OneDrive - Banco BTG Pactual S.A\Documents\offshore'
    outlook = win32com.client.Dispatch('outlook.application')
    namespace = outlook.GetNamespace("MAPI")
    dict_index = {}
    i=1
    j=0
    for folder in namespace.Folders:
        dict_index.update({str(folder).lower():i})
        i+=1

    root_folder = namespace.Folders.Item(dict_index[email_sender])
    print(root_folder)
    
    cliente = cliente.lower()
    data = data[-4:]+data[3:5]+data[:2]
    
    if os.path.isdir(path+'\\'+cliente)==True:
        if os.path.isdir(path+'\\'+cliente+'\\'+data)==False:
            os.mkdir(path+'\\'+cliente+'\\'+data)
    else:
        os.mkdir(path+'\\'+cliente)
        os.mkdir(path+'\\'+cliente+'\\'+data)
    n_path = path+'\\'+cliente+'\\'+data
    
    for folder in folders_search:
        print(main_folder)
        print(folder)
        subfolder = root_folder.Folders[main_folder].Folders[folder]
        message = subfolder.Items
    
        for msg in message:
            if j>total:
                break
            else:
                body_content = msg.body
                msg_sub = msg.Subject
                if (search_string in body_content)&(data in msg_sub):
                    count_attachments = msg.Attachments.Count

                    string = msg_sub.split(" ")
                    for i in range(0, len(string)):
                        if string[i] == 'of':
                            ticker = string[i+1]
                            if '*' in ticker:
                                ticker = ticker.replace("*", '')
                            elif "&" in ticker:
                                ticker = ticker.replace("&", '')

                    if count_attachments > 0:
                        for item in range(count_attachments):
                            file_name = msg.Attachments.Item(item + 1).Filename
                            if '.pdf' in file_name:
                                attach = msg.Attachments.Item(item+1)
                                attach.SaveAsFile(n_path+'\\'+str(j)+' - '+ticker+'.pdf')
                                j+=1