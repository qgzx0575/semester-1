# Week 1.7, Session 2

# Example code with logic error that does not throw any errors
# To find where the logic breaks, inject print() statements
# to track the variables at each critical step

def calculate_total(cart_items):
    subtotal = sum(cart_items)
    print(f"[DEBUG 1] Initial subtotal: {subtotal}") # Track starting state
    
    if subtotal > 50:
        subtotal * 0.90  
        print(f"[DEBUG 2] Inside discount block. Subtotal is now: {subtotal}") 
        
    final_total = subtotal + 5
    print(f"[DEBUG 3] Final total before return: {final_total}")
    return final_total

calculate_total([20, 30, 10])