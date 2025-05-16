function populateCountries(){
    // list of 20 major countries in array
    var countries = ["Australia", "Brazil", "Canada", "China", "France", "Germany", "India", "Indonesia", "Italy", "Japan", "Mexico", "Nigeria", "Russia", "South Korea", "Spain", "Turkey", "Thailand", "United Kingdom", "United States", "Other"];

    // get the select element
    var countrySelect = document.getElementById("country");

    // loop through the array and create an option element for each country
    for (var i = 0; i < countries.length; i++) {
        var country = countries[i];
        var option = document.createElement("option");
        option.value = country;
        option.innerHTML = country;
        countrySelect.appendChild(option);
    }
}

function updateAgeValue(){
    const ageInput = document.getElementById("age");
    const ageValueSpan = document.getElementById("ageValue");
    ageValueSpan.textContent = ageInput.value;
}

function displayResume() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const street = document.getElementById("street").value;
    const city = document.getElementById("city").value;
    const country = document.getElementById("country").value;
    const university = document.getElementById("university").value;
    const degree = document.getElementById("degree").value;
    const graduationYear = document.getElementById("graduationYear").value;
    const ref = document.getElementById("ref").value;
    const profile = document.getElementById("profile").value;
    const skills = document.getElementById("skills").value;
    const experience = document.getElementById("experience").value;
    const colour = document.getElementById("favColour").value;

    // Display the details
    const resumeDetails = `
    Name:${name} 
    Age: ${age}
    Email:${email}
    Phone: ${phone}
    Address:${street}, ${city}, ${country}
    University: ${university}
    Degree: ${degree}
    Year of Graduation: ${graduationYear}
    Reference: ${ref}
    Profile: ${profile}
    Skills: ${skills}
    Experience: ${experience}
    Favorite Colour: ${colour}
`;


    // Show the details in an alert
    alert(resumeDetails);
}