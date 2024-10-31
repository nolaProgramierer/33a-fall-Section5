document.addEventListener('DOMContentLoaded', () => {

    // Show/hide error message
    const showVoteErrorMsg = (msg, id) => {
        const msgDiv = document.querySelector(`.vote-msg[data-piano="${id}"]`);
        msgDiv.textContent = msg;
        msgDiv.style.display = "block";

        setTimeout(() => {
            msgDiv.style.display = "none";
        }, 2500)
    }
   
    
    // Vote for piano function
    document.querySelectorAll('.vote-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const pianoId = btn.dataset.piano;
            const token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    
            // Disable the button to prevent multiple clicks
            btn.disabled = true;
    
            try {
                console.log("Voting for " + pianoId);
    
                const response = await fetch(`/pianos/vote/${pianoId}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        content: 1
                    }),
                    headers: {
                        "X-CSRFToken": token,
                        "Content-Type": "application/json"
                    }
                });
    
                if (!response.ok) {
                    // Handle non-200 responses explicitly
                    const errorData = await response.json();
                    showVoteErrorMsg(errorData.error || "An error occurred", pianoId);
                    btn.disabled = false;
                    return;
                }
    
                const data = await response.json();
    
                if (data.msg) {
                    showVoteErrorMsg(data.msg, pianoId);
                } else {
                    // Update vote count on the page
                    document.querySelector(`.piano-votes[data-piano="${pianoId}"]`).textContent = `Number of votes: ${data.content}`;
                }
            } catch (error) {
                // Handle network or unexpected errors
                console.error("Error during voting:", error);
                showVoteErrorMsg("Failed to vote, please try again later", pianoId);
            } finally {
                // Re-enable the button after the process is complete
                btn.disabled = false;
            }
        });
    });
    

   // Delete piano
    const deleteLinks = document.querySelectorAll('.piano_delete_links');
    const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    // const pianoIndexUrl = "{% url 'index' %}";

    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const confirmation = confirm("Are you really sure you want to delete this wonderful piano?")

            if (confirmation) {
                // Get the URL from the dataset
                const url = this.dataset.url;
                // Find the parent card element
                const pianoCard = this.closest('.card.mb-3');

                fetch (url, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrf_token,
                        'Content-Type': 'application/json'
                    },
                }).then(response => {
                    if (response.ok) {
                        alert('Piano has been successfully deleted.');
                        // Remove the card element from the DOM
                        pianoCard.remove();
                    } else {
                        alert("Houston, we have a problem.")
                    }
                }).catch(err => console.error("Error", err))
            }
        })
    })

});
// End DOMContentLoaded

