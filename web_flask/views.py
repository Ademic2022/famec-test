from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify
from flask_login import login_required, current_user
from models import storage
from models.task import Task
from models.notification import Notification
import json
from werkzeug.routing import UUIDConverter
from .context_processors import inject_globals

views = Blueprint('views', __name__)
@views.context_processor
def inject_global():
    return inject_globals()

# Define a sample route that uses the family_tasks variable
"""Route to Landing PAGE"""
@views.route('/')
def landing_page():
    background_image_urls = [
        url_for('static', filename='images/home1.jpg'),
        url_for('static', filename='images/home2.jpg'),
        url_for('static', filename='images/home3.jpg'),
        url_for('static', filename='images/famec_landn_1.jpg'),
        url_for('static', filename='images/Famec_logo_white.png'),
        url_for('static', filename='images/famec_landn_2.jpg'),
        url_for('static', filename='images/famec_landn_3.jpg'),
        url_for('static', filename='images/family.jpg')
    ]
    return render_template('landing_page.html', images = background_image_urls)

@views.route('/dashboard')
@login_required
def dashboard():
    # Assuming you have a datetime field named 'created_at' in your Task model
    user = current_user
    user_tasks = user.tasks
    recent_tasks = user_tasks[:3]  
    
    return render_template('dashboard.html', user=user, recent_tasks=recent_tasks)

@views.route('/users')
@login_required
def users():
    return render_template('users.html', user = current_user)

@views.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        # Process the form submission
        task_title = request.form.get('task_title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        due_date = request.form.get('due_date')
        user_id = current_user.id
        family_id = current_user.family_id
        status = request.form.get('status')
        if status:
            status = 1
        else:
            status = 0
        if priority == 'High':
            priority = 2
        elif priority == 'Medium':
            priority = 1
        else:
            priority = 0

        if len(description) < 5:
            flash('please give more detailed description', category='error')
        elif len(task_title) < 2:
            flash('detailed title is required', category='error')
        elif len(due_date) < 1:
            flash('please set due date', category='error')
        else:
            new_task = Task(title=task_title, description=description, due_date=due_date, user_id=user_id, family_id=family_id, status = status)
            storage.new(new_task)
            storage.save()

            # Get all family members (excluding the creator)
            family_members = storage.get_all_families(new_task.family_id)
            for member in family_members:
                # print(member.firstname)
                if member.id != new_task.user_id:  # Exclude the creator
                    content = f"A new task '{new_task.title}' has been created in your family."
                    notification = Notification(
                        sender=current_user,
                        recipient=member,  # Use the member's ID as the recipient
                        content=content,
                        family_id=new_task.family_id
                    )
                    storage.new(notification)

            storage.save()
                        


            flash('New Task added Successfully', category='success')
            return redirect(url_for('views.tasks'))
    family_tasks = current_user.family.tasks
    return render_template('task.html', user = current_user, family_tasks=family_tasks)

@views.route('/notification')
@login_required
def notification():
    profile_image = [
        url_for('static', filename='images/avatar.png')
    ]
    user_id = current_user.id
    notifications = storage.get_notifications(user_id)
    return render_template('notification.html', user = current_user, profile_image=profile_image, notifications=notifications)

@views.route('/events')
@login_required
def events():
    return render_template('events.html', user = current_user)

@views.route('/family')
@login_required
def family():
    profile_image = [
        url_for('static', filename='images/avatar.png')
    ]
    user_family_id = current_user.family_id
    families = storage.get_all_families(user_family_id)
    return render_template('family.html', user = current_user, image=profile_image, families=families)

@views.route('/settings')
@login_required
def settings():
    profile_image = [
        url_for('static', filename='images/avatar.png')
    ]
    user_family_id = current_user.family_id
    family_name = storage.find_family_name(user_family_id)
    return render_template('settings.html', user = current_user, image=profile_image, family=family_name)

@views.route('/delete-task', methods=['POST'])
def delete_task():
    data = json.loads(request.data)
    taskId = data['taskId']
    task = storage.get_task_by_id(taskId)

    if not task:
        return jsonify({'error': 'Task not found'}), 404
    else:
        if task.user_id == current_user.id:
            # Delete the task from the database (you should have a method for this)
            storage.delete(task)
            storage.save()

            # Return a success message
            flash('Task Deleted Successfully', category='success')
            return jsonify({'message': 'Task deleted successfully'}), 200

@views.route('/update-task/<string:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    # Fetch the task from the database based on task_id
    task = storage.get_task_by_id(task_id)
    
    if not task:
        # Handle the case where the task doesn't exist or an error occurs
        # You can return an error message or appropriate status code
        flash("Task not found or error fetching task", category='error')
        return redirect(url_for('views.tasks'))
    
    if request.method == 'POST':
        # Retrieve form data from the POST request
        task_title = request.form.get('task_title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        due_date = request.form.get('due_date')
        status = request.form.get('status')
        
        # Convert the 'status' value to an integer
        if status:
            status = 1
        else:
            status = 0

        if priority == 'High':
            priority = 2
        elif priority == 'Medium':
            priority = 1
        else:
            priority = 0

        # Update task attributes
        task.title = task_title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        task.status = status
        
        # Save the updated task
        storage.update(task)
        flash('Task updated Successfully', category='success')
    
    # If the request is a GET request (e.g., to fetch task data for AJAX update)
    task_data = {
        'title': task.title,
        'description': task.description,
        'priority': task.priority,
        'due_date': task.due_date,
        'status': task.status,
        'id': task.id
        # Add other task attributes here
    }
    
    return jsonify(task_data)