const WebSocket = require('ws');

ws = new WebSocket("ws://localhost:6969");
getScore([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);

var lastReq = null
var newestReply = null

function getScore(arr) {   
    newestReply = null
    lastReq = arr
    
}

ws.addEventListener("open", (event) => {
    while(true) {
        if (lastReq != null) {
            ws.send(lastReq.toString());
            lastReq = null
        }
    }
});






