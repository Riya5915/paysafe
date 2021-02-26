from django.shortcuts import render
import requests, json, random
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
from django.urls import reverse


CORS_ALLOWED_ORIGINS = [
    'https://api.test.paysafe.com/paymenthub/v1/payments',
    'http://localhost:8000'
]

response_headers = {
    "Access-Control-Allow-Origin": "*"
}

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CSRF_TRUSTED_ORIGINS = [
    'https://api.test.paysafe.com/paymenthub/v1/payments',
    'http://localhost:8000'
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

formData = []
# Create your views here.
@csrf_exempt
def index(request):
    print("form submission done here")
    return render(request, "payments/index.html")

@csrf_exempt
def getFormData(request):
    if(request.method == "POST"):
        form = request.POST
        print(form)
        print(form['emailid'])

        # createCustomer()

        key = "Basic cHJpdmF0ZS03NzUxOkItcWEyLTAtNWYwMzFjZGQtMC0zMDJkMDIxNDQ5NmJlODQ3MzJhMDFmNjkwMjY4ZDNiOGViNzJlNWI4Y2NmOTRlMjIwMjE1MDA4NTkxMzExN2YyZTFhODUzMTUwNWVlOGNjZmM4ZTk4ZGYzY2YxNzQ4"
        url = 'https://api.test.paysafe.com/paymenthub/v1/customers'
        mci = ((form['emailid'].split('@'))[0])+str(random.randint(1001,100001))
        params = {
            "merchantCustomerId": mci,
            "currency": "USD",
            "amount": form['amount'],
            "locale": "en_US",
            "firstName": form['fname'],
            "middleName": "",
            "lastName": form['lname'],
            "dateOfBirth": {
                "year": 1981,
                "month": 10,
                "day": 24
            },
            "billingAddress": {
                "nickName": form['fname']+" "+form['lname'],
                "street": form['address'],
                "city": form['city'],
                "zip": form['zipcode'],
                "country": "US",
                "state": "CA"
            },
            "email": form['emailid'],
            "phone": form['phone'],
            "ip": "192.0.126.111",
            "gender": "M",
            "nationality": "Canadian",
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': key,
            'Simulator': '"EXTERNAL"',
        }

        getid = {
            'merchantCustomerId': mci
        }

        try:
            r = requests.get(url, params=getid, headers=headers)
            print("inside try, get request done\n")
            try:
                data = r.json()
                if data['error']:
                    raise Exception
                else:
                    print("successfully done")
            except:
                print("inside try inside except\n")
                raise Exception
        except:
            r = requests.post(url, data=json.dumps(params), headers=headers)
            print("inside catch, post request done\n")

        content = r.json()
        print(content)
        print(content['id'])

        token = createSingleUseToken(content, headers)
        print(token)
        print("token returned")

        return render(request, ("payments/checkout.html"), {
            "token": json.dumps(token),
            "content": content,
            "data": params,
            "form": json.dumps(form)
        })
    else:
        return render(request, "payments/index.html")

@csrf_exempt
def createSingleUseToken(content, headers):

    url = "https://api.test.paysafe.com/paymenthub/v1/customers/"+ content['id'] +"/singleusecustomertokens"
    mrno = "Ref"+content['merchantCustomerId']
    params = {
        "merchantRefNum": mrno,
        "paymentTypes": [
            "CARD"
        ]
    }

    r = requests.post(url, data=json.dumps(params), headers=headers)
    rdata = r.json()
    print("single use token id = " + rdata['singleUseCustomerToken'])
    print("inside catch, post request done\n")

    user = UserInfo(
        merchantCustomerId=content['merchantCustomerId'],
        customerid=content['id'],
        paymentToken=content['paymentToken'],
        singleUsePaymentHandle=rdata['id']
    )
    user.save()
    rdata['merchantRefNumber'] = mrno
    return rdata

@csrf_exempt
def checkout(request, token, data, content, form):
    return render(request, "payments/checkout.html", {
        "token": token,
        "form": form,
        "data": data,
        "content": content
    })