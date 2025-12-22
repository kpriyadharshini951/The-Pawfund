from django.shortcuts import render
from .models import Donation
from .models import Adoption



def home(request):
    return render(request, 'myapp/home.html')


def dogs(request):
    return render(request, 'myapp/dogs.html')


def donate(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        if amount:
            Donation.objects.create(amount=amount)
            return render(request, 'myapp/dogs.html', {'message': f"Thank you for donating Rs.{amount}!"})
    return render(request, 'myapp/dogs.html')


def adopt(request):
    if request.method == "POST":
        dog = request.POST.get('dog_name')
        adopter = request.POST.get('adopter_name')

        if dog and adopter:
            
            if Adoption.objects.filter(dog_name=dog).exists():
                return render(request, 'myapp/dogs.html', {
                    'message': f"❌ {dog} has already been adopted!"
                })

            
            Adoption.objects.create(dog_name=dog, adopter_name=adopter)
            return render(request, 'myapp/dogs.html', {
                'message': f"🎉 {adopter}, adoption confirmed for {dog}! Thank you for giving a loving home 🐶💙"
            })

    return render(request, 'myapp/dogs.html')
