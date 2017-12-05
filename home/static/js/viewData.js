var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        site: 'Capa2',
        item: '',
        startTime: '2017-11-01',
        endTime: '2017-11-10',
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
                            vm.timeSeries = response.data.data;
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