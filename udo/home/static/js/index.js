const titleElement = document.getElementById('title');
const descriptionElement = document.getElementById('description');
const changeTextButton = document.getElementById('changeTextButton');

const initialTitle = "[ You can track your project for DevOps ]";
const initialDescription = "Stay in control of your development workflow with our powerful project tracking tool. Monitor progress, collaborate with your team, and streamline your DevOps pipeline—all in one place. Keep tasks organized, meet deadlines efficiently, and boost productivity with real-time updates and seamless integrations. Start managing your projects smarter today!";

const newTitle = "[ Optimize Your DevOps Workflow ]";
const newDescription = "Unlock the full potential of your projects with advanced tracking and automation. Gain insights, improve collaboration, and ensure seamless deployments with an intuitive, data-driven approach. Take your DevOps management to the next level today!";

function typeText(element, text, callback) {
    let index = 0;
    function type() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, 25);
        } else if (callback) {
            callback();
        }
    }
    type();
}

function writeInitialText() {
    typeText(titleElement, initialTitle, () => {
        typeText(descriptionElement, initialDescription);
    });
}

function changeText() {
    titleElement.textContent = ""; // Instantly clear title
    descriptionElement.textContent = ""; // Instantly clear description
    
    typeText(titleElement, newTitle, () => {
        typeText(descriptionElement, newDescription);
    });
}

window.onload = writeInitialText;
changeTextButton.onclick = changeText;
