from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mandrill
from django.template import Context, loader
from django.conf import settings


@csrf_exempt
def front(request):

    if request.method == 'POST':

        which = request.POST['which']
        post_data = request.POST.copy()
        del post_data['which']

        subject = 'Ithacash Newsletter Signup' if which == 'email' else 'Message from ithacash.com'

        t = loader.get_template('emails/front.txt')
        c = Context({
            'post_data': post_data
        })
        message = t.render(c)

        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

        try:
            mandrill_client.messages.send(
                {
                    'to': [{'email': 'support@ithacash.com'}],
                    'html': message,
                    'from_name': 'Ithacash.com',
                    'from_email': request.POST['email'],
                    'subject': subject,
                })

            return (JsonResponse({'success': True}))

        except Exception, e:
            return (JsonResponse({'errors': str(e)}, status=500))

        else:
            return (JsonResponse({'errors': 'else'}, status=500))

    else:
        return render(request, 'front.html')


def getting_an_account(request):
    return render(request, 'getting.html')