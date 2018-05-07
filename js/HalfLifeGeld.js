
// Use the margin convention practice
var ExampleMargin = {top: 50, right: 70, bottom: 50, left: 70},
    width = $("#HalfLifeGeldChart").width() - ExampleMargin.left - ExampleMargin.right, // Use the window's width
    height = $("#HalfLifeGeldChart").height() - ExampleMargin.top - ExampleMargin.bottom; // Use the window's height





d3.csv("../data/hl/arbeit.csv", function(csv) {

    csv.forEach(function(d){
        d.x = +d.x;
        d.y = +d.y;
        });

    data = csv;



    var testMin = d3.min(data, function (d){return d.y});
    console.log(testMin);
    var testMax = d3.max(data, function (d){return d.y});
    console.log(testMax);

    var xScale = d3.scaleLinear()
        .domain([d3.min(data, function (d){return d.x}), d3.max(data, function (d){return d.x})]) // input
        .range([0, width]); // output

    var yScale = d3.scaleLog()
        .domain([d3.min(data, function (d){return d.y}),d3.max(data, function (d){return d.y})]) // input
        .range([height, 0]); // output


// d3's line generator
    var line = d3.line()
        .x(function(d) { return xScale(d.x); }) // set the x values for the line generator
        .y(function(d) { return yScale(d.y); }) // set the y values for the line generator
        .curve(d3.curveCardinal); // apply smoothing to the line




    console.log("showing the data");
    console.log(data);


    // Add the SVG to the page and employ
    var svg = d3.select("#HalfLifeGeldChart").append("svg")
        .attr("width", width + ExampleMargin.left + ExampleMargin.right)
        .attr("height", height + ExampleMargin.top + ExampleMargin.bottom)
        .append("g")
        .attr("transform", "translate(" + ExampleMargin.left + "," + ExampleMargin.top + ")");

    // Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

    // Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

    // Append the path, bind the data, and call the line generator
    svg.append("path")
        .datum(data) // Binds data to the line
        .attr("class", "line") // Assign a class for styling
        .attr("d", line) // Calls the line generator
        .attr("fill","none")
        .attr("stroke","#960510")
        .attr("stroke-width", 2);


    // Appends a circle for each datapoint
    svg.selectAll(".dot")
        .data(data)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot") // Assign a class for styling
        .attr("cx", function(d) { return xScale(d.x) })
        .attr("cy", function(d) { return yScale(d.y) })
        .attr("r", 0.1)
        .attr("fill","#960510");

});