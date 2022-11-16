(function () {
    const month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for (let element of document.getElementsByClassName("datetime")) {
        let stamp = element.dataset.timestamp

        if (!stamp.endsWith("Z"))
            stamp += "Z"

        let date = new Date(stamp)

        let time = date.getHours().toString().padStart(2, "0") + ":" + date.getMinutes().toString().padStart(2, "0")

        element.innerHTML = month_names[date.getMonth()] + " " + date.getDate().toString().padStart(2, "0") + " " + date.getFullYear() + " at " + time
    }
})()
