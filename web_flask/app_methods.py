def inject_globals():
    from models import storage
    from flask_login import current_user

    
    if current_user.is_authenticated:
        # task counter
        task_counter = storage.count('Task', current_user.family_id) if storage.count('Task', current_user.family_id) > 0 else 0
        # notification counter
        notification_counter = storage.count_distinct_notifications(current_user.id) if storage.count_distinct_notifications(current_user.id) > 0 else 0
        # Image display
        img_url = current_user.profile_img if current_user.profile_img else ''
        return {
            'task_counter': task_counter, 
            'notification_counter':notification_counter,
            'profile_image':img_url
            }
    else:
        return {
            'task_counter': 0, 
            'notification_counter':0,
            'profile_image':0
            }

# Allowed image extensions
def allowed_file(filename):
    # Check if the file has a valid extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in set(["jpg", "jpeg", "png", "gif"])

