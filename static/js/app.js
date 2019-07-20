//API CALL TO AUTHOR SEARCH

// Select the submit button
function displayData(){ 

   var submit = d3.select("#submit");


   submit.on("click", function() {

  // Prevent the page from refreshing

   d3.event.preventDefault();

  // Select the input element and get the raw HTML node

   var inputElement = d3.select("#search-form-input");

  // Get the value property of the input element

   var author = inputElement.property("value");

// var filteredData = people.filter(person => person.bloodType === inputValue);
 
// Set the span tag in the h1 element to the text
  // that was entered in the form

  d3.select("h1>span").text(author);
//   d3.select(".summary").text(author);
//   d3.select(".summary")
//     .append("li").text(`Mean: ${mean}`)
//     .append("li").text(`Median: ${median}`)
//     .append("li").text(`Mode: ${mode}`)
//     .append("li").text(`Variance: ${variance}`)
//     .append("li").text(`Standard Deviation: ${standardDeviation}`);

   d3.json(`api/authorsearch/${author}`).then(function(data){
    console.log (data)  
});

// author='Amy Tan'
// d3.json(`api/authorsearch/${author}`).then(function(data){
//     console.log (data)
// })

})

}

displayData()