//API CALL TO AUTHOR SEARCH

// Select the submit button

   var submit = d3.select("#submit");


   submit.on("click", function() {

  // Prevent the page from refreshing

   d3.event.preventDefault();

  // Select the input element and get the raw HTML node

   var inputElement = d3.select("#search-form-input");

  // Get the value property of the input element

   var author = inputElement.property("value");
   console.log(author)

// var filteredData = people.filter(person => person.bloodType === inputValue);
 
// Set the span tag in the h1 element to the text
  // that was entered in the form

   d3.json(`api/authorsearch/${author}`).then(function(data){

    birthplace=data['birthplace']
    gender=data['gender']
    rating=data['rating']
    books=data['books']

    d3.select(".summary").text(author)
      .append("li").text(birthplace)
      .append("li").text(gender)
    
      tbody = d3.select("tbody")
        tbody.text("")
        books.forEach(function(title){
            new_tr = tbody.append("tr")
            new_td = new_tr.append("td").text(title)


        console.log (data)
});



})
});