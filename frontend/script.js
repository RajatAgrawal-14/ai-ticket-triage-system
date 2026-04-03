const API_URL = "http://127.0.0.1:8000";

// Submit ticket
async function submitTicket() {
  const message = document.getElementById("message").value;
  const resultDiv = document.getElementById("result");
  document.getElementById("message").value = "";

  // Loading state
  resultDiv.innerHTML = "Analyzing...";

  try {
    const response = await fetch(API_URL + "/tickets/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    });

    const data = await response.json();

    resultDiv.innerHTML = `
    <h3>Analysis Result</h3>
    Category: ${data.category} <br>
    Priority: ${data.priority} <br>
    Confidence: ${data.confidence}
`;

    loadTickets();
  } catch (error) {
    resultDiv.innerHTML = "Error occurred!";
  }
}

// Load previous tickets
async function loadTickets() {
  const response = await fetch(API_URL + "/tickets");
  const data = await response.json();

  const table = document.getElementById("ticketList");
  table.innerHTML = "";

  data.forEach((ticket) => {
    if (data.length === 0) {
      table.innerHTML = "<tr><td colspan='4'>No tickets yet</td></tr>";
      return;
    }
    const color =
    ticket.priority === "P0" ? "red" :
    ticket.priority === "P1" ? "orange" :
    ticket.priority === "P2" ? "blue" : "green";

const row = `
<tr>
    <td>${ticket.message}</td>
    <td>${ticket.category}</td>
    <td style="color:${color}">${ticket.priority}</td>
    <td>${ticket.confidence}</td>
</tr>
`;
    table.innerHTML += row;
  });
}

// Load tickets on page load
loadTickets();
