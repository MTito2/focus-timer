const btnHome = document.getElementById("btnHome")
const calendarInput = document.getElementById("calendarInput")

const dashboard1 = document.getElementById("dashboard1")
const dashboard2 = document.getElementById("dashboard2")
const dashboard3 = document.getElementById("dashboard3")
const dashboard4 = document.getElementById("dashboard4")

const overlay = document.createElement("div")
overlay.className = "indicators-overlay"
overlay.textContent = "Carregando..."

let registers = ""

function createElementRow(){
    const tableRow = document.createElement("div")
    tableRow.className = "indicators-table-row"
    
    for (let index = 0; index < 5; index++) {
        const tableContent = document.createElement("p")
        tableContent.className = "indicators-table-content"
        
        tableRow.appendChild(tableContent)
    }
    return tableRow
}

async function loadCardValues() {
    contentDash1 = await pywebview.api.get_total_hours()
    contentDash2 = await pywebview.api.get_biggest_session()
    contentDash3 = await pywebview.api.get_average_time()
    contentDash4 = await pywebview.api.get_proportion_focus()
    
    dashboard1.textContent = contentDash1
    dashboard2.textContent = contentDash2
    dashboard3.textContent = contentDash3
    dashboard4.textContent = contentDash4 + "%"
}

function removeCardsValues() {
    dashboard4.textContent = ""
    dashboard1.textContent = ""
    dashboard2.textContent = ""
    dashboard3.textContent = ""
}

function updateTable() {
    const table = document.getElementById("indicatorsTable")
    const tableContentContainer = document.createElement("div")
    
    tableContentContainer.className = "indicators-content-container"

    if (registers != ""){
        loadCardValues()
        
        // Limpa a tabela antes de adicionar os dados
        const tableRows = document.querySelectorAll(".indicators-table-row");
        tableRows.forEach(row => row.remove());     
        
        // Cria a tabela com os dados filtrados
        registers.forEach(element => {
            const tableRow = createElementRow()
            const tableContents = tableRow.children
            const contentDate = tableContents[0]
            const contentDesc = tableContents[1]
            const contentRawTime = tableContents[2]
            const contentIdleTime = tableContents[3]
            const contentActualDuration = tableContents[4]
            
            contentDate.textContent = element["date"]
            contentDesc.textContent = element["description"]
            contentRawTime.textContent = element["raw_time"]
            contentIdleTime.textContent = element["idle_time"]
            contentActualDuration.textContent = element["actual_duration"]
            
            tableContentContainer.appendChild(tableRow)
        });

        table.appendChild(tableContentContainer)
    }

    else {
        removeCardsValues()
        const tableRows = document.querySelectorAll(".indicators-table-row");
        tableRows.forEach(row => row.remove());   
    }
}

btnHome.addEventListener("click", () => {
    window.location.href='home.html';
})

calendarInput.addEventListener("blur", async() => {
    document.body.appendChild(overlay)

    const date = calendarInput.value
    await pywebview.api.set_period(date)
    registers = await pywebview.api.get_registers()
    updateTable()

    document.body.removeChild(overlay)
})

calendarInput.addEventListener("keydown", async(e) => {
    if (e.key === "Enter" ) {
        document.body.appendChild(overlay)

        const date = calendarInput.value
        await pywebview.api.set_period(date)
        registers = await pywebview.api.get_registers()
        updateTable()

        document.body.removeChild(overlay)
    }
})

updateTable()
