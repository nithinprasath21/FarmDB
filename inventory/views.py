from django.shortcuts import render, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.contrib import messages
from django.contrib.auth import logout

# Initialize MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['farm_inventory']

# Admin Login View
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve user by username only
        user = db.admins.find_one({'username': username})

        if user:
            # Check if password matches
            if user['password'] == password:
                request.session['admin_id'] = str(user['_id'])  # Use session to track login
                messages.success(request, "")
                return redirect('dashboard')
            else:
                # Incorrect password, retain username in context
                messages.error(request, "Incorrect password. Please try again.")
                return render(request, 'admin_login.html', {'username': username})
        else:
            # Username not found
            messages.error(request, "Invalid username.")
            return redirect('admin_login')

    return render(request, 'admin_login.html')

# Admin Signup View
def admin_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'admin_signup.html', {'username': username})

        # Check if username already exists
        if db.admins.find_one({'username': username}):
            messages.error(request, "Username already exists.")
            return render(request, 'admin_signup.html', {'username': username})

        # Insert new admin into the database
        db.admins.insert_one({'username': username, 'password': password})
        messages.success(request, "Admin registered successfully.")
        return redirect('admin_login')

    return render(request, 'admin_signup.html')

# Dashboard view
def dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')

    stock_data = {
        'Vegetables': db.items.count_documents({'category': 'Vegetables'}),
        'Fruits': db.items.count_documents({'category': 'Fruits'}),
        'Liquids': db.items.count_documents({'category': 'Liquids'}),
    }

    # Retrieve item names and quantities for the chart
    items = db.items.find({}, {'item_name': 1, 'quantity': 1})
    item_data = [(item['item_name'], item['quantity']) for item in items]

    item_names = [item[0] for item in item_data]
    quantities = [item[1] for item in item_data]

    return render(request, 'dashboard.html', {
        'stock_data': stock_data,
        'item_names': item_names,
        'quantities': quantities
    })

# View to add a supplier and display existing suppliers
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        db.suppliers.insert_one({'name': name, 'contact': contact})
        return redirect('add_supplier')  # Redirect back to the same page

    suppliers = list(db.suppliers.find())
    # Rename `_id` to `id` for Django compatibility
    for supplier in suppliers:
        supplier['id'] = str(supplier.pop('_id'))  # Pop `_id` and store it as `id`
    return render(request, 'add_supplier.html', {'suppliers': suppliers})

# View to edit a supplier
def edit_supplier(request, id):
    supplier = db.suppliers.find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
        # Get updated data from the form
        updated_name = request.POST['name']
        updated_contact = request.POST['contact']
        
        # Update supplier details in the database
        db.suppliers.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': updated_name, 'contact': updated_contact}}
        )
        return redirect('add_supplier')

    return render(request, 'edit_supplier.html', {'supplier': supplier})

# View to delete a supplier
def delete_supplier(request, id):
    if request.method == 'POST':
        # Delete supplier from the database
        db.suppliers.delete_one({'_id': ObjectId(id)})
        return redirect('add_supplier')

# View to add a transporter and display existing transporters
def add_transporter(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        vehicle_number = request.POST['vehicle_number']
        db.transporters.insert_one({'name': name, 'contact': contact, 'vehicle_number': vehicle_number})
        return redirect('add_transporter')  # Redirect back to the same page

    transporters = list(db.transporters.find())
    for transporter in transporters:
        transporter['id'] = str(transporter.pop('_id'))  # Rename `_id` to `id`
    return render(request, 'add_transporter.html', {'transporters': transporters})

# View to edit a transporter
def edit_transporter(request, id):
    transporter = db.transporters.find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
        # Get updated data from the form
        updated_name = request.POST['name']
        updated_contact = request.POST['contact']
        updated_vehicle_number = request.POST['vehicle_number']
        
        # Update transporter details in the database
        db.transporters.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': updated_name, 'contact': updated_contact, 'vehicle_number': updated_vehicle_number}}
        )
        return redirect('add_transporter')

    return render(request, 'edit_transporter.html', {'transporter': transporter})

# View to delete a transporter
def delete_transporter(request, id):
    if request.method == 'POST':
        # Delete transporter from the database
        db.transporters.delete_one({'_id': ObjectId(id)})
        return redirect('add_transporter')

# View to add items
def add_items(request):
    suppliers = list(db.suppliers.find())

    for supplier in suppliers:
        supplier['id'] = str(supplier['_id'])  # Store `_id` as `id` in string format

    if request.method == 'POST':
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        supplier_id = request.POST['supplier']  # Get the selected supplier's ID
        
        # Insert the new item into the 'items' collection
        db.items.insert_one({
            'item_name': item_name,
            'quantity': quantity,
            'supplier_id': ObjectId(supplier_id)  # Store supplier_id as ObjectId
        })  # No need to capture inserted_id if not used

        return redirect('view_items')  # Redirect to a view that lists items after adding

    return render(request, 'add_items.html', {'suppliers': suppliers})

# View to see items
def view_items(request):
    items = list(db.items.find())
    
    # Fetch suppliers for mapping
    suppliers = {str(supplier['_id']): supplier['name'] for supplier in db.suppliers.find()}

    # Convert MongoDB ObjectId to string for template rendering
    for item in items:
        item['id'] = str(item['_id'])  # Ensure we are correctly assigning the ID
        # Add supplier name to each item
        item['supplier_name'] = suppliers.get(str(item['supplier_id']), 'Unknown Supplier')

    return render(request, 'view_items.html', {'items': items})


# View to edit an item
def edit_item(request, id):
    item = db.items.find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
        # Get updated data from the form
        updated_item_name = request.POST['item_name']
        updated_quantity = request.POST['quantity']
        updated_supplier_id = request.POST['supplier']  # Ensure you have the supplier id

        # Update item details in the database
        db.items.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'item_name': updated_item_name, 'quantity': updated_quantity, 'supplier_id': ObjectId(updated_supplier_id)}}
        )
        return redirect('view_items')

    suppliers = list(db.suppliers.find())
    for supplier in suppliers:
        supplier['id'] = str(supplier['_id'])  # Create a new key for the string ID

    return render(request, 'edit_item.html', {'item': item, 'suppliers': suppliers})

# View to delete an item
def delete_item(request, id):
    if request.method == 'POST':
        # Delete item from the database
        db.items.delete_one({'_id': ObjectId(id)})
        return redirect('view_items')

# View to populate initial data
def populate_items(request):
    initial_items = [
        {'item_name': 'Tomato', 'category': 'Vegetables', 'quantity': 20, 'supplier_id': None},
        {'item_name': 'Carrot', 'category': 'Vegetables', 'quantity': 15, 'supplier_id': None},
        {'item_name': 'Apple', 'category': 'Fruits', 'quantity': 10, 'supplier_id': None},
        {'item_name': 'Mango', 'category': 'Fruits', 'quantity': 8, 'supplier_id': None},
        {'item_name': 'Water', 'category': 'Liquids', 'quantity': 50, 'supplier_id': None},
        {'item_name': 'Milk', 'category': 'Liquids', 'quantity': 30, 'supplier_id': None},
    ]
    db.items.insert_many(initial_items)
    return redirect('dashboard')

# Logout View
def logout_view(request):
    # Clear session data and messages
    logout(request)  # Clear session data
    messages.get_messages(request)  # Initialize message queue to clear any messages
    return redirect('admin_login')