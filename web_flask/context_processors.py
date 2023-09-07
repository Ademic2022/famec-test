from models import storage
from flask_login import current_user

# def inject_globals():
#     task_counter = storage.count(Task)
#     return {'task_counter': task_counter}
def inject_globals():
    if current_user.is_authenticated:
        task_counter = storage.count('Task', current_user.family_id)
    else:
        task_counter = 0

    if current_user.is_authenticated:
        notification_counter = storage.count_distinct_notifications(current_user.id)
    else:
        notification_counter = 0
    return {'task_counter': task_counter, 'notification_counter':notification_counter}
