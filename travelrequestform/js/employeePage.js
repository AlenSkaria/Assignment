let travelReq = {
  requests: [],
};
let trform = document.getElementById("trform");
let request = document.getElementById("request");
let display = document.getElementById("display");

function showPage(data) {
  console.log(data);
  if (data === "form") {
    trform.classList.remove("hide");
    request.classList.add("hide");
    display.classList.add("hide");
  } else if (data === "vr") {
    trform.classList.add("hide");
    request.classList.remove("hide");
    display.classList.add("hide");
    displayRequests();
  }
}

function submitForm(event) {
  event.preventDefault();
  let empId = document.getElementById("empid").value;
  let empName = document.getElementById("empName").value;
  let project = document.getElementById("project").value;
  let cause = document.getElementById("cause").value;
  let source = document.getElementById("source").value;
  let destination = document.getElementById("destination").value;
  let fromDate = document.getElementById("fromDate").value;
  let toDate = document.getElementById("toDate").value;
  let noOfDays = document.getElementById("totalDays").value;
  let modeOfTravel = document.getElementById("modeOfTravel").value;
  let priority = document.getElementById("priority").value;
  let formData = {
    requestId: Date.now(),
    requestor: loggedUser.userId,
    empId: empId,
    empName: empName,
    project: project,
    cause: cause,
    source: source,
    destination: destination,
    fromDate: fromDate,
    toDate: toDate,
    noOfDays: noOfDays,
    modeOfTravel: modeOfTravel,
    priority: priority,
    status: "pending",
  };
  console.log(formData);
  travelReq.requests.push(formData);
  localStorage.setItem("travelRequests", JSON.stringify(travelReq));
  document.querySelector("form").reset();
  alert("Request submitted successfully!");
}

function calculateDaysDifference() {
  const from = new Date(fromDate.value);
  const to = new Date(toDate.value);
  if (!isNaN(from) && !isNaN(to)) {
    const diff = to - from;
    const diffDays = Math.ceil(diff / (1000 * 60 * 60 * 24));
    document.getElementById("totalDays").value = diffDays >= 0 ? diffDays : "0";
  } else {
    totalDays.value = "";
  }
}
toDate.addEventListener("change", () => {
  calculateDaysDifference();
});

//view request section
function displayRequests() {
  const userRequests = travelReq.requests.filter(
    (req) => req.requestor === loggedInUserId
  );
  console.log(userRequests);
  const pendingRequests = document.getElementById("pendingRequests");
  const approvedRequests = document.getElementById("approvedRequests");
  const rejectedRequests = document.getElementById("rejectedRequests");
  const onHoldRequests = document.getElementById("onHoldRequests");

  pendingRequests.innerHTML = "";
  approvedRequests.innerHTML = "";
  rejectedRequests.innerHTML = "";
  onHoldRequests.innerHTML = "";

  userRequests.forEach((req) => {
    const reqDiv = document.createElement("div");
    reqDiv.className = "request-item";
    reqDiv.innerHTML = `
    <div class="displayHere">
    <div class="displayp">

          <p>Emp ID: ${req.empId}, Emp Name: ${req.empName}</p>
          <p>Project: ${req.project}, Priority: ${req.priority}</p>
          <p>Status: ${req.status}</p>
          </div>
          <div class="displayButton">
          ${
            req.status === "pending" || req.status === "onhold"
              ? `<button onclick="editRequest(${req.requestId})">Edit</button>`
              : ""
          }
          <button onclick="viewRequest(${req.requestId})">View</button>
        `;

    if (req.status === "pending") {
      pendingRequests.appendChild(reqDiv);
    } else if (req.status === "approved") {
      approvedRequests.appendChild(reqDiv);
    } else if (req.status === "rejected") {
      rejectedRequests.appendChild(reqDiv);
    } else if (req.status === "onhold") {
      onHoldRequests.appendChild(reqDiv);
    }
  });

  if (pendingRequests.innerHTML.trim() === "") {
    displayNoRequestsMessage(pendingRequests, "pending");
  }
  if (approvedRequests.innerHTML.trim() === "") {
    displayNoRequestsMessage(approvedRequests, "approved");
  }
  if (rejectedRequests.innerHTML.trim() === "") {
    displayNoRequestsMessage(rejectedRequests, "rejected");
  }
  if (onHoldRequests.innerHTML.trim() === "") {
    displayNoRequestsMessage(onHoldRequests, "on hold");
  }
  function displayNoRequestsMessage(container, categoryName) {
    const noDataMessage = document.createElement("p");
    noDataMessage.innerText = `No ${categoryName} requests found.`;
    container.appendChild(noDataMessage);
  }
}

function viewRequest(requestId) {
  const req = travelReq.requests.find((r) => r.requestId === requestId);

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
  trform.classList.add("hide");
  request.classList.add("hide");
  display.classList.remove("hide");
}

function editRequest(requestId) {
  showPage("form");
  const req = travelReq.requests.find((r) => r.requestId === requestId);
  document.getElementById("empid").value = req.empId;
  document.getElementById("empName").value = req.empName;
  document.getElementById("project").value = req.project;
  document.getElementById("cause").value = req.cause;
  document.getElementById("source").value = req.source;
  document.getElementById("destination").value = req.destination;
  document.getElementById("fromDate").value = req.fromDate;
  document.getElementById("toDate").value = req.toDate;
  document.getElementById("totalDays").value = req.noOfDays;
  document.getElementById("modeOfTravel").value = req.modeOfTravel;
  document.getElementById("priority").value = req.priority;

  document.querySelector("form").onsubmit = function (event) {
    event.preventDefault();
    submitEditedForm(event, requestId);
  };
}

//edited form
function submitEditedForm(event, requestId) {
  const updatedReq = {
    empId: document.getElementById("empid").value,
    empName: document.getElementById("empName").value,
    project: document.getElementById("project").value,
    cause: document.getElementById("cause").value,
    source: document.getElementById("source").value,
    destination: document.getElementById("destination").value,
    fromDate: document.getElementById("fromDate").value,
    toDate: document.getElementById("toDate").value,
    noOfDays: document.getElementById("totalDays").value,
    modeOfTravel: document.getElementById("modeOfTravel").value,
    priority: document.getElementById("priority").value,
  };
  const reqIndex = travelReq.requests.findIndex(
    (r) => r.requestId === requestId
  );
  if (reqIndex !== -1) {
    travelReq.requests[reqIndex] = {
      ...travelReq.requests[reqIndex],
      ...updatedReq,
    };
    localStorage.setItem("travelRequests", JSON.stringify(travelReq));
    console.log(travelReq.requests[reqIndex]);
    console.log(travelReq);
    alert("Request updated successfully!");
  } else {
    alert("Request not found!");
  }
  window.location.reload();
  displayRequests();
}

//view request section

function logOut() {
  localStorage.removeItem("loggedUser");
  window.location.href = "../pages/login.html";
}
let loggedUser = null;
let loggedInUserId = null;
let travelReqLocalstg = null;
document.addEventListener("DOMContentLoaded", () => {
  loggedUser = localStorage.getItem("loggedUser");
  loggedUser = JSON.parse(loggedUser);
  loggedInUserId = loggedUser.userId;
  console.log(loggedUser);
  travelReqLocalstg = localStorage.getItem("travelRequests");
  travelReqLocalstg = JSON.parse(travelReqLocalstg);
  console.log(travelReqLocalstg);
  if (travelReqLocalstg) {
    travelReq = travelReqLocalstg;
    console.log(travelReq);
  }
  if (!loggedUser) {
    window.location.href = "../pages/login.html";
  }
});
