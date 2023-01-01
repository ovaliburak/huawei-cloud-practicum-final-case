from twilio.rest import Client

def send_message_to_customer(*args, **kwargs):
    account_sid = 'AC6ed9a3d4980f356b73f5f79eea5890d1' 
    auth_token = 'ff4041fb5781c75c40fcd23ae6bce208' 
    client = Client(account_sid, auth_token)
    print(client)
    body = f"""
    Hello {args[0]["customer_name"]} {args[0]["customer_last_name"]}, 
we have a product for you. Product id: {args[0]["id"]}

Please contact your representative:
Name: {args[0]["employee_first_name"]}
Surname: {args[0]["employee_last_name"]}
Phone Number: {args[0]["employee_phone_number"]}
"""
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=body,      
                                to='whatsapp:+905551747415' 
                            ) 
    
    print(message.sid)
    
def send_message_to_employee(*args):
    account_sid = 'AC6ed9a3d4980f356b73f5f79eea5890d1' 
    auth_token = 'ff4041fb5781c75c40fcd23ae6bce208' 
    client = Client(account_sid, auth_token)
    
    body = f"""
The product number {args[0]["id"]} is in line with our customer's request. 
Please inform your customer about the product.

Customer information:
Name: {args[0]["customer_name"]}
Surname: {args[0]["customer_last_name"]}
Phone Number: {args[0]["customer_phone_number"]}
"""    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=body,      
                                to='whatsapp:+905551747415' 
                            ) 
    
    print(message.sid)
    
