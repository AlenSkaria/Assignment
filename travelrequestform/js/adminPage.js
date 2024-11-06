let travelReq = {};
function displayRequests(filter = "all") {
  const requestsContainer = document.getElementById("requestsContainer");
  requestsContainer.innerHTML = "";

  const categoryTitle = document
    .getElementById("categoryTitle")
    .querySelector("h3");
  if (filter === "all") {
    categoryTitle.textContent = "All Requests";
  } else if (filter === "approved") {
    categoryTitle.textContent = "Approved Requests";
  } else if (filter === "pending") {
    categoryTitle.textContent = "Pending Requests";
  } else if (filter === "rejected") {
    categoryTitle.textContent = "Rejected Requests";
  } else if (filter === "onhold") {
    categoryTitle.textContent = "On Hold Requests";
  }

  const filteredRequests = travelReq.requests.filter(
    (req) => filter === "all" || req.status === filter
  );

  const priorityOrder = ["Critical", "Normal"];
  filteredRequests.sort((a, b) => {
    const pX = priorityOrder.indexOf(a.priority);
    const pY = priorityOrder.indexOf(b.priority);

    if (pX !== pY) {
      return pX - pY;
    }

    return a.requestId - b.requestId;
  });
  if (filteredRequests.length === 0) {
    const noRequestsMessage = document.createElement("h3");
    noRequestsMessage.textContent = "No Requests";
    requestsContainer.appendChild(noRequestsMessage); // Display the "No Requests" message
  } else {
    filteredRequests.forEach((req) => {
      const reqDiv = document.createElement("div");
      reqDiv.className = "request-item";
      reqDiv.innerHTML = `
    <div class='mainCollection'>
    <div class='pCollection'>
    <p><strong>Emp Name:</strong> ${req.empName}</p>
    <p><strong>Project:</strong> ${req.project}</p>
    <p><strong>Priority:</strong> ${req.priority}</p>
    <p><strong>Status:</strong> ${req.status}</p>
    </div>
    <div class='buttonCollection'>
    <button onclick="approveRequest(${req.requestId})">Approve</button>
    <button onclick="rejectRequest(${req.requestId})">Reject</button>
    <button onclick="putOnHold(${req.requestId})">Put on Hold</button>
    <button onclick="viewRequest(${req.requestId})">View Details</button>
    </div>
    </div>
    `;
      document.getElementById("requestsContainer").classList.remove("hide");
      document.getElementById("categoryTitle").classList.remove("hide");
      document.getElementById("display").classList.add("hide");
      requestsContainer.appendChild(reqDiv);
    });
  }
}

function approveRequest(requestId) {
  const req = travelReq.requests.find((r) => r.requestId === requestId);
  req.status = "approved";
  displayRequests("approved");
  localStorage.setItem("travelRequests", JSON.stringify(travelReq));
}

function rejectRequest(requestId) {
  const req = travelReq.requests.find((r) => r.requestId === requestId);
  req.status = "rejected";
  displayRequests("rejected");
  localStorage.setItem("travelRequests", JSON.stringify(travelReq));
}

function putOnHold(requestId) {
  const req = travelReq.requests.find((r) => r.requestId === requestId);
  req.status = "onhold";
  displayRequests("onhold");
  localStorage.setItem("travelRequests", JSON.stringify(travelReq));
}

//view requst user
function viewRequest(requestId) {
  const req = travelReq.requests.find((r) => r.requestId === requestId);
  const display = document.getElementById("display");

  display.innerHTML = `
        <h3 class="trTitle">Request Details</h3>
        <p><strong>Emp ID:</strong> ${req.empId}</p>
        <p><strong>Emp Name:</strong> ${req.empName}</p>
        <p><strong>Project:</strong> ${req.project}</p>
        <p><strong>Priority:</strong> ${req.priority}</p>
        <p><strong>Status:</strong> ${req.status}</p>
        <p><strong>Cause:</strong> ${req.cause}</p>
        <p><strong>Source:</strong> ${req.source}</p>
        <p><strong>Destination:</strong> ${req.destination}</p>
        <p><strong>From Date:</strong> ${req.fromDate}</p>
        <p><strong>To Date:</strong> ${req.toDate}</p>
        <p><strong>Total Days:</strong> ${req.noOfDays}</p>
        <p><strong>Mode of Travel:</strong> ${req.modeOfTravel}</p>
      `;
  document.getElementById("requestsContainer").classList.add("hide");
  document.getElementById("categoryTitle").classList.add("hide");
  display.classList.remove("hide");
}

// Handle tab switching
function setFilter(filter) {
  displayRequests(filter);
}
function logOut() {
  localStorage.removeItem("loggedUser");
  window.location.href = "../pages/login.html";
}

document.addEventListener("DOMContentLoaded", () => {
  travelReqLocalstg = localStorage.getItem("travelRequests");
  travelReqLocalstg = JSON.parse(travelReqLocalstg);
  console.log(travelReqLocalstg);
  loggedUser = localStorage.getItem("loggedUser");
  loggedUser = JSON.parse(loggedUser);
  loggedInUserId = loggedUser.userId;
  console.log(loggedUser);
  if (travelReqLocalstg) {
    travelReq = travelReqLocalstg;
    console.log(travelReq);
    displayRequests();
  }
  if (!loggedUser) {
    window.location.href = "../pages/login.html";
  }
});
