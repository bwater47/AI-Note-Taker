document.addEventListener('DOMContentLoaded', function () {
    const noteForm = document.querySelector('#note-form');
    const noteContent = document.querySelector('#note-content');
    let saveTimeout;

    // Function to save note content
    function saveNote() {
        const noteId = noteForm.dataset.noteId;
        const content = noteContent.value;

        fetch(`/note/${noteId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Note saved successfully');
                } else {
                    console.error('Failed to save note');
                }
            })
            .catch(error => console.error('Error:', error));
    }

    // Auto-save on content change
    noteContent.addEventListener('input', function () {
        clearTimeout(saveTimeout);
        saveTimeout = setTimeout(saveNote, 1000); // Save after 1 second of inactivity
    });

    // Handle note summarization
    document.querySelectorAll('.summarize-btn').forEach(button => {
        button.addEventListener('click', function () {
            const noteId = noteForm.dataset.noteId;
            const summaryType = this.dataset.summaryType;

            fetch(`/note/${noteId}/summarize`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ summary_type: summaryType }),
            })
                .then(response => response.json())
                .then(data => {
                    if (data.summary) {
                        document.querySelector('#summary-result').textContent = data.summary;
                    } else {
                        console.error('Failed to generate summary');
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

    // Copy note content
    document.querySelector('#copy-note').addEventListener('click', function () {
        noteContent.select();
        document.execCommand('copy');
        alert('Note content copied to clipboard!');
    });
});