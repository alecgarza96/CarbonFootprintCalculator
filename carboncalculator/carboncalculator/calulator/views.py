from django.shortcuts import render

# Create your views here.
def calculator(request):
	return render(request, "calculator.html")

def footprint(request):
	footprint = 0

	footprint += (int(request.POST['electric_bill'])*105)
	footprint += (int(request.POST['gas_bill'])*105)
	footprint += (int(request.POST['oil_bill'])*113)
	footprint += (int(request.POST['yearly_mileage'])*.79)
	footprint += (int(request.POST['flights_over_four_hours'])*4400)
	footprint += (int(request.POST['flights_less_four_hours'])*1100)
	if request.POST['recycle_newspaper'] == "N":
		footprint += 184
	if request.POST['recycle_aluminum_tin'] == "N":
		footprint += 166
	return render(request, "footprint.html", {"footprint": footprint})
	