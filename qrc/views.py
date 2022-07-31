from django.shortcuts import render
from datetime import datetime as dt
import qrcode
rou= None

# Create your views here.

def index(request):
    global rou
    if request.method=='POST':
        x=request.POST
        print(x)
        print(x['link'])
        #img=qrcode.make(x['link'])
        #img.save("test.png")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=100,
            border=2 )
        qr.add_data(x['link'])
        qr.make(fit=True)
        img = qr.make_image(fill_color=x['fill'], back_color=x['back'])
        loc=dt.now()
        rou=f'qr/qr_{loc.year}{loc.month}{loc.day}_{loc.second}{loc.microsecond}.png'
        print(rou)
        img.save(f'static/{rou}')
    context={'rou':rou}
    return render(request, 'qrc/index.html', context)
