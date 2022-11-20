let httpRequest;
document
  .getElementById("ajaxButton")
  .addEventListener("click", makeRequest);

function makeRequest() {
  httpRequest = new XMLHttpRequest();

  httpRequest.onreadystatechange = showImage;
  httpRequest.open("POST", "http://127.0.0.1:8000");
  httpRequest.send();
}

function showImage() {
  if (httpRequest.readyState === XMLHttpRequest.DONE) {
    if (httpRequest.status === 200) {
      alert(httpRequest.responseText);
    } else {
      console.log("There was a problem with the request.");
      alert("There was a problem with the request.");
    }
  }
}