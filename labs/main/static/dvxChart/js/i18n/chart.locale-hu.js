(function (DateFormatter) {
    /**
      * dvxCharts Hungarian Translation
      * http://www.dvxcharts.com/ 
      * 
      * In order to use a particular language pack, you need to include the JavaScript language
      * pack to the head of your page, after referencing the dvxCharts.chart JavaScript file.
      * 
      * <script src="../js/dvxCharts.chart.min.js" type="text/javascript"></script>
      * <script src="../js/i18n/chart.locale-xx.js" type="text/javascript"></script>
      **/
    DateFormatter.DateFormat = {
        dayNames: [
            "Va", "Hé", "Ke", "Sze", "Csü", "Pé", "Szo",
            "Vasárnap", "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat"
        ],
        monthNames: [
            "Jan", "Feb", "Már", "Ápr", "Máj", "Jún", "Júl", "Aug", "Szep", "Okt", "Nov", "Dec",
            "Január", "Február", "Március", "Áprili", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"
        ],
        amPm: ["de", "du", "DE", "DU"],
        s: function (j) { return '.-ik'; },
        masks: {
            shortDate: "yyyy/d/m",
            shortTime: "tt h:MM",
            longTime: "tt h:MM:ss"
        }
    };
})(dvxCharts.DateFormatter);
