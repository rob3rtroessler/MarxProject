
/*
    FIRST VISUALIZATION: EASY BAR CHART
*/

function switchfunc() {
    document.getElementById("switch").innerHTML= "updated";
}



// define margins for SVG drawing area
var marginBarchart = {top: 40, right: 40, bottom: 40, left: 40};
var widthBarchart = $("#MarxChart").width() - marginBarchart.left - marginBarchart.right,
    heightBarchart = $("#MarxChart").height() - marginBarchart.top - marginBarchart.bottom;

// implement SVG drawing area
var svgBarchart = d3.select("#MarxChart").append("svg")
    .attr("width", widthBarchart + marginBarchart.left + marginBarchart.right)
    .attr("height", heightBarchart + marginBarchart.top + marginBarchart.bottom)
    .append("g")
    .attr("transform", "translate(" + marginBarchart.left + "," + marginBarchart.top + ")");


/*
    TODO!!
*/



// set the ranges
var x = d3.scaleBand()
    .range([0, widthBarchart])
    .padding(0.1);
var y = d3.scaleLinear()
    .range([heightBarchart, 0]);


// get the data
d3.csv("../data/words.csv", function(error, data) {
    if (error) {throw error;}


    // format the data
    data.forEach(function(d) {
        d.frequency = +d.frequency;
    });

    // Scale the range of the data in the domains
    x.domain(data.map(function(d) { return d.word; }));
    y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

    // append the rectangles for the bar chart
    svgBarchart.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.word); })
        .attr("width", x.bandwidth())
        .attr("y", function(d) { return y(d.frequency); })
        .attr("height", function(d) { return heightBarchart - y(d.frequency); });

    // add the x Axis
    svgBarchart.append("g")
        .attr("transform", "translate(0," + heightBarchart + ")")
        .call(d3.axisBottom(x));

    // add the y Axis
    svgBarchart.append("g")
        .call(d3.axisLeft(y));

});


