// Elementos
const startBtn = document.getElementById("startBtn")
const homeInput = document.getElementById("homeInput")
// Funções

// Listeners
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