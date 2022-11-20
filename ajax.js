let httpRequest;
document
    .getElementById("ajaxButton")
    .addEventListener("click", makeRequest);

function makeRequest() {
    httpRequest = new XMLHttpRequest();

    let all_inputs = document.getElementById("all_inputs");
    // formData is like dictionary in python ._. help me
    const formData = new FormData(all_inputs);

    httpRequest.onreadystatechange = showImage;
    httpRequest.open("POST", "http://127.0.0.1:8000");
    httpRequest.send(formData);
}

function showImage() {
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