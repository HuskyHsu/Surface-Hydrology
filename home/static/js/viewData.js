var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    created: function () {
        var vm = this;
        axios.get('/data/all/')
            .then(function (response) {
                vm.siteBasic = response.data.success;
                vm.ajaxData_();
                vm.plotCalendarGraph(vm.calendar);
            })
            .catch(function (error) {
                console.log(error);
            });
    },
    data: {
        site: 'Capa2',
        item: '',
        startTime: '2015-04-01',
        endTime: '2015-06-10',
        siteBasic: [],
        timeSeries: "",
        checkedItems: [],
        calendar: [{
            "date": "2013-11-15",
            "num": 18.0
        }, {
            "date": "2013-11-16",
            "num": 48.0
        }, {
            "date": "2013-11-17",
            "num": 48.0
        }, {
            "date": "2013-11-18",
            "num": 48.0
        }, {
            "date": "2013-11-19",
            "num": 48.0
        }, {
            "date": "2013-11-20",
            "num": 48.0
        }, {
            "date": "2013-11-21",
            "num": 48.0
        }, {
            "date": "2013-11-22",
            "num": 48.0
        }, {
            "date": "2013-11-23",
            "num": 48.0
        }, {
            "date": "2013-11-24",
            "num": 48.0
        }, {
            "date": "2013-11-25",
            "num": 48.0
        }, {
            "date": "2013-11-26",
            "num": 48.0
        }, {
            "date": "2013-11-27",
            "num": 48.0
        }, {
            "date": "2013-11-28",
            "num": 48.0
        }, {
            "date": "2013-11-29",
            "num": 48.0
        }, {
            "date": "2013-11-30",
            "num": 48.0
        }, {
            "date": "2013-12-01",
            "num": 48.0
        }, {
            "date": "2013-12-02",
            "num": 48.0
        }, {
            "date": "2013-12-03",
            "num": 48.0
        }, {
            "date": "2013-12-04",
            "num": 48.0
        }, {
            "date": "2013-12-05",
            "num": 48.0
        }, {
            "date": "2013-12-06",
            "num": 48.0
        }, {
            "date": "2013-12-07",
            "num": 48.0
        }, {
            "date": "2013-12-08",
            "num": 48.0
        }, {
            "date": "2013-12-09",
            "num": 48.0
        }, {
            "date": "2013-12-10",
            "num": 48.0
        }, {
            "date": "2013-12-11",
            "num": 48.0
        }, {
            "date": "2013-12-12",
            "num": 27.0
        }, {
            "date": "2014-04-29",
            "num": 23.0
        }, {
            "date": "2014-04-30",
            "num": 48.0
        }, {
            "date": "2014-05-01",
            "num": 48.0
        }, {
            "date": "2014-05-02",
            "num": 48.0
        }, {
            "date": "2014-05-03",
            "num": 48.0
        }, {
            "date": "2014-05-04",
            "num": 48.0
        }, {
            "date": "2014-05-05",
            "num": 48.0
        }, {
            "date": "2014-05-06",
            "num": 48.0
        }, {
            "date": "2014-05-07",
            "num": 48.0
        }, {
            "date": "2014-05-08",
            "num": 48.0
        }, {
            "date": "2014-05-09",
            "num": 48.0
        }, {
            "date": "2014-05-10",
            "num": 48.0
        }, {
            "date": "2014-05-11",
            "num": 48.0
        }, {
            "date": "2014-05-12",
            "num": 48.0
        }, {
            "date": "2014-05-13",
            "num": 48.0
        }, {
            "date": "2014-05-14",
            "num": 48.0
        }, {
            "date": "2014-05-15",
            "num": 48.0
        }, {
            "date": "2014-05-16",
            "num": 48.0
        }, {
            "date": "2014-05-17",
            "num": 48.0
        }, {
            "date": "2014-05-18",
            "num": 48.0
        }, {
            "date": "2014-05-19",
            "num": 48.0
        }, {
            "date": "2014-05-20",
            "num": 48.0
        }, {
            "date": "2014-05-21",
            "num": 48.0
        }, {
            "date": "2014-05-22",
            "num": 48.0
        }, {
            "date": "2014-05-23",
            "num": 48.0
        }, {
            "date": "2014-05-24",
            "num": 48.0
        }, {
            "date": "2014-05-25",
            "num": 48.0
        }, {
            "date": "2014-05-26",
            "num": 48.0
        }, {
            "date": "2014-05-27",
            "num": 48.0
        }, {
            "date": "2014-05-28",
            "num": 48.0
        }, {
            "date": "2014-05-29",
            "num": 48.0
        }, {
            "date": "2014-05-30",
            "num": 24.0
        }, {
            "date": "2015-01-08",
            "num": 24.0
        }, {
            "date": "2015-01-09",
            "num": 48.0
        }, {
            "date": "2015-01-10",
            "num": 48.0
        }, {
            "date": "2015-01-11",
            "num": 48.0
        }, {
            "date": "2015-01-12",
            "num": 48.0
        }, {
            "date": "2015-01-13",
            "num": 48.0
        }, {
            "date": "2015-01-14",
            "num": 48.0
        }, {
            "date": "2015-01-15",
            "num": 48.0
        }, {
            "date": "2015-01-16",
            "num": 48.0
        }, {
            "date": "2015-01-17",
            "num": 48.0
        }, {
            "date": "2015-01-18",
            "num": 48.0
        }, {
            "date": "2015-01-19",
            "num": 48.0
        }, {
            "date": "2015-01-20",
            "num": 48.0
        }, {
            "date": "2015-01-21",
            "num": 48.0
        }, {
            "date": "2015-01-22",
            "num": 48.0
        }, {
            "date": "2015-01-23",
            "num": 48.0
        }, {
            "date": "2015-01-24",
            "num": 48.0
        }, {
            "date": "2015-01-25",
            "num": 48.0
        }, {
            "date": "2015-01-26",
            "num": 48.0
        }, {
            "date": "2015-01-27",
            "num": 48.0
        }, {
            "date": "2015-01-28",
            "num": 48.0
        }, {
            "date": "2015-01-29",
            "num": 48.0
        }, {
            "date": "2015-01-30",
            "num": 48.0
        }, {
            "date": "2015-01-31",
            "num": 48.0
        }, {
            "date": "2015-02-01",
            "num": 48.0
        }, {
            "date": "2015-02-02",
            "num": 48.0
        }, {
            "date": "2015-02-03",
            "num": 48.0
        }, {
            "date": "2015-02-04",
            "num": 48.0
        }, {
            "date": "2015-02-05",
            "num": 46.0
        }, {
            "date": "2015-02-06",
            "num": 48.0
        }, {
            "date": "2015-02-07",
            "num": 48.0
        }, {
            "date": "2015-02-08",
            "num": 48.0
        }, {
            "date": "2015-02-09",
            "num": 48.0
        }, {
            "date": "2015-02-10",
            "num": 48.0
        }, {
            "date": "2015-02-11",
            "num": 48.0
        }, {
            "date": "2015-02-12",
            "num": 48.0
        }, {
            "date": "2015-02-13",
            "num": 48.0
        }, {
            "date": "2015-02-14",
            "num": 48.0
        }, {
            "date": "2015-02-15",
            "num": 48.0
        }, {
            "date": "2015-02-16",
            "num": 48.0
        }, {
            "date": "2015-02-17",
            "num": 48.0
        }, {
            "date": "2015-02-18",
            "num": 48.0
        }, {
            "date": "2015-02-19",
            "num": 48.0
        }, {
            "date": "2015-02-20",
            "num": 48.0
        }, {
            "date": "2015-02-21",
            "num": 48.0
        }, {
            "date": "2015-02-22",
            "num": 48.0
        }, {
            "date": "2015-02-23",
            "num": 48.0
        }, {
            "date": "2015-02-24",
            "num": 48.0
        }, {
            "date": "2015-02-25",
            "num": 48.0
        }, {
            "date": "2015-02-26",
            "num": 24.0
        }, {
            "date": "2015-05-10",
            "num": 38.0
        }, {
            "date": "2015-05-11",
            "num": 48.0
        }, {
            "date": "2015-05-12",
            "num": 48.0
        }, {
            "date": "2015-05-13",
            "num": 48.0
        }, {
            "date": "2015-05-14",
            "num": 48.0
        }, {
            "date": "2015-05-15",
            "num": 48.0
        }, {
            "date": "2015-05-16",
            "num": 48.0
        }, {
            "date": "2015-05-17",
            "num": 48.0
        }, {
            "date": "2015-05-18",
            "num": 48.0
        }, {
            "date": "2015-05-19",
            "num": 48.0
        }, {
            "date": "2015-05-20",
            "num": 48.0
        }, {
            "date": "2015-05-21",
            "num": 48.0
        }, {
            "date": "2015-05-22",
            "num": 48.0
        }, {
            "date": "2015-05-23",
            "num": 48.0
        }, {
            "date": "2015-05-24",
            "num": 48.0
        }, {
            "date": "2015-05-25",
            "num": 48.0
        }, {
            "date": "2015-05-26",
            "num": 48.0
        }, {
            "date": "2015-05-27",
            "num": 48.0
        }, {
            "date": "2015-05-28",
            "num": 48.0
        }, {
            "date": "2015-05-29",
            "num": 48.0
        }, {
            "date": "2015-05-30",
            "num": 48.0
        }, {
            "date": "2015-05-31",
            "num": 48.0
        }, {
            "date": "2015-06-01",
            "num": 48.0
        }, {
            "date": "2015-06-02",
            "num": 48.0
        }, {
            "date": "2015-06-03",
            "num": 48.0
        }, {
            "date": "2015-06-04",
            "num": 48.0
        }, {
            "date": "2015-06-05",
            "num": 48.0
        }, {
            "date": "2015-06-06",
            "num": 48.0
        }, {
            "date": "2015-06-07",
            "num": 48.0
        }, {
            "date": "2015-06-08",
            "num": 48.0
        }, {
            "date": "2015-06-09",
            "num": 48.0
        }, {
            "date": "2015-06-10",
            "num": 48.0
        }, {
            "date": "2015-06-11",
            "num": 48.0
        }, {
            "date": "2015-06-12",
            "num": 48.0
        }, {
            "date": "2015-06-13",
            "num": 48.0
        }, {
            "date": "2015-06-14",
            "num": 48.0
        }, {
            "date": "2015-06-15",
            "num": 48.0
        }, {
            "date": "2015-06-16",
            "num": 48.0
        }, {
            "date": "2015-06-17",
            "num": 48.0
        }, {
            "date": "2015-06-18",
            "num": 48.0
        }, {
            "date": "2015-06-19",
            "num": 48.0
        }, {
            "date": "2015-06-20",
            "num": 48.0
        }, {
            "date": "2015-06-21",
            "num": 48.0
        }, {
            "date": "2015-06-22",
            "num": 48.0
        }, {
            "date": "2015-06-23",
            "num": 48.0
        }, {
            "date": "2015-06-24",
            "num": 48.0
        }, {
            "date": "2015-06-25",
            "num": 48.0
        }, {
            "date": "2015-06-26",
            "num": 48.0
        }, {
            "date": "2015-06-27",
            "num": 48.0
        }, {
            "date": "2015-06-28",
            "num": 48.0
        }, {
            "date": "2015-06-29",
            "num": 48.0
        }, {
            "date": "2015-06-30",
            "num": 48.0
        }, {
            "date": "2015-07-01",
            "num": 48.0
        }, {
            "date": "2015-07-02",
            "num": 48.0
        }, {
            "date": "2015-07-03",
            "num": 48.0
        }, {
            "date": "2015-07-04",
            "num": 48.0
        }, {
            "date": "2015-07-05",
            "num": 48.0
        }, {
            "date": "2015-07-06",
            "num": 48.0
        }, {
            "date": "2015-07-07",
            "num": 48.0
        }, {
            "date": "2015-07-08",
            "num": 48.0
        }, {
            "date": "2015-07-09",
            "num": 48.0
        }, {
            "date": "2015-07-10",
            "num": 48.0
        }, {
            "date": "2015-07-11",
            "num": 48.0
        }, {
            "date": "2015-07-12",
            "num": 48.0
        }, {
            "date": "2015-07-13",
            "num": 48.0
        }, {
            "date": "2015-07-14",
            "num": 48.0
        }, {
            "date": "2015-07-15",
            "num": 48.0
        }, {
            "date": "2015-07-16",
            "num": 48.0
        }, {
            "date": "2015-07-17",
            "num": 48.0
        }, {
            "date": "2015-07-18",
            "num": 48.0
        }, {
            "date": "2015-07-19",
            "num": 48.0
        }, {
            "date": "2015-07-20",
            "num": 48.0
        }, {
            "date": "2015-07-21",
            "num": 48.0
        }, {
            "date": "2015-07-22",
            "num": 48.0
        }, {
            "date": "2015-07-23",
            "num": 48.0
        }, {
            "date": "2015-07-24",
            "num": 48.0
        }, {
            "date": "2015-07-25",
            "num": 48.0
        }, {
            "date": "2015-07-26",
            "num": 48.0
        }, {
            "date": "2015-07-27",
            "num": 48.0
        }, {
            "date": "2015-07-28",
            "num": 48.0
        }, {
            "date": "2015-07-29",
            "num": 48.0
        }, {
            "date": "2015-07-30",
            "num": 48.0
        }, {
            "date": "2015-07-31",
            "num": 48.0
        }, {
            "date": "2015-08-01",
            "num": 48.0
        }, {
            "date": "2015-08-02",
            "num": 48.0
        }, {
            "date": "2015-08-03",
            "num": 48.0
        }, {
            "date": "2015-08-04",
            "num": 48.0
        }, {
            "date": "2015-08-05",
            "num": 48.0
        }, {
            "date": "2015-08-06",
            "num": 48.0
        }, {
            "date": "2015-08-07",
            "num": 48.0
        }, {
            "date": "2015-08-08",
            "num": 48.0
        }, {
            "date": "2015-08-09",
            "num": 48.0
        }, {
            "date": "2015-08-10",
            "num": 48.0
        }, {
            "date": "2015-08-11",
            "num": 48.0
        }, {
            "date": "2015-08-12",
            "num": 48.0
        }, {
            "date": "2015-08-13",
            "num": 48.0
        }, {
            "date": "2015-08-14",
            "num": 48.0
        }, {
            "date": "2015-08-15",
            "num": 48.0
        }, {
            "date": "2015-08-16",
            "num": 48.0
        }, {
            "date": "2015-08-17",
            "num": 48.0
        }, {
            "date": "2015-08-18",
            "num": 48.0
        }, {
            "date": "2015-08-19",
            "num": 48.0
        }, {
            "date": "2015-08-20",
            "num": 48.0
        }, {
            "date": "2015-08-21",
            "num": 48.0
        }, {
            "date": "2015-08-22",
            "num": 48.0
        }, {
            "date": "2015-08-23",
            "num": 48.0
        }, {
            "date": "2015-08-24",
            "num": 48.0
        }, {
            "date": "2015-08-25",
            "num": 48.0
        }, {
            "date": "2015-08-26",
            "num": 48.0
        }, {
            "date": "2015-08-27",
            "num": 48.0
        }, {
            "date": "2015-08-28",
            "num": 48.0
        }, {
            "date": "2015-08-29",
            "num": 48.0
        }, {
            "date": "2015-08-30",
            "num": 48.0
        }, {
            "date": "2015-08-31",
            "num": 48.0
        }, {
            "date": "2015-09-01",
            "num": 48.0
        }, {
            "date": "2015-09-02",
            "num": 48.0
        }, {
            "date": "2015-09-03",
            "num": 48.0
        }, {
            "date": "2015-09-04",
            "num": 48.0
        }, {
            "date": "2015-09-05",
            "num": 48.0
        }, {
            "date": "2015-09-06",
            "num": 48.0
        }, {
            "date": "2015-09-07",
            "num": 48.0
        }, {
            "date": "2015-09-08",
            "num": 48.0
        }, {
            "date": "2015-09-09",
            "num": 48.0
        }, {
            "date": "2015-09-10",
            "num": 48.0
        }, {
            "date": "2015-09-11",
            "num": 48.0
        }, {
            "date": "2015-09-12",
            "num": 48.0
        }, {
            "date": "2015-09-13",
            "num": 48.0
        }, {
            "date": "2015-09-14",
            "num": 48.0
        }, {
            "date": "2015-09-15",
            "num": 48.0
        }, {
            "date": "2015-09-16",
            "num": 48.0
        }, {
            "date": "2015-09-17",
            "num": 48.0
        }, {
            "date": "2015-09-18",
            "num": 48.0
        }, {
            "date": "2015-09-19",
            "num": 48.0
        }, {
            "date": "2015-09-20",
            "num": 48.0
        }, {
            "date": "2015-09-21",
            "num": 48.0
        }, {
            "date": "2015-09-22",
            "num": 48.0
        }, {
            "date": "2015-09-23",
            "num": 48.0
        }, {
            "date": "2015-09-24",
            "num": 48.0
        }, {
            "date": "2015-09-25",
            "num": 48.0
        }, {
            "date": "2015-09-26",
            "num": 48.0
        }, {
            "date": "2015-09-27",
            "num": 48.0
        }, {
            "date": "2015-09-28",
            "num": 48.0
        }, {
            "date": "2015-09-29",
            "num": 48.0
        }, {
            "date": "2015-09-30",
            "num": 48.0
        }, {
            "date": "2015-10-01",
            "num": 48.0
        }, {
            "date": "2015-10-02",
            "num": 48.0
        }, {
            "date": "2015-10-03",
            "num": 48.0
        }, {
            "date": "2015-10-04",
            "num": 48.0
        }, {
            "date": "2015-10-05",
            "num": 48.0
        }, {
            "date": "2015-10-06",
            "num": 48.0
        }, {
            "date": "2015-10-07",
            "num": 48.0
        }, {
            "date": "2015-10-08",
            "num": 48.0
        }, {
            "date": "2015-10-09",
            "num": 48.0
        }, {
            "date": "2015-10-10",
            "num": 48.0
        }, {
            "date": "2015-10-11",
            "num": 48.0
        }, {
            "date": "2015-10-12",
            "num": 48.0
        }, {
            "date": "2015-10-13",
            "num": 48.0
        }, {
            "date": "2015-10-14",
            "num": 36.0
        }, {
            "date": "2015-10-15",
            "num": 45.0
        }, {
            "date": "2015-10-16",
            "num": 48.0
        }, {
            "date": "2015-10-17",
            "num": 48.0
        }, {
            "date": "2015-10-18",
            "num": 48.0
        }, {
            "date": "2015-10-19",
            "num": 48.0
        }, {
            "date": "2015-10-20",
            "num": 25.0
        }]
    },
    computed: {
        siteField: function () {
            var site = this.site;
            var field = this.siteBasic.filter(function (item) {
                return item.name === site;
            }).map(function (item) {
                return item.field
            })
            this.item = field.length > 0 ? field[0][0] : ''
            return field.length > 0 ? field[0] : ''
        },
    },
    methods: {
        plotLine: function (item, data) {

            var margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 50
            };
            var width = 960 - margin.left - margin.right;
            var height = 500 - margin.top - margin.bottom;

            var svg = d3.select("#timeSeries")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom);

            svg.selectAll("g").remove();
            var g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            var parseTime = d3.timeParse("%Y-%m-%dT%H:%M:%S");
            // 2015-05-10T05:30:00
            var x = d3.scaleTime()
                .rangeRound([0, width]);

            var y = d3.scaleLinear()
                .rangeRound([height, 0]);

            var line = d3.line()
                .x(function (d) {
                    return x(parseTime(d.TIMESTAMP));
                })
                .y(function (d) {
                    return y(d[item]);
                });

            x.domain(d3.extent(data, function (d) {
                return parseTime(d.TIMESTAMP);
            }));
            y.domain(d3.extent(data, function (d) {
                return d[item];
            }));

            g.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            g.append("g")
                .call(d3.axisLeft(y))
                .append("text")
                .attr("fill", "#000")
                .attr("transform", "rotate(-90)")
                .attr("y", 6)
                .attr("dy", "0.71em")
                .attr("text-anchor", "end")
                .text(item);

            g.append("path")
                .datum(data)
                .attr("fill", "none")
                .attr("stroke", "steelblue")
                .attr("stroke-linejoin", "round")
                .attr("stroke-linecap", "round")
                .attr("stroke-width", 1.5)
                .attr("d", line);

        },
        plotCalendarGraph: function (datum) {
            var width = 960;
            var height = 136;
            var cellSize = 17;

            var color = d3.scaleQuantize()
                .domain([0, 48])
                .range(['#eee', '#c6e48b', '#7bc96f']);

            var svg = d3.select("#calendar-graph")
                .selectAll("svg")
                .data(d3.range(2013, 2016))
                .enter().append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g")
                .attr("transform", "translate(" + ((width - cellSize * 53) / 2) + "," + (height - cellSize * 7 - 1) + ")");

            svg.append("text")
                .attr("transform", "translate(-6," + cellSize * 3.5 + ")rotate(-90)")
                .attr("font-family", "sans-serif")
                .attr("font-size", 10)
                .attr("text-anchor", "middle")
                .text(function (d) {
                    return d;
                });

            var rect = svg.append("g")
                .attr("fill", "none")
                .attr("stroke", "#ccc")
                .selectAll("rect")
                .data(function (d) {
                    return d3.timeDays(new Date(d, 0, 1), new Date(d + 1, 0, 1));
                })
                .enter().append("rect")
                .attr("width", cellSize)
                .attr("height", cellSize)
                .attr("x", function (d) {
                    return d3.timeWeek.count(d3.timeYear(d), d) * cellSize;
                })
                .attr("y", function (d) {
                    return d.getDay() * cellSize;
                })
                .datum(d3.timeFormat("%Y-%m-%d"));

            svg.append("g")
                .attr("fill", "none")
                .attr("stroke", "#000")
                .selectAll("path")
                .data(function (d) {
                    return d3.timeMonths(new Date(d, 0, 1), new Date(d + 1, 0, 1));
                })
                .enter().append("path")
                .attr("d", pathMonth);

            var data = d3.nest()
                .key(function (d) { return d.date; })
                .rollup(function (d) { return d[0].num })
                .object(datum);

            rect.filter(function (d) {
                    return d in data;
                })
                .attr("fill", function (d) {
                    return color(data[d]);
                });

            function pathMonth(t0) {
                var t1 = new Date(t0.getFullYear(), t0.getMonth() + 1, 0),
                    d0 = t0.getDay(),
                    w0 = d3.timeWeek.count(d3.timeYear(t0), t0),
                    d1 = t1.getDay(),
                    w1 = d3.timeWeek.count(d3.timeYear(t1), t1);
                return "M" + (w0 + 1) * cellSize + "," + d0 * cellSize +
                    "H" + w0 * cellSize + "V" + 7 * cellSize +
                    "H" + w1 * cellSize + "V" + (d1 + 1) * cellSize +
                    "H" + (w1 + 1) * cellSize + "V" + 0 +
                    "H" + (w0 + 1) * cellSize + "Z";
            }
        },
        ajaxData: _.debounce(
            function () {

                var vm = this;
                axios.get(`/data/${vm.site}/${vm.item}/${vm.startTime}/${vm.endTime}/`)
                    .then(function (response) {
                        vm.timeSeries = response.data.data;
                    })
                    .catch(function (error) {
                        vm.timeSeries = []
                    })
            },
            500
        ),
        ajaxData_: function () {
            var vm = this;
            axios.get(`/data/${vm.site}/${vm.item}/${vm.startTime}/${vm.endTime}/`)
                .then(function (response) {
                    vm.timeSeries = response.data.data;
                })
                .catch(function (error) {
                    vm.timeSeries = []
                })
        }
    },
    watch: {
        startTime: function () {
            this.ajaxData()
        },
        endTime: function () {
            this.ajaxData()
        },
        item: function () {
            this.ajaxData_()
        },
        timeSeries: function () {
            this.plotLine(this.item, this.timeSeries)
        },
        site: function () {
            this.checkedItems = []
        }
    }
})