let httpRequest;
document
    .getElementById("ajaxButton")
    .addEventListener("click", makeRequest);

function makeRequest() {
    httpRequest = new XMLHttpRequest();

    let all_inputs = document.getElementById("all_inputs");
    // formData is like dictionary in python ._. help me
    const formData = new FormData(all_inputs);

    httpRequest.onreadystatechange = getProtein;
    httpRequest.open("POST", "http://127.0.0.1:8000/dna_to_rna/");
    httpRequest.send(formData);
}

function getProtein() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            let json = JSON.parse(httpRequest.responseText)

            let rna_input = document.getElementById("rna_id")
            rna_input.value = json.rna

            let protein_input = document.getElementById("protein_id")
            protein_input.value = json.protein
        } else {
            console.log("There was a problem with the request.");
            alert("There was a problem with the request.");
        }
    }
}

let httpRequestPlot
document
    .getElementById("plotButton")
    .addEventListener("click", makeRequestImg);

function makeRequestImg() {
    httpRequestPlot = new XMLHttpRequest();

    let form_gc = document.getElementById("form_gc");
    const formData = new FormData(form_gc);

    httpRequestPlot.onreadystatechange = showImage;
    httpRequestPlot.open("POST", "http://127.0.0.1:8000/plot/");
    httpRequestPlot.send(formData);
}

function showImage() {
    if (httpRequestPlot.readyState === XMLHttpRequest.DONE) {
        if (httpRequestPlot.status === 200) {
            let json = JSON.parse(httpRequestPlot.responseText)

            let plot_img = document.getElementById("plot_img")
            plot_img.src = json.plot_img + "?t=" + new Date().getTime()
        } else {
            console.log("There was a problem with the request.");
            alert("There was a problem with the request.");
        }
    }
}