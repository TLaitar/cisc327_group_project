from flask import Blueprint, redirect, session, request, make_response
import qa327.library.validation as valid
import qa327.library.tickets as tic

'''
The following functions allow the user to fill out ticket name, quantity,
price and expiration date in order to update a ticket.
If the ticket fails to post, users are given an error message and redirected
to the homepage
'''

update_page = Blueprint('update_page', __name__)

@update_page.route('/', methods=['GET'])
def update_get():
    return redirect('/', code=303)

@update_page.route('/', methods=['POST'])
def update_post():
    ticket_name = request.form.get('ticket_name')
    email=session['logged_in']
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    expiration = request.form.get('expiration')
    errors=[]
    update_msg='failed to update ticket'
    
    if not valid.validate_name(ticket_name):
        errors.append("The name of the ticket mys be more than 60 characters")
    if not valid.validate_quantity(quantity) and int(quantity)!=0:
        errors.append("You may only sell between 0 and a hundred tickets inclusive")
    if not valid.validate_price(price):
        errors.append("Prices must be between $10 and $100 (whole numbers only)")
    if len(errors) == 0:
        ticket = tic.update_ticket(ticket_name, quantity, price, expiration, email)
        if ticket is None:
            if int(quantity)==0:
                 update_msg='Successfully removed the ticket(s)'
                
            else:
                update_msg='Successfully listed the ticket(s)'
        else:
            errors.append(ticket)
    if len(errors) > 0:
        update_msg += ", ".join(errors)+"." #adding all of the errors to the updat message
        
    resp=make_response(redirect('/', code=303))
    resp.set_cookie('update_msg', update_msg)
    return resp

    '''ticket = tic.update_ticket(ticket_name, quantity, price, expiration)
    #If ticket exists return None, else print error message
    if ticket:
        #debug
        #print('debug: failed to update ticket')
        #print("successfully updated ticket listing")
        update_message="successfully updated ticket listing"
    
    else:
        update_message="failed to update ticket"
        
    return render_template('index.html',update_message=update_message)
    return redirect('/', code=303)
    '''
