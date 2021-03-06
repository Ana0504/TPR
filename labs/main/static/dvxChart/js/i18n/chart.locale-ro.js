(function (DateFormatter) {
    /**
      * dvxCharts Romanian Translation
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
            "Dum", "Lun", "Mar", "Mie", "Joi", "Vin", "Sâm",
            "Duminică", "Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă"
        ],
        monthNames: [
            "Ian", "Feb", "Mar", "Apr", "Mai", "Iun", "Iul", "Aug", "Sep", "Oct", "Noi", "Dec",
            "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"
        ],
        amPm: ["am", "pm", "AM", "PM"],
        /*
         Here is a problem in romanian: 
                M	/	F
         1st = primul / prima
         2nd = Al doilea / A doua
         3rd = Al treilea / A treia 
         4th = Al patrulea/ A patra
         5th = Al cincilea / A cincea 
         6th = Al șaselea / A șasea
         7th = Al șaptelea / A șaptea
         .... 
         */
        s: function (j) { return j < 11 || j > 13 ? ['st', 'nd', 'rd', 'th'][Math.min((j - 1) % 10, 3)] : 'th' },
        masks: {
            shortDate: "m/d/yyyy",
            shortTime: "h:MM TT",
            longTime: "h:MM:ss TT"
        }
    };
})(dvxCharts.DateFormatter);
