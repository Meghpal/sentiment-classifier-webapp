// https://css-tricks.com/how-to-recreate-the-ripple-effect-of-material-design-buttons/

createRipple = event => {
    const button = event.currentTarget;
    const diameter = Math.max(button.clientWidth, button.clientHeight);
    const radius = diameter / 2;
    const circle = document.createElement("span");
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.offsetX - radius}px`;
    circle.style.top = `${event.offsetY - radius}px`;
    circle.classList.add("ripple");
    console.log(event)
    const ripple = button.getElementsByClassName("ripple")[0];

    if (ripple) {
        ripple.remove();
    }
    button.appendChild(circle);
}

const buttons = document.getElementsByClassName("btn");
for (const button of buttons) {
    button.addEventListener("click", createRipple);
}