var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        site: 'Capa2',
        item: '',
        startTime: '2015-04-01',
        endTime: '2015-06-10',
        siteBasic: [],
        timeSeries: []
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
        gettimeSeries: function () {
            var site = this.site;
            var item = this.item;
            var startTime = this.startTime;
            var endTime = this.endTime;

            var vm = this;

            if (item != '') {
                axios.get(`/data/${site}/${item}/${startTime}/${endTime}`)
                    .then(function (response) {
                        if (response.data.check) {
                            // console.log(response);
                            // vm.timeSeries = response.data.data;
                            var data = response.data.data;

                            var svg = d3.select("svg");
                            var margin = { top: 20, right: 20, bottom: 30, left: 50 };
                            var width = +svg.attr("width") - margin.left - margin.right;
                            var height = +svg.attr("height") - margin.top - margin.bottom;
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
                                .call(d3.axisBottom(x))
                                .select(".domain")
                                .remove();

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




                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        }
    }
})

axios.get('/data/all/')
    .then(function (response) {
        // app.siteBasic = response.data.success;
        app.siteBasic = response.data.success
        // console.log(response.data);
    })
    .catch(function (error) {
        console.log(error);
    });