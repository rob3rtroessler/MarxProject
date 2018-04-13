
// Use the margin convention practice
var ExampleMargin = {top: 50, right: 70, bottom: 50, left: 70},
    width = $("#ExampleLineChart").width() - ExampleMargin.left - ExampleMargin.right, // Use the window's width
    height = $("#ExampleLineChart").height() - ExampleMargin.top - ExampleMargin.bottom; // Use the window's height

// The number of datapoints
var n = 21;

var xScale = d3.scaleLinear()
    .domain([0, n-1]) // input
    .range([0, width]); // output

var yScale = d3.scaleLinear()
    .domain([0, 1]) // input
    .range([height, 0]); // output

// d3's line generator
var line = d3.line()
    .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
    .y(function(d) { return yScale(d.y); }) // set the y values for the line generator
    .curve(d3.curveMonotoneX); // apply smoothing to the line

// An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
var dataset = d3.range(n).map(function(d) { return {"y": d3.randomUniform(1)() } });

console.log(dataset);

// Add the SVG to the page and employ
var svg = d3.select("#ExampleLineChart").append("svg")
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
    .datum(dataset) // Binds data to the line
    .attr("class", "line") // Assign a class for styling
    .attr("d", line) // Calls the line generator
    .attr("fill","none")
    .attr("stroke","#960510")
    .attr("stroke-width", 2);


// Appends a circle for each datapoint
svg.selectAll(".dot")
    .data(dataset)
    .enter().append("circle") // Uses the enter().append() method
    .attr("class", "dot") // Assign a class for styling
    .attr("cx", function(d, i) { return xScale(i) })
    .attr("cy", function(d) { return yScale(d.y) })
    .attr("r", 3)
    .attr("fill","#960510");