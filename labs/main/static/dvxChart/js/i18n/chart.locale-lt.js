(function (DateFormatter) {
    /**
      * dvxCharts Lithuanian Translation
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
            "Sek", "Pir", "Ant", "Tre", "Ket", "Pen", "Šeš",
            "Sekmadienis", "Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis"
        ],
        monthNames: [
            "Sau", "Vas", "Kov", "Bal", "Geg", "Bir", "Lie", "Rugj", "Rugs", "Spa", "Lap", "Gru",
            "Sausis", "Vasaris", "Kovas", "Balandis", "Gegužė", "Birželis", "Liepa", "Rugpjūtis", "Rugsėjis", "Spalis", "Lapkritis", "Gruodis"
        ],
        amPm: ["am", "pm", "AM", "PM"],
        s: function (j) { return j < 11 || j > 13 ? ['st', 'nd', 'rd', 'th'][Math.min((j - 1) % 10, 3)] : 'th' },
        masks: {
            shortDate: "m/d/yyyy",
            shortTime: "h:MM TT",
            longTime: "h:MM:ss TT"
        }
    };
})(dvxCharts.DateFormatter);
