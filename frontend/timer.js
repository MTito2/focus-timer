// Elementos
const timerDisplay = document.getElementById("timerDisplay")
const studyTitle = document.getElementById("studyTitle")
const finishBtn = document.getElementById("finishBtn")
const subject = localStorage.getItem("studySubject")

// Estado
studyTitle.textContent = `Estudo: ${subject}`

// Funções
function stopwatchDisplay(){
    pywebview.api.elapsed().then(function(value){
        timerDisplay.textContent = value;
    });
}

// Listeners
finishBtn.addEventListener("click", () =>{
    pywebview.api.receive_study_title(subject)
    pywebview.api.calculate_final_time()
    pywebview.api.stop()
    pywebview.api.export_report()

})

document.addEventListener("keydown", (event) =>{
    if (event.key === " "){
        finishBtn.click()
    }
})

// Execuções
setInterval(stopwatchDisplay, 300)
