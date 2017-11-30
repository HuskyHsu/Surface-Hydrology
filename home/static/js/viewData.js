var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        site: 'Capa2',
        item: '',
        startTime: '2017-11-01T10:00',
        endTime: '2017-11-10T08:00',
        siteBasic: [],
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