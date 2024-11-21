from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Inventory
from .forms import InventoryForm

def cashier(request):
    items = Inventory.objects.all()
    context = {
        'items':items
    }
    return render(request, 'arcade/pos.html', context)

@login_required
def add_inventory(request):
    # Check if the user has an associated staff profile
    try:
        staff_profile = request.user.staff_profile
    except AttributeError:
        messages.error(request, "You don't have permission to upload inventory.")
        return redirect('inventory_list')

    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            # Save the form but don't commit to the database yet
            inventory_item = form.save(commit=False)
            # Associate the logged-in staff with the inventory
            inventory_item.staff = staff_profile
            inventory_item.save()
            messages.success(request, "Inventory item added successfully!")
            return redirect('inventory_list')
    else:
        form = InventoryForm()

    return render(request, 'arcade/inventory/add.html', {'form': form})

def inventory_list(request):
    items = Inventory.objects.all().order_by('-date')
    return render(request, 'arcade/inventory/list.html', {'items': items})


# Update Inventory View
def update_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Respond to AJAX request with success message
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True, "message": "Inventory item updated successfully!"})
            messages.success(request, "Inventory item updated successfully!")
            return redirect('inventory_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = InventoryForm(instance=item)
    return render(request, 'arcade/inventory/update_inventory.html', {'form': form})


# Delete Inventory View
def delete_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        item.delete()
        # Respond to AJAX request with success message
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"success": True, "message": "Inventory item deleted successfully!"})
        messages.success(request, "Inventory item deleted successfully!")
        return redirect('inventory_list')
    return render(request, 'arcade/inventory/delete_inventory.html', {'item': item})