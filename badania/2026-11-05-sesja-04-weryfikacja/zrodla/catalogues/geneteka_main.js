var $_GET = {};
var iHist = 0;
var sUrl = 0;

delay = (function () {
    var timer = 0;
    return function (callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();

$(document).ready(function () {

    $("#sel_w").change(function () {
        getGET();
        $("#sel_rid").val($_GET['bdm']);
        $("#search_form").submit();
    });

    function formatsel(state) {
        var originalOption = state.element;
        return state.text + " <span>" + $(originalOption).data('years') + "</span>";
    }

    function matchStart(term, text) {
        if (latinize(text).toUpperCase().indexOf(latinize(term).toUpperCase()) == 0) {
            return true;
        }

        return false;
    }
    
    $("#search_clear").click(function() {
        
        $("#sel_rid option:first-child").prop("selected", true).change();
        $(".input-search").val('').change();
        $(".input-checkbox").prop('checked', false).change();
        
    });

 


    $.fn.select2.amd.require(['select2/compat/matcher'], function (oldMatcher) {
        $("#sel_rid").select2({
            templateResult: formatsel,
            templateSelection: formatsel,
            escapeMarkup: function (m) {
                return m;
            },
            "language": {
                "noResults": function () {
                    return _NORESULTS;
                }
            }
        });
    });

    var sSelKey = $("ul.tabs li.active").attr('data-key');
    var sSelRid = $("ul.tabs li.active").attr('data-rid');



    tabShow(sSelKey, sSelRid);

    checkLastname();

    $("#sel_rid").change(function () {
        checkLastname();
        getGET();
        var orgRid = $("#sel_rid option:selected").attr('data-' + sSelKey);
        if (orgRid != '' && orgRid != undefined) {
            $("#sel_rid option:selected").val(orgRid);

        } else {
            if ($("#sel_rid option:selected").attr('data-d') != undefined)
                $("input[name=bdm]").val('D');
            if ($("#sel_rid option:selected").attr('data-s') != undefined)
                $("input[name=bdm]").val('S');
            if ($("#sel_rid option:selected").attr('data-b') != undefined)
                $("input[name=bdm]").val('B');
        }
    });
    $("#sel_rid").change();

    $("#search_lastname, #search_lastname2, #search_name, #search_name2, #pair").change(function () {
        checkLastname();
    });

    $("#search_lastname, #search_lastname2, #search_name, #search_name2").keyup(function () {
        checkLastname();
    });
    
    $("#last").change(function() {
        $("#selectdays").prop("disabled", !$(this).prop("checked"));
    });
    $("#last").change();

    $('#zs_name').keyup(function () {
        var search = $(this).val();
        if (search != '') {
            $("#boczek").hide();
            $("#boczeksearch").show().html("<center>Wyszukiwanie...</center>");
            delay(function () {
                $("#boczeksearch").html("<center>Pobieranie...</center>");
                $.ajax({
                    url: "api/getParish.php?search=" + search
                }).done(function (data) {
                    $("#boczeksearch").html(data);
                });
            }, 300);
        } else {
            $("#boczek").show();
            $("#boczeksearch").hide();
        }
    });



    $('.tablesearch').on('preXhr.dt', function () {
        getGET();
    });

    $('.tablesearch').on('page.dt', function () {
        updateDatatablesUrl($(this));
    });

    $('.tablesearch').on('length.dt', function () {
        updateDatatablesUrl($(this));
    });

    $('.tablesearch').on('order.dt', function () {
        updateDatatablesUrl($(this));
    });

    $('.tablesearch').on('search.dt', function () {
        updateDatatablesUrl($(this));
    });

    $('.tablesearch').on('xhr.dt', function (e, settings, json, xhr) {
        var sParishes = '';
        for(var i in json.parishes) {
            var aParishes = json.parishes[i];
            var sParish = '- ' + aParishes[0][3] + ': ';
            for(var j in json.parishes[i]) {
                if (j > 0) {
                    sParish += ', ';
                }
                var aParish = json.parishes[i][j];
                var link = updateURL(window.location.href, 'rid', aParish[0]);
                var link = updateURL(link, 'near', '');
                var link = updateURL(link, 'w', i);
                var text = aParish[1];
                if (aParish[2] > 0) {
                     text += " [" + aParish[2] + "km]";
                }
                sParish += '<a href="'+link+'">'+text+'</a>';
            }
            sParishes += sParish + "<br/>";
        }
        
        $("#parishes").html(sParishes);
        $('#status').html("execTime:" + json.execTime + " sql:" + json.sql);
    });

    window.addEventListener('popstate', function (event) {
            console.log('onpopstate');
        if (event.state) {
            console.log('is event state');
            console.log(event);
            state = event.state;
            location.reload();
        }

    }, false);



});

function updateDatatablesUrl(datatable) {
    iHist = iHist + 1;
    getGET();
    var table = datatable.DataTable();
    var length = table.page.len();
    var page = table.page.info().page;
    var ordertable = table.order();
    var searchtable = table.search();
    sUrl = window.location.href;
    sUrl = updateURL(sUrl, 'ordertable', JSON.stringify(ordertable));
    sUrl = updateURL(sUrl, 'searchtable', searchtable);
    sUrl = updateURL(sUrl, 'rpp1', page * length);
    sUrl = updateURL(sUrl, 'rpp2', length);
    if (iHist > 2) {
        console.log('history push');
        window.history.pushState(null, document.title, sUrl);
    }
}


function getGET() {
    document.location.search.replace(/\??(?:([^=]+)=([^&]*)&?)/g, function () {
        function decode(s) {
            return decodeURIComponent(s.split("+").join(" "));
        }

        $_GET[decode(arguments[1])] = decode(arguments[2]);
    });
}

function checkLastname() {
    if ($("#search_lastname").val() != undefined) {

        if ($("#sel_rid").val() == "A" || $("#sel_rid").val() == "B" || $("#sel_rid").val() == "S" || $("#sel_rid").val() == "D") {
            $("#search_lastname").attr("required", "required");
            $("#near").prop("checked", false);
            $("#near").prop("disabled", true);
        } else {
            $("#search_lastname").removeAttr("required");
            if ($("#search_lastname").val().length > 1 || $("#search_lastname2").val().length > 1
                    || $("#search_name").val().length > 1 || $("#search_name2").val().length > 1) {
                $("#near").prop("disabled", false);
            } else {
                $("#near").prop("checked", false);
                $("#near").prop("disabled", true);
            }
        }

        if (($("#search_lastname").val() != '' || $("#search_name").val() != '') && ($("#search_lastname2").val() != '' || $("#search_name2").val() != '')) {
            $("#pair").prop("disabled", false);
            if ($("#pair").prop("checked")) {
                $("#person2").html($("#person2").data("spouse"));
                if ($("ul.tabs li.active").data("key") != "s") {
                    $("#parents").prop("checked", false);
                    $("#parents").prop("disabled", true);
                } else {
                    $("#parents").prop("disabled", false);
                }
            } else {
                $("#person2").html($("#person2").data("or"));
                $("#parents").prop("disabled", false);
            }
        } else {
            $("#pair").prop("checked", false);
            $("#pair").prop("disabled", true);
            $("#parents").prop("disabled", false);
        }
    }

}

function tabShow(type, rid) {
    displayStart = 0;
    ordertable = [[0, 'asc'], [1, 'asc'], [2, 'asc']];
    pageLength = 50;
    searchtable = '';

    getGET();

    if ($_GET['op'] = 'gt') {

        if (rid == '') {
            $_GET['rid'] = 'B';
        } else {
            $_GET['rid'] = rid;
            if (($_GET['bdm'] == undefined || $_GET['bdm'] == '') && type != undefined)
                $_GET['bdm'] = type.toString().toUpperCase();
        }
        if ($_GET['rpp1'] != undefined && $_GET['rpp1'] != '') {
            displayStart = parseInt($_GET['rpp1']);
        }
        if ($_GET['rpp2'] != undefined && $_GET['rpp2'] != '') {
            pageLength = parseInt($_GET['rpp2']);
        }
        if ($_GET['ordertable'] != undefined && $_GET['ordertable'] != '') {
            ordertable = JSON.parse($_GET['ordertable']);
        }
        if ($_GET['searchtable'] != undefined && $_GET['searchtable'] != '') {
            searchtable = $_GET['searchtable'];
        }
        $_GET['lang'] = sLang;

        oTable = $('#table_' + type).DataTable({
            "retrieve": true,
            "displayLength": pageLength,
            "lengthMenu": [10, 25, 50],
            "displayStart": displayStart,
            "processing": true,
            "serverSide": true,
            "pagingType": "simple_numbers",
            "ajax": {
                "url": "api/getAct.php",
                "contentType": "application/json; charset=UTF-8",
                "data": $_GET
            },
            "language": {
                "url": "lang/dt." + sLang + ".json"
            },
            "order": ordertable,
            "search": {
                "search": searchtable
            },
            "sDom": '<"top"flp>rt<"bottom"ip><"clear">',
            "columns": [
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                null,
                {"orderable": false, "searchable": false}
            ]
        });
    }



}

function updateURL(url, key, val) {
    var reExp = new RegExp("[\?|\&]" + key + "=[0-9a-zA-Z\_\+\-\|\.\,\;]*");
    if (reExp.test(url)) {
        var reExp = new RegExp("[\?&]" + key + "=([^&#]*)");
        var delimiter = reExp.exec(url)[0].charAt(0);
        url = url.replace(reExp, delimiter + key + "=" + val);
    } else {
        var newParam = key + "=" + val;
        if (!url.indexOf('?')) {
            url += '?';
        }
        if (url.indexOf('#') > -1) {
            var urlparts = url.split('#');
            url = urlparts[0] + "&" + newParam + (urlparts[1] ? "#" + urlparts[1] : '');
        } else {
            url += "&" + newParam;
        }
    }
    return url;
}



