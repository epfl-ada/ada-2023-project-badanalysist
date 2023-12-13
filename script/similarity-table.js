var values = [
    ['English Brown Ale', 'American Brown Ale', 'Smoked Beer', 'American Pale Lager', 'American IPA'],
    ["12-17", "15-26", "1-100", "2-4", "6-12"],
    ["15-25", "25-45", "1-120", "5-19", "50-70"],
    ["4-5.5%", "4.2-6.3%", "0-15%", "4.1-5.1%", "6.3-7.5%"],
    ["Amber to Brown", "Deep Copper to Very Dark Brown", "Varies", "Straw to Gold", "Gold to Copper, Red/Brown"],
    ["Clear", "Clear", "Varies","Brilliant to Clear","Clear to Slight Haze"],
    ["Balance ranges from dry to sweet maltiness. Roast malt tones of toffee, nuts and caramel sometimes contribute to the flavor profile","Caramel, Chocolate, Toast", "Varies", "Grainy", "Biscuit, Bready, Caramel"],
    ["Hop aroma and flavor is very low. Hop bitterness is very low to low", "Hop aroma and flavor are low to medium. Hop bitterness is medium to high","Varies", "Low", "Hop aroma is high and hop flavor is strong both with floral qualities and citrus-like, piney, resinous or sulfur-like American-variety hop character. Hop bitterness is medium-high to very high"],
    ["Soft", "Varies", "Varies","Drying","Soft to Sticky"]]

var data = [{
type: 'table',
header: {
  values: [["<b>Beer Styles</b>"], ["<b>Color SRM</b>"],
               ["<b>Bitterness IBU</b>"], ["<b>Alcohol ABV</b>"], ["<b>Color</b>"],
            ["<b>Clarity</b>"], ["<b>Perceived Malt Aroma & Flavor</b>"], ["<b>Perceived Hop Aroma & Flavor</b>"],
            ["<b>Body</b>"]],
  align: "center",
  line: {width: 1, color: 'black'},
  fill: {color: "grey"},
  font: {family: "Arial", size: 12, color: "white"}
},
cells: {
  values: values,
  align: "center",
  line: {color: "black", width: 1},
  font: {family: "Arial", size: 11, color: ["black"]}
}
}]

var layout = {
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent'}

Plotly.newPlot('similarity-table', data, layout);
