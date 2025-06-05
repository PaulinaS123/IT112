from django.shortcuts import render


def home_view(request):
    # Get the user_name parameter from the URL query string (?user_name=YourName)
    user_name = request.GET.get('user_name', None)  # None if not provided

    # Prepare context to send to the template
    context = {
        'user_name': user_name
    }

    # Render the template with the context
    return render(request, 'base.html', context)
