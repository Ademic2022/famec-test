from models import storage
from models.user import User
from models.family import Family
from flask import Blueprint, render_template, url_for,request, flash, redirect
from flask_login import logout_user, login_user
# import string, random

import hashlib
import re

auth = Blueprint('auth', __name__)

# def generate_random_id(length=8):
#     characters = string.ascii_letters + string.digits
#     random_id = ''.join(random.choices(characters, k=length))
#     return random_id
# random_id = generate_random_id()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the form submission
        email = request.form.get('email')
        password = request.form.get('password')
        hash_password = hashlib.md5(password.encode()).hexdigest()

        user = storage.find_user_by_email(email)
        if user:
            if hash_password == user.password:
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else: 
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User with this email does not exist', category='error')

    return render_template('auth/login.html') 

# REGISTER ROUTE FUNCTIONALITY
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        user_data = {
            "firstname": request.form.get('firstname'),
            "lastname": request.form.get('lastname'),
            "username": request.form.get('username'),
            "password": request.form.get('password'),
            "confirm_pass": request.form.get('confirm_pass'),
            "email": request.form.get('email'),
            "address": request.form.get('address'),
            "zipcode": request.form.get('zipcode'),
            "country": request.form.get('country'),
            "state": request.form.get('state'),
            "birth_month": request.form.get('birth_month'),
            "birth_day": request.form.get('birth_day'),
            "t_c": request.form.get('t_c')
        }
        existing_user = storage.find_user_by_email(user_data['email'])
        if existing_user:
            flash('Email already exists. Please login.', category='error')
        elif len(user_data['firstname']) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif len(user_data['lastname']) < 2:
            flash('Last Name must be greater than 1 character', category='error')
        elif user_data['password'] != user_data['confirm_pass']:
            flash('Passwords do not match', category='error')
        elif len(user_data['password']) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_data['email']):
            flash('Invalid email address', category='error')
        elif len(user_data['zipcode']) > 5:
            flash('Invalid zipcode', category='error')
        elif 't_c' not in user_data:
            flash('You must accept the terms and conditions to register', category='error')
        # elif any(not user_data[field] for field in ['firstname', 'lastname', 'password', 'confirm_pass', 'email', 'address', 'zipcode', 'country', 'state', 'birth_month', 'birth_day']):
        #     flash('All fields are required', category='error')
        else:
            family_option = request.form.get('family_option') == 'create'  # Assuming you have a checkbox in your form
            if family_option:

                family_name = request.form.get('family_name')  # Get the family name from the form
                if not family_name:
                    flash('Family name is required to create a new family', category='error')
                    return render_template('auth/register.html', user_data=user_data)  # Display the registration form again
                if all(user_data[field] for field in ['firstname', 'lastname', 'password', 'confirm_pass', 'email', 'address', 'zipcode', 'country', 'state', 'birth_month', 'birth_day']):
                    # All checks passed, proceed with registration
                    birthday = f"{user_data['birth_month']}/{user_data['birth_day']}"
                    new_user = User(
                        firstname=user_data['firstname'],
                        lastname=user_data['lastname'],
                        username=user_data['username'],
                        password=user_data['password'],
                        email=user_data['email'],
                        address=user_data['address'],
                        zipcode=user_data['zipcode'],
                        country=user_data['country'],
                        state=user_data['state'],
                        birthday=birthday
                    )


                    # store user in database
                    storage.new(new_user)
                    storage.save()

                     # Now, obtain the user ID after the user has been added to the database
                    new_user = storage.find_user_by_email(user_data['email'])
                    # Create a new family instance and associate it with the user
                    new_family = Family(name=family_name, owner_id=new_user.id)

                    new_user.family = new_family

                    # Store the updated user in the database with the associated family
                    storage.save()

                    flash('Registration successful', category='success')
                    return redirect(url_for('auth.login'))
            else:
                family_id = request.form.get('family_id')

                if not family_id:
                    flash('Please select an existing family to join', category='error')
                    return render_template('auth/register.html', user_data=user_data)  # Display the registration form again
                
                if all(user_data[field] for field in ['firstname', 'lastname', 'password', 'confirm_pass', 'email', 'address', 'zipcode', 'country', 'state', 'birth_month', 'birth_day']):
                    # All checks passed, proceed with registration
                    birthday = f"{user_data['birth_month']}/{user_data['birth_day']}"
                    new_user = User(
                        firstname=user_data['firstname'],
                        lastname=user_data['lastname'],
                        username=user_data['username'],
                        password=user_data['password'],
                        email=user_data['email'],
                        address=user_data['address'],
                        zipcode=user_data['zipcode'],
                        country=user_data['country'],
                        state=user_data['state'],
                        birthday=birthday
                    )

                    # Query the database to get the selected family
                    selected_family = storage.get_family_by_id(family_id)
                    if selected_family:
                        
                        # Associate the user with the selected family
                        new_user.family = selected_family
                        # Store user with the associated family in the database
                        storage.new(new_user)
                        storage.save()
                        message = f"You have successfully registered and joined {selected_family.name}'s Family"
                        flash(message, category='success')
                        return redirect(url_for('auth.login'))
                    else:
                         # Handle the case where the selected family doesn't exist
                        flash('The selected family does not exist', category='error')
                        return render_template('auth/register.html', user_data=user_data)  # Display the registration form again
        
        return render_template('auth/register.html', user_data=user_data)
    
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
