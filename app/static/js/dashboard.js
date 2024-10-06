document.addEventListener('DOMContentLoaded', function () {
    // Function to handle note deletion
    function deleteNote(noteId) {
        if (confirm('Are you sure you want to delete this note?')) {
            fetch(`/note/${noteId}/delete`, { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Remove the note from the DOM
                        document.querySelector(`#note-${noteId}`).remove();
                    } else {
                        alert('Failed to delete the note. Please try again.');
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    }

    // Add event listeners to delete buttons
    document.querySelectorAll('.delete-note').forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const noteId = this.dataset.noteId;
            deleteNote(noteId);
        });
    });

    // Function to handle creating a new note
    document.querySelector('#new-note-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const title = this.querySelector('#new-note-title').value;
        const content = this.querySelector('#new-note-content').value;

        fetch('/note/new', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, content }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Reload the page to show the new note
                    window.location.reload();
                } else {
                    alert('Failed to create new note. Please try again.');
                }
            })
            .catch(error => console.error('Error:', error));
    });
});