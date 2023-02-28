from django.shortcuts import render, redirect
from apps.authentication.models import CustomUser
from wallet.models import UserWallet
import random, string
from django.utils import timezone
from .models import Coupon
# Create your views here.


def FundDeposit(request):
    msg=""
    if request.method == "POST":
        try:
            amount = request.POST["amount"]
            getUser= CustomUser.objects.get(username=request.user.username)
            receiver = UserWallet.objects.get(user = getUser)           
            receiver.balance  += int(amount)
            receiver.save()
            msg = "Transaction Success"
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again"
    user = UserWallet.objects.get(user=request.user)
    return render(request,'home/fund-deposit.html',{"balance":user.balance,"msg":msg})


#------------------------------------------------- coupon generation function -----------------------------------


def GenerateCoupons(request):
    if request.method == 'POST':
        getUser= CustomUser.objects.get(username=request.user.username)
        deductamount = UserWallet.objects.get(user = getUser) 
        discount_amount = request.POST['discount_amount']
        deductamount.balance -= int(discount_amount)
        expiration_date = request.POST['expiration_date']
        deductamount.save()
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        coupon = Coupon(code=code, discount_amount=discount_amount, expiration_date=expiration_date)
        coupon.save()
        return redirect('coupon_list')
    return render(request, 'home/generate_coupon.html')



def CouponList(request):
    coupons = Coupon.objects.all()
    return render(request, 'home/coupon_list.html', {'coupons': coupons})

def use_coupon(request, coupon_id):
    coupon = Coupon.objects.get(pk=coupon_id)
    coupon.is_used = True
    coupon.save()
    return redirect('coupon_list')

def delete_coupon(request, coupon_id):
    coupon = Coupon.objects.get(pk=coupon_id)
    coupon.delete()
    return redirect('coupon_list')



