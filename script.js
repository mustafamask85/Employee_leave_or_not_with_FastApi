document.getElementById("predictionForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = {};

  formData.forEach((value, key) => {
    data[key] = isNaN(value) ? value : Number(value);
  });

  try {
    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    const resultBox = document.getElementById("result");
    resultBox.innerHTML = `
      <span class="${result.prediction === 1 ? 'yes' : 'no'}">
        ${result.prediction === 1 ? '⚠️ Employee Likely to Leave' : '✅ Employee Likely to Stay'}
      </span>
    `;
  } catch (err) {
    document.getElementById("result").innerHTML = "❌ Error connecting to server.";
    console.error("Error:", err);
  }
});
