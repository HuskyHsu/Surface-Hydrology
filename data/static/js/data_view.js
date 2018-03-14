var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    created: function () {
        var vm = this;
        axios.get('/api/get/lhc/all')
            .then(function (response) {
                vm.siteBasic = response.data.success;
                vm.ajaxData_();
                vm.ajaxCalendar(vm.siteBasic[0].name ,vm.siteBasic[0].field[0]);
                // vm.plotCalendarGraph(vm.calendar);
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
        calendar: []
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
            var width = d3.select("#timeSeries").node().parentNode.offsetWidth - margin.left - margin.right;
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

            d3.select("#calendar-graph").selectAll("svg").remove();

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
                axios.get(`/api/get/lhc/${vm.site}/${vm.item}/${vm.startTime}/${vm.endTime}`)
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
            axios.get(`/api/get/lhc/${vm.site}/${vm.item}/${vm.startTime}/${vm.endTime}`)
                .then(function (response) {
                    vm.timeSeries = response.data.data;
                })
                .catch(function (error) {
                    vm.timeSeries = []
                })
        },
        ajaxCalendar: function (capa, item){
            var vm = this;
            axios.get(`/api/get/lhc/${capa}/calendarGraph/${item}`)
            .then(function (response) {
                vm.calendar = response.data.success;
                vm.plotCalendarGraph(vm.calendar)
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    },
    watch: {
        startTime: function () {
            this.ajaxData();
        },
        endTime: function () {
            this.ajaxData();
        },
        item: function () {
            this.ajaxData_();
            this.ajaxCalendar(this.site ,this.item);
        },
        timeSeries: function () {
            this.plotLine(this.item, this.timeSeries);
        },
        site: function () {
            this.checkedItems = [];
            this.ajaxCalendar(this.site ,this.item);
        }
    }
})