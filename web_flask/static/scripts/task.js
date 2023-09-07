// Function to handle the "Add New Task" modal
$(function() {
    $("#new_task").click(function() {
        $(".new_task").modal('show');
    });

    $(".new_task").modal({
        closable: true
    });
});
// checkbox
$('.ui.checkbox').checkbox();
// Function to handle the "Update Task" modal
$(function() {
    $("#update-task-button").click(function() {
        // Get the task ID from the data attribute
        const taskId = $(this).data('task-id');

        // You can now use taskId to fetch the task data via an AJAX request
        // and populate the update modal with the task data
        fetchTaskDataAndOpenModal(taskId);
    });

    $(".update_task").modal({
        closable: true
    });
});

// Function to fetch task data via AJAX and open the "Update Task" modal
function fetchTaskDataAndOpenModal(taskId) {
    $.ajax({
        url: '/update-task/' + taskId.toString(), // Adjust the URL to your Flask route for fetching task data
        type: 'GET',
        success: function(data) {
            // Use data to populate the update modal
            // For example, if you receive JSON data, set form fields like this:
            $('.update_task').find('[name="task_title"]').val(data.title);
            $('.update_task').find('[name="description"]').val(data.description);
            $('.update_task').find('[name="priority"]').val(data.priority);
            $('.update_task').find('[name="due_date"]').val(data.due_date);
            // Populate other form fields as needed
            // Then, open the modal
            $('.update_task').modal('show');
        },
        error: function(error) {
            // Handle any errors here
        }
    });
}

// Function to handle the "Delete Task" modal
$(function() {
    $(".delete-task-button").click(function(event) {
        const taskId = $(event.currentTarget).data('task-id');
        // Set the taskId in the hidden input field in the modal
        $("#taskIdInput").val(taskId);
        // Show the delete modal
        $(".delete_modal.modal").modal('show');
    });

    $(".delete_modal.modal").modal({
        closable: true
    });

    // Handle the delete confirmation button click
    $("#confirmDeleteButton").click(function() {
        // Get the taskId from the hidden input field
        const taskId = $("#taskIdInput").val();

        // Send a POST request to delete the task
        fetch('/delete-task', {
            method: 'POST',
            body: JSON.stringify({ taskId: taskId }),
        })
        .then((_res) => {
            // Reload the page or perform any necessary actions
            window.location.reload();
        });
    });
});

$(document).ready(function() {
    let taskId; // Define taskId in the outer scope
    $('.update-task-button').click(function() {
        // Get the task ID from the data attribute
        taskId = $(this).data('task-id');
        
        // You can now use taskId to fetch the task data via an AJAX request or other means
        // For example, you can use AJAX to fetch the task data and populate the modal dynamically
        $.ajax({
            url: '/update-task/' + taskId.toString(), // Adjust the URL to your Flask route for fetching task data
            type: 'GET',
            success: function(data) {
                // Use data to populate the update modal
                // For example, if you receive JSON data, you can set form fields like this:
                $('.update_task').find('[name="task_id"]').val(data.id);
                $('.update_task').find('[name="task_title"]').val(data.title);
                $('.update_task').find('[name="description"]').val(data.description);
                $('.update_task').find('[name="priority"]').val(data.priority);
                $('.update_task').find('[name="due_date"]').val(data.due_date);
                // Populate other form fields as needed
                // Then, open the modal
                $('.update_task').modal('show');
            },
            error: function(error) {
                // Handle any errors here
            }
        });
    });

    $('.update_task form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
    
        // Debug: Check if the function is called
        console.log('Form submit event fired');
    
        // Serialize the form data into a format that can be sent as POST data
        const formData = $(this).serialize();
    
        // Debug: Check if formData is correctly serialized
        console.log('Form data:', formData);
    
        // Send a POST request to update the task
        fetch(`/update-task/${taskId}`, {
            method: 'POST',
            body: formData,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then((response) => {
            if (response.ok) {
             // Reload the page
                window.location.href = '/tasks';
            } else {
                // Handle the case where the update was not successful
                console.error('Error updating task:', response.statusText);
            }
        })
        .catch((error) => {
            // Handle any errors here
            console.error('Error updating task:', error);
        });
    });
    
    
});