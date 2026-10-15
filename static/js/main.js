document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".nav-links");

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            const open = nav.classList.toggle("open");
            toggle.setAttribute("aria-expanded", String(open));
        });
    }

    const dateInput = document.querySelector('input[name="travel_date"]');

    if (dateInput) {
        const today = new Date();
        const localDate = new Date(
            today.getTime() - today.getTimezoneOffset() * 60000
        ).toISOString().slice(0, 10);

        dateInput.min = localDate;
    }

    // Terms & Conditions error par scroll karega
    const notice = document.querySelector(".booking-card .notice");

    if (notice) {
        notice.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    }

});
