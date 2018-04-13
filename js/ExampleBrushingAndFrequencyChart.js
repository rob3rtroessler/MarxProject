var BrushData = d3.range(800).map(Math.random);

console.log(BrushData);

var BrushMargin = {top: 20, right: 70, bottom: 50, left: 70},
    BrushWidth = $("#ExampleBrushingAndFrequencyChart").width() - BrushMargin.left - BrushMargin.right,
    BrushHeight = $("#ExampleBrushingAndFrequencyChart").height() - BrushMargin.top - BrushMargin.bottom;

var svg = d3.select("#ExampleBrushingAndFrequencyChart").append("svg")
    .attr("width", BrushWidth + BrushMargin.left + BrushMargin.right)
    .attr("height",BrushHeight + BrushMargin.top + BrushMargin.bottom);

g = svg.append("g").attr("transform", "translate(" + BrushMargin.left + "," + BrushMargin.top + ")");

var x = d3.scaleLinear().range([0, BrushWidth]).domain([0,20]),
    y = d3.randomNormal(BrushHeight / 2, BrushHeight / 8);

var brush = d3.brushX()
    .extent([[0, 0], [BrushWidth, BrushHeight]])
    .on("start brush end", brushmoved);

g.append("g")
    .attr("class", "axis axis--x")
    .attr("transform", "translate(0," + BrushHeight + ")")
    .call(d3.axisBottom(x));

var circle = g.append("g")
    .attr("class", "circle")
    .selectAll("circle")
    .data(BrushData)
    .enter().append("circle")
    .attr("cx", function (d) { return d * BrushWidth})
    .attr("cy", BrushHeight/2)
    .attr("r", 1);

var gBrush = g.append("g")
    .attr("class", "brush")
    .call(brush);

var handle = gBrush.selectAll(".handle--custom")
    .data([{type: "w"}, {type: "e"}])
    .enter().append("path")
    .attr("class", "handle--custom")
    .attr("fill", "#666")
    .attr("fill-opacity", 0.8)
    .attr("stroke", "#000")
    .attr("stroke-width", 1.5)
    .attr("cursor", "ew-resize")
    .attr("d", d3.arc()
        .innerRadius(0)
        .outerRadius(BrushHeight / 2)
        .startAngle(0)
        .endAngle(function(d, i) { return i ? Math.PI : -Math.PI; }));

gBrush.call(brush.move, [0, 8].map(x));

function brushmoved() {
    var s = d3.event.selection;
    if (s == null) {
        handle.attr("display", "none");
        circle.classed("active", false);
    } else {
        var sx = s.map(x.invert);
        circle.classed("active", function(d) { return sx[0] <= d && d <= sx[1]; });
        handle.attr("display", null).attr("transform", function(d, i) { return "translate(" + s[i] + "," + BrushHeight / 2 + ")"; });
    }
}