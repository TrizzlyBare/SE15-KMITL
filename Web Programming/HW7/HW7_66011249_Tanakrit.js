document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("jsonFileInput");
  const uploadButton = document.getElementById("uploadButton");

  uploadButton.addEventListener("click", function () {
    const file = fileInput.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        const data = JSON.parse(event.target.result);
        populateData(data);
      };
      reader.readAsText(file);
    } else {
      alert("Please select a JSON file first.");
    }
  });

  function populateData(data) {
    document.getElementById("student-name").value = data.student_name;
    document.getElementById("dob").value = data.date_of_birth;
    document.getElementById("admission-date").value = data.date_of_admission;
    document.getElementById("degree").value = data.degree;
    document.getElementById("major").value = data.major;
    document.getElementById("student-id").value = data.student_id;
    document.getElementById("graduation-date").value = data.date_of_graduation;

    const tbody = document.querySelector("table tbody");
    tbody.innerHTML = "";
    const years = Object.keys(data.credit);
    let totalCredits = 0;
    let totalGradePoints = 0;

    years.forEach((year) => {
      const semesters = Object.keys(data.credit[year]);
      semesters.forEach((semester) => {
        const semesterHeaderRow = document.createElement("tr");
        const semesterHeaderCell = document.createElement("td");
        semesterHeaderCell.colSpan = 3;
        semesterHeaderCell.textContent = `${semester}, ${year}`;
        semesterHeaderCell.classList.add("semester-header");
        semesterHeaderRow.appendChild(semesterHeaderCell);
        tbody.appendChild(semesterHeaderRow);

        let semesterCredits = 0;
        let semesterGradePoints = 0;

        const courses = Array.isArray(data.credit[year][semester])
          ? data.credit[year][semester]
          : [data.credit[year][semester]];
        courses.forEach((course) => {
          const row = document.createElement("tr");
          const courseTitleCell = document.createElement("td");
          const creditCell = document.createElement("td");
          const gradeCell = document.createElement("td");

          courseTitleCell.textContent = `${course.subject_id} - ${course.name}`;
          creditCell.textContent = course.credit;
          gradeCell.textContent = course.grade;

          row.appendChild(courseTitleCell);
          row.appendChild(creditCell);
          row.appendChild(gradeCell);

          tbody.appendChild(row);

          const gradePoint = getGradePoint(course.grade);
          semesterCredits += parseFloat(course.credit);
          semesterGradePoints += parseFloat(course.credit) * gradePoint;
          totalCredits += parseFloat(course.credit);
          totalGradePoints += parseFloat(course.credit) * gradePoint;
        });

        const gps = semesterGradePoints / semesterCredits;
        const gpa = totalGradePoints / totalCredits;

        const summaryRow = document.createElement("tr");
        const summaryCell = document.createElement("td");
        summaryCell.colSpan = 3;
        summaryCell.textContent = `GPS: ${gps.toFixed(2)}, GPA: ${gpa.toFixed(
          2
        )}`;
        summaryCell.classList.add("summary-row");
        summaryRow.appendChild(summaryCell);
        tbody.appendChild(summaryRow);
      });
    });
  }

  function getGradePoint(grade) {
    switch (grade) {
      case "A":
        return 4.0;
      case "B+":
        return 3.5;
      case "B":
        return 3.0;
      case "C+":
        return 2.5;
      case "C":
        return 2.0;
      case "D+":
        return 1.5;
      case "D":
        return 1.0;
      case "F":
        return 0.0;
      default:
        return 0.0;
    }
  }
});
