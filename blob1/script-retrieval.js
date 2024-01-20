// script.js

const SERVER_URL = 'http://127.0.0.1:5000';  // Update with your server's URL

async function fetchWebAddress(buttonName) {
    const response = await fetch(`${SERVER_URL}/api/fetch_web_address?button_name=${buttonName}`);

    if (!response.ok) {
        throw new Error(`Failed to fetch web address. Status: ${response.status}`);
    }

    const data = await response.json();
    return data.web_address;
}

// ... rest of the script


function fetchandupdate(buttonName) {
    // Call the Django API function to fetch the web address
    document.getElementById('resData').src = "./assets-retrieval/loading.gif";
    setTimeout(function() {
        webAddress  = fetchWebAddress(buttonName)
        .then(webAddress => {
            // Update the 'img' element's src attribute with the fetched web address
            document.getElementById('resData').src = webAddress;
        })
        .catch(error => {
            console.error("Error fetching web address:", error);

        });
    }, 3000);
}
function reset(){
    document.getElementById('resData').src = "./assets-retrieval/picture.jpg";
}
function home(){
    window.location.href = "./landingPage.html";
}
function push(){
    window.location.href = "./index.php";
}