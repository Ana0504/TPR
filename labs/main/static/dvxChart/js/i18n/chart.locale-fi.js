(function (DateFormatter) {
    /**
      * dvxCharts (fi) Finnish Translation
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
            "Su", "Ma", "Ti", "Ke", "To", "Pe", "La",
            "Sunnuntai", "Maanantai", "Tiista", "Keskiviikko", "Torstai", "Perjantai", "Lauantai"
        ],
        monthNames: [
            "Tam", "Hel", "Maa", "Huh", "Tou", "Kes", "Hei", "Elo", "Syy", "Lok", "Mar", "Jou",
            "Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kes&auml;kuu", "Hein&auml;kuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"
        ],
        amPm: ["am", "pm", "AM", "PM"],
        s: function (j) { return j < 11 || j > 13 ? ['st', 'nd', 'rd', 'th'][Math.min((j - 1) % 10, 3)] : 'th' },
        masks: {
            shortDate: "dd.mm.yyyy",
            shortTime: "h:MM TT",
            longTime: "h:MM:ss TT"
        }
    };
})(dvxCharts.DateFormatter);
