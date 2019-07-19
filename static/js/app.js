//API CALL TO AUTHOR SEARCH

// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#example-form-input");

  // Get the value property of the input element
  var author = inputElement.property("value");

//   console.log(inputValue);

  // Set the span tag in the h1 element to the text
  // that was entered in the form
  d3.select("h1>span").text(author);

  d3.json(`api/authorsearch/${author}`).then(function(data){
        console.log (data)
});

// author='Amy Tan'
// d3.json(`api/authorsearch/${author}`).then(function(data){
//     console.log (data)
// })





// // Search filter function
// function myFilter() {
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById('myInput');
//     filter = input.value.toUpperCase();
//     ul = document.getElementById('myUL');
//     li = ul.getElementsByTagName('a')[0];
//     txtValue = a.textContent || a.innerText;
//     if(txtValue.toUpperCase().indexOf(filter) > -1) {
//         li[i].style.display = "";
//  }   else {
//         li[i].style.display = "none";
//  }
    
// }


// When the user clicks on <div>, open the popup
// function myPopup() {
//     var popup = document.getElementById("myPopup");
//     popup.classList.toggle("show");
//   }

//   function init() {
    // Grab a reference to the dropdown select element
//     var selector = d3.select("#selDataset");
  
//     // Use the list of country names to populate the select options
    // d3.json("/countries").then((countryNames) => {
    //   countryNames.forEach((country) => {
    //     selector
    //       .append("option")
    //       .text(country)
    //       .property("value", country);
    //   });
  
//       // Use the first country from the list to build the initial plots
//       const firstCountry = countryNames[0];
//       buildbarCharts(firstCountry);
//       buildlineCharts(firstCountry);
//       buildCharts(firstCountry);
//     });
//   }
  
//   function optionChanged(newCountry) {
//     // Fetch new data each time a new sample is selected
//     buildbarCharts(newCountry);
//     buildlineCharts(newCountry);
//     buildCharts(newCountry);
//   }
  
//   // Initialize the dashboard
//   init();
  