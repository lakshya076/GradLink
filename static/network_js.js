function applyMarkdownSyntax(syntax) {
    const markdownInput = document.getElementById("markdownInput");
    const selection = window.getSelection();
    const range = selection.getRangeAt(0);
    const selectedText = range.toString();
    const wrappedText = `${syntax}${selectedText}${syntax}`;

    range.deleteContents();
    range.insertNode(document.createTextNode(wrappedText));

    updatePreview();
}

function updatePreview() {
    const markdownContent = document.getElementById("markdownInput").innerText;
    const preview = document.getElementById("preview");
    preview.innerHTML = marked.parse(markdownContent);
}

// Event Listener
document.getElementById("markdownInput").addEventListener("input", updatePreview);

function createPost() {
    const markdownInput = document.getElementById("markdownInput");
    const markdownContent = markdownInput.innerText;

    if (markdownContent.trim() === "") {
        alert("Please enter some content for your post.");
        return;
    }

    const post = document.createElement("div");
    post.classList.add("post");

    post.innerHTML = `
      <div class="post-content">${marked.parse(markdownContent)}</div>
    `;

    // Add the new post to the top of the posts container
    const postsContainer = document.getElementById("postsContainer");
    postsContainer.prepend(post);

    // Clear the input and preview
    markdownInput.innerText = "";
    document.getElementById("preview").innerHTML = "";
}
