from twilio.rest import Client 
 
account_sid = 'AC6ed9a3d4980f356b73f5f79eea5890d1' 
auth_token = 'ff4041fb5781c75c40fcd23ae6bce208' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+905551747415' 
                          ) 
 
print(message.sid)
