# created by Ali Hassan Faris 
# render import from django that helps with the html update 
from django.shortcuts import render

# Initiation of the Calculation function with a request parameter
def calculator(request):
    # Check if the request method is 'POST'
    if request.method == 'POST':
        
        # Get the value of the 'result' input field from the form data
        result = request.POST.get('result')
        
        # Get the value of the 'value' input field from the form data
        value = request.POST.get('value')
        
        # Get the value of the 'clear' input field from the form data
        clear = request.POST.get('clear')
        
        # Get the value of the 'calculate' input field from the form data
        calculate = request.POST.get('calculate')
        
        # Check if the 'clear' button was clicked
        if clear:
            # Reset the 'result' to an empty string
            result = ''
        
        # Check if a number or operator button was clicked
        elif value:
            # Append the clicked value to the 'result'
            result += value
        
        # Check if the 'calculate' button was clicked
        elif calculate:
            try:
                # Evaluate the 'result' expression and convert it to a string
                result = str(eval(result))
            except:
                # Handle any evaluation errors and set 'result' to 'Error'
                result = 'Error'
        
        else:
            # Set the initial 'result' to '0'
            result = '0'
        
        # Render the 'index.html' template with the updated 'result'
        return render(request, 'index.html', {'result': result})
    
    else:
        # Render the 'index.html' template with the initial 'result' as '0'
        return render(request, 'index.html', {'result': '0'})
