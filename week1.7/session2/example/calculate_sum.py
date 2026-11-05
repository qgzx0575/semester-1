# Week 1.7, Session 2

# Example code with logic error that does not throw any errors

def calculate_total(cart_items):
    subtotal = sum(cart_items)
    
    if subtotal > 50:
        subtotal * 0.90  
        
    final_total = subtotal + 5
    return final_total

calculate_total([20, 30, 10])