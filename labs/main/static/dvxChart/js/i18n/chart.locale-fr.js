(function (DateFormatter) {
    /**
      * dvxCharts French Translation
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
            "Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam",
            "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"
        ],
        monthNames: [
            "Jan", "Fév", "Mar", "Avr", "Mai", "Jui", "Jul", "Aou", "Sep", "Oct", "Nov", "Déc",
            "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"
        ],
        amPm: ["am", "pm", "AM", "PM"],
        s: function (j) { return j == 1 ? 'er' : 'e'; },
        masks: {
            shortDate: "m/d/yyyy",
            shortTime: "h:MM TT",
            longTime: "h:MM:ss TT"
        }
    };
})(dvxCharts.DateFormatter);
