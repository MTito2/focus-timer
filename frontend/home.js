// Elementos
const startBtn = document.getElementById("startBtn")
const homeInput = document.getElementById("homeInput")
const settingsBtn = document.getElementById("settingsBtn")
const homeSettingsContainer = document.getElementById("homeSettingsContainer")
const homeSettingsItems = document.querySelectorAll(".home-settings-item")
const homeIdleContainer = document.getElementById("homeIdleContainer")
const homeDisplayTime = document.getElementById("homeDisplayTime")
const btnLess = document.getElementById("btnLess")
const btnMore = document.getElementById("btnMore")
const btnSave = document.getElementById("btnSave")
let idleTime

if ("idleTime" in localStorage){
    idleTime = localStorage.getItem("idleTime")
}

else {
    idleTime = 1
}

// Funções
function showDisplayIdleTime(){
    homeDisplayTime.textContent = `${idleTime} min`
}

function saveIdleTime(){
    localStorage.setItem("idleTime", idleTime)
}

// Listeners
settingsBtn.addEventListener("click", () =>{
    homeSettingsContainer.classList.add("home-settings-container-show")
    
    document.addEventListener("keydown", (event) =>{
    if (event.key === "Escape"){
        homeSettingsContainer.classList.remove("home-settings-container-show")
        homeIdleContainer.classList.remove("home-idle-container-show")
        }
    })
})

document.addEventListener("click", (e) => {
    if (settingsBtn.contains(e.target)) return
    
    if (homeSettingsContainer.contains(e.target)) return

    if (homeIdleContainer.contains(e.target)) return

    homeSettingsContainer.classList.remove("home-settings-container-show");
    homeIdleContainer.classList.remove("home-idle-container-show")
})

homeSettingsItems.forEach((item) => {
    item.addEventListener("click", () => {
        if (item.textContent === "Indicadores") {
            window.location.href='indicators.html';
        } 

        else if (item.textContent === "Tempo de ociosidade") {
            homeSettingsContainer.classList.remove("home-settings-container-show");
            homeIdleContainer.classList.add("home-idle-container-show");
        }
    });
});

btnLess.addEventListener("click", () => {
    if (idleTime > 1) {
        idleTime--
        showDisplayIdleTime()
    }
})

btnMore.addEventListener("click", () => {
    idleTime++
    showDisplayIdleTime()
})

btnSave.addEventListener("click", () => {
    saveIdleTime()
    showDisplayIdleTime()
    homeIdleContainer.classList.remove("home-idle-container-show")
    pywebview.api.setter_idle_limit(idleTime)
})

document.addEventListener("click", (event) =>{
    if (!homeSettingsContainer.contains(event.target) && !settingsBtn.contains(event.target) && btnLess.contains(event.target) && btnMore.contains(event.target)) {
        homeSettingsContainer.classList.remove("home-settings-container-show")
        homeIdleContainer.classList.remove("home-idle-container-show")
    }
})

startBtn.addEventListener("click", () =>{
    pywebview.api.start()
    const subject = homeInput.value

    localStorage.setItem("studySubject", subject)
})

document.addEventListener("keydown", (event) =>{
    if (event.key === "Enter"){
        startBtn.click()
    }
})

// Execuções
showDisplayIdleTime()